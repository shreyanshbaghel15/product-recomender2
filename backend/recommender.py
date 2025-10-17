import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sqlalchemy.orm import Session
from typing import List, Dict, Tuple
import models
import pandas as pd

class ProductRecommender:
    def __init__(self, db: Session):
        self.db = db
        
    def get_user_interaction_matrix(self) -> Tuple[np.ndarray, List[int], List[int]]:
        """Create user-item interaction matrix for collaborative filtering"""
        interactions = self.db.query(models.UserInteraction).all()
        
        if not interactions:
            return np.array([]), [], []
        
        # Create interaction scores
        interaction_weights = {
            'view': 1,
            'click': 2,
            'cart': 3,
            'wishlist': 4,
            'purchase': 5
        }
        
        user_ids = list(set([i.user_id for i in interactions]))
        product_ids = list(set([i.product_id for i in interactions]))
        
        matrix = np.zeros((len(user_ids), len(product_ids)))
        
        for interaction in interactions:
            user_idx = user_ids.index(interaction.user_id)
            product_idx = product_ids.index(interaction.product_id)
            weight = interaction_weights.get(interaction.interaction_type, 1)
            
            if interaction.rating:
                weight *= interaction.rating / 5.0
            
            matrix[user_idx][product_idx] += weight
        
        return matrix, user_ids, product_ids
    
    def collaborative_filtering(self, user_id: int, n: int = 10) -> List[Tuple[int, float]]:
        """Collaborative filtering based on user similarity"""
        matrix, user_ids, product_ids = self.get_user_interaction_matrix()
        
        if len(matrix) == 0 or user_id not in user_ids:
            return []
        
        user_idx = user_ids.index(user_id)
        
        # Calculate user similarity
        user_similarity = cosine_similarity(matrix)
        similar_users = user_similarity[user_idx]
        
        # Get weighted scores for products
        scores = np.dot(similar_users, matrix)
        
        # Remove already interacted products
        user_interactions = matrix[user_idx]
        scores[user_interactions > 0] = -1
        
        # Get top N recommendations
        top_indices = np.argsort(scores)[::-1][:n]
        recommendations = [(product_ids[idx], scores[idx]) for idx in top_indices if scores[idx] > 0]
        
        return recommendations
    
    def content_based_filtering(self, user_id: int, n: int = 10) -> List[Tuple[int, float]]:
        """Content-based filtering using product features"""
        # Get user's interaction history
        user_interactions = self.db.query(models.UserInteraction).filter(
            models.UserInteraction.user_id == user_id
        ).all()
        
        if not user_interactions:
            return []
        
        # Get all products
        all_products = self.db.query(models.Product).all()
        
        if not all_products:
            return []
        
        # Create feature vectors from product descriptions, categories, and tags
        product_features = []
        product_ids = []
        
        for product in all_products:
            features = f"{product.name} {product.description} {product.category} {product.tags}"
            product_features.append(features)
            product_ids.append(product.id)
        
        # Vectorize features
        vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
        feature_matrix = vectorizer.fit_transform(product_features)
        
        # Get user profile based on interacted products
        interacted_product_ids = [i.product_id for i in user_interactions]
        interacted_indices = [product_ids.index(pid) for pid in interacted_product_ids if pid in product_ids]
        
        if not interacted_indices:
            return []
        
        # Create user profile as average of interacted products
        user_profile = feature_matrix[interacted_indices].mean(axis=0)
        
        # Calculate similarity with all products
        similarities = cosine_similarity(user_profile, feature_matrix)[0]
        
        # Remove already interacted products
        for idx in interacted_indices:
            similarities[idx] = -1
        
        # Get top N recommendations
        top_indices = np.argsort(similarities)[::-1][:n]
        recommendations = [(product_ids[idx], similarities[idx]) for idx in top_indices if similarities[idx] > 0]
        
        return recommendations
    
    def hybrid_recommendations(self, user_id: int, n: int = 5) -> List[Tuple[int, float, str]]:
        """Combine collaborative and content-based filtering"""
        collab_recs = self.collaborative_filtering(user_id, n * 2)
        content_recs = self.content_based_filtering(user_id, n * 2)
        
        # If no collaborative filtering results, use content-based
        if not collab_recs and not content_recs:
            # Return popular products for cold start
            return self.get_popular_products(n)
        
        # Combine scores
        combined_scores = {}
        
        for product_id, score in collab_recs:
            combined_scores[product_id] = combined_scores.get(product_id, 0) + score * 0.6
        
        for product_id, score in content_recs:
            combined_scores[product_id] = combined_scores.get(product_id, 0) + score * 0.4
        
        # Sort by combined score
        sorted_recs = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)[:n]
        
        # Determine recommendation reason
        results = []
        for product_id, score in sorted_recs:
            reason = "hybrid"
            if product_id in [p[0] for p in collab_recs] and product_id in [p[0] for p in content_recs]:
                reason = "collaborative_and_content"
            elif product_id in [p[0] for p in collab_recs]:
                reason = "collaborative"
            else:
                reason = "content"
            
            results.append((product_id, score, reason))
        
        return results
    
    def get_popular_products(self, n: int = 5) -> List[Tuple[int, float, str]]:
        """Get popular products for cold start problem"""
        products = self.db.query(models.Product).order_by(models.Product.rating.desc()).limit(n).all()
        return [(p.id, p.rating, "popular") for p in products]
    
    def get_user_behavior_summary(self, user_id: int) -> Dict:
        """Get summary of user behavior for LLM context"""
        interactions = self.db.query(models.UserInteraction).filter(
            models.UserInteraction.user_id == user_id
        ).all()
        
        if not interactions:
            return {
                "total_interactions": 0,
                "categories": [],
                "recent_products": [],
                "interaction_types": {}
            }
        
        # Get product details
        product_ids = [i.product_id for i in interactions]
        products = self.db.query(models.Product).filter(models.Product.id.in_(product_ids)).all()
        product_map = {p.id: p for p in products}
        
        # Analyze behavior
        categories = {}
        interaction_types = {}
        recent_products = []
        
        for interaction in sorted(interactions, key=lambda x: x.timestamp, reverse=True)[:5]:
            product = product_map.get(interaction.product_id)
            if product:
                recent_products.append(product.name)
                categories[product.category] = categories.get(product.category, 0) + 1
            
            interaction_types[interaction.interaction_type] = interaction_types.get(interaction.interaction_type, 0) + 1
        
        return {
            "total_interactions": len(interactions),
            "categories": sorted(categories.items(), key=lambda x: x[1], reverse=True),
            "recent_products": recent_products,
            "interaction_types": interaction_types
        }
