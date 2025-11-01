"""
Configuration settings for Blockchain Scalability Showcase
"""
import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-blockchain-2025'
    DEBUG = False
    TESTING = False
    
    # Application settings
    APP_NAME = "Blockchain Scalability Showcase"
    APP_VERSION = "1.0.0"
    
    # Paper metadata
    PAPER_TITLE = "Blockchain Scalability Challenges and Solutions: A Comparative Analysis of Layer 2 Implementations and Sharding"
    PAPER_AUTHOR = "Neha Sachdeva"
    
    # Performance constants (based on research paper)
    ETHEREUM_BASE_TPS = 15
    BITCOIN_TPS = 7
    VISA_TPS = 24000
    
    # Layer 2 metrics
    LAYER2_TPS_RANGE = (2000, 4000)
    LAYER2_COST_REDUCTION = (10, 100)  # 10-100x reduction
    OPTIMISTIC_FINALITY_DAYS = 7
    ZK_FINALITY = "instant"
    
    # Sharding metrics
    BASE_SHARD_TPS = 100
    MAX_SHARDS = 64
    CROSS_SHARD_LATENCY_MULTIPLIER = 1.5
    
    # Visualization settings
    CHART_COLORS = {
        'layer1': '#3b82f6',      # Blue
        'layer2': '#8b5cf6',      # Purple
        'sharding': '#10b981',    # Green
        'hybrid': '#f59e0b',      # Orange
        'comparison': '#ef4444'   # Red
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
