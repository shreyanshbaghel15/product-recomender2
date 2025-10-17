import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('recommendations');

  useEffect(() => {
    fetchUsers();
    fetchProducts();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get(`${API_URL}/users`);
      setUsers(response.data);
      if (response.data.length > 0) {
        setSelectedUser(response.data[0].id);
      }
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const fetchProducts = async () => {
    try {
      const response = await axios.get(`${API_URL}/products`);
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  const fetchRecommendations = async () => {
    if (!selectedUser) return;
    
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/recommendations/${selectedUser}`);
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUserChange = (e) => {
    setSelectedUser(parseInt(e.target.value));
  };

  const handleInteraction = async (productId, interactionType) => {
    if (!selectedUser) return;
    
    try {
      await axios.post(`${API_URL}/interactions`, {
        user_id: selectedUser,
        product_id: productId,
        interaction_type: interactionType
      });
      
      // Refresh recommendations after interaction
      if (activeTab === 'recommendations') {
        fetchRecommendations();
      }
    } catch (error) {
      console.error('Error creating interaction:', error);
    }
  };

  useEffect(() => {
    if (selectedUser && activeTab === 'recommendations') {
      fetchRecommendations();
    }
  }, [selectedUser, activeTab]);

  return (
    <div className="App">
      <header className="header">
        <div className="container">
          <h1>🛍️ AI Product Recommender</h1>
          <p>Personalized recommendations powered by machine learning</p>
        </div>
      </header>

      <div className="container">
        <div className="user-selector">
          <label htmlFor="user-select">Select User:</label>
          <select id="user-select" value={selectedUser || ''} onChange={handleUserChange}>
            {users.map(user => (
              <option key={user.id} value={user.id}>
                {user.username} ({user.email})
              </option>
            ))}
          </select>
        </div>

        <div className="tabs">
          <button 
            className={`tab ${activeTab === 'recommendations' ? 'active' : ''}`}
            onClick={() => setActiveTab('recommendations')}
          >
            Recommendations
          </button>
          <button 
            className={`tab ${activeTab === 'products' ? 'active' : ''}`}
            onClick={() => setActiveTab('products')}
          >
            All Products
          </button>
        </div>

        {activeTab === 'recommendations' && (
          <div className="recommendations-section">
            <div className="section-header">
              <h2>Personalized Recommendations</h2>
              <button className="refresh-btn" onClick={fetchRecommendations} disabled={loading}>
                {loading ? '🔄 Loading...' : '🔄 Refresh'}
              </button>
            </div>

            {loading ? (
              <div className="loading">Loading recommendations...</div>
            ) : recommendations.length === 0 ? (
              <div className="empty-state">
                <p>No recommendations available. Try interacting with some products first!</p>
              </div>
            ) : (
              <div className="products-grid">
                {recommendations.map((rec, index) => (
                  <div key={rec.product.id} className="product-card recommended">
                    <div className="recommendation-badge">#{index + 1} Recommended</div>
                    <img src={rec.product.image_url} alt={rec.product.name} />
                    <div className="product-info">
                      <h3>{rec.product.name}</h3>
                      <p className="category">{rec.product.category}</p>
                      <p className="description">{rec.product.description}</p>
                      <div className="rating">
                        {'⭐'.repeat(Math.round(rec.product.rating))} {rec.product.rating}
                      </div>
                      <p className="price">${rec.product.price}</p>
                      <div className="explanation">
                        <strong>Why this product?</strong>
                        <p>{rec.explanation}</p>
                      </div>
                      <div className="match-score">
                        Match Score: {(rec.score * 100).toFixed(0)}%
                      </div>
                      <div className="actions">
                        <button onClick={() => handleInteraction(rec.product.id, 'view')}>
                          👁️ View
                        </button>
                        <button onClick={() => handleInteraction(rec.product.id, 'cart')}>
                          🛒 Add to Cart
                        </button>
                        <button onClick={() => handleInteraction(rec.product.id, 'wishlist')}>
                          ❤️ Wishlist
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === 'products' && (
          <div className="products-section">
            <h2>All Products</h2>
            <div className="products-grid">
              {products.map(product => (
                <div key={product.id} className="product-card">
                  <img src={product.image_url} alt={product.name} />
                  <div className="product-info">
                    <h3>{product.name}</h3>
                    <p className="category">{product.category}</p>
                    <p className="description">{product.description}</p>
                    <div className="rating">
                      {'⭐'.repeat(Math.round(product.rating))} {product.rating}
                    </div>
                    <p className="price">${product.price}</p>
                    <div className="actions">
                      <button onClick={() => handleInteraction(product.id, 'view')}>
                        👁️ View
                      </button>
                      <button onClick={() => handleInteraction(product.id, 'cart')}>
                        🛒 Add to Cart
                      </button>
                      <button onClick={() => handleInteraction(product.id, 'wishlist')}>
                        ❤️ Wishlist
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <footer className="footer">
        <p>Built with ❤️ using FastAPI, React, and OpenAI</p>
      </footer>
    </div>
  );
}

export default App;
