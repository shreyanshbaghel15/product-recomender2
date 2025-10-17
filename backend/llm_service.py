import os
from openai import OpenAI
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.client = OpenAI(api_key=api_key)
            self.enabled = True
        else:
            self.client = None
            self.enabled = False
    
    def generate_explanation(
        self, 
        product_name: str, 
        product_description: str,
        product_category: str,
        user_behavior: Dict,
        recommendation_reason: str
    ) -> str:
        """Generate LLM-powered explanation for why a product is recommended"""
        
        if not self.enabled:
            return self._generate_fallback_explanation(
                product_name, product_category, user_behavior, recommendation_reason
            )
        
        # Build context from user behavior
        behavior_context = self._build_behavior_context(user_behavior)
        
        # Create prompt for LLM
        prompt = f"""You are a helpful e-commerce assistant. Explain why we're recommending this product to the user in a friendly, concise way (2-3 sentences max).

Product Details:
- Name: {product_name}
- Category: {product_category}
- Description: {product_description}

User Behavior:
{behavior_context}

Recommendation Method: {recommendation_reason}

Generate a personalized explanation for why this product is recommended to this user. Make it engaging and highlight the connection to their interests."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful e-commerce recommendation assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"LLM Error: {e}")
            return self._generate_fallback_explanation(
                product_name, product_category, user_behavior, recommendation_reason
            )
    
    def _build_behavior_context(self, user_behavior: Dict) -> str:
        """Build readable context from user behavior data"""
        context_parts = []
        
        if user_behavior.get("total_interactions", 0) > 0:
            context_parts.append(f"- Total interactions: {user_behavior['total_interactions']}")
        
        if user_behavior.get("categories"):
            top_categories = [cat for cat, _ in user_behavior["categories"][:3]]
            context_parts.append(f"- Favorite categories: {', '.join(top_categories)}")
        
        if user_behavior.get("recent_products"):
            recent = user_behavior["recent_products"][:3]
            context_parts.append(f"- Recently viewed: {', '.join(recent)}")
        
        if user_behavior.get("interaction_types"):
            types = user_behavior["interaction_types"]
            context_parts.append(f"- Interaction types: {', '.join([f'{k}({v})' for k, v in types.items()])}")
        
        return "\n".join(context_parts) if context_parts else "- New user with limited history"
    
    def _generate_fallback_explanation(
        self, 
        product_name: str, 
        product_category: str,
        user_behavior: Dict,
        recommendation_reason: str
    ) -> str:
        """Generate rule-based explanation when LLM is not available"""
        
        if recommendation_reason == "popular":
            return f"This {product_category} is highly rated and popular among our customers. It's a great choice to explore!"
        
        if recommendation_reason == "collaborative":
            return f"Based on your shopping patterns, users with similar interests loved this {product_category}. We think you'll enjoy it too!"
        
        if recommendation_reason == "content":
            categories = user_behavior.get("categories", [])
            if categories:
                top_cat = categories[0][0]
                return f"Since you've shown interest in {top_cat}, this {product_category} matches your preferences perfectly!"
            return f"This {product_category} aligns well with your browsing history and interests."
        
        if recommendation_reason == "collaborative_and_content":
            return f"This {product_name} is a perfect match! It's popular among users like you and matches your interests in {product_category}."
        
        return f"We recommend this {product_category} based on your unique shopping profile and preferences."
