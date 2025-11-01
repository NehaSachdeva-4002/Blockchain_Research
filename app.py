"""
Main Flask application for Blockchain Scalability Showcase
Research paper: Blockchain Scalability Challenges and Solutions
Author: Neha Sachdeva
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from config import config
from data.metrics import BlockchainMetrics
from data.calculations import ScalabilityCalculator

def create_app(config_name='development'):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    
    # Initialize data handlers
    metrics = BlockchainMetrics()
    calculator = ScalabilityCalculator()
    
    # Routes
    @app.route('/')
    def index():
        """Landing page with paper overview"""
        return render_template('index.html',
                             paper_title=app.config['PAPER_TITLE'],
                             author=app.config['PAPER_AUTHOR'])
    
    @app.route('/comparison')
    def comparison():
        """Interactive comparison dashboard"""
        return render_template('comparison.html')
    
    @app.route('/layer2')
    def layer2():
        """Layer 2 deep dive page"""
        return render_template('layer2.html')
    
    @app.route('/sharding')
    def sharding():
        """Sharding analysis page"""
        return render_template('sharding.html')
    
    @app.route('/hybrid')
    def hybrid():
        """Hybrid model showcase page"""
        return render_template('hybrid.html')
    
    # API Endpoints
    @app.route('/api/metrics/all')
    def api_all_metrics():
        """Get all blockchain metrics"""
        return jsonify({
            'success': True,
            'data': metrics.get_all_solutions()
        })
    
    @app.route('/api/metrics/base')
    def api_base_metrics():
        """Get base layer metrics"""
        return jsonify({
            'success': True,
            'data': metrics.BASE_LAYER
        })
    
    @app.route('/api/metrics/layer2')
    def api_layer2_metrics():
        """Get Layer 2 solution metrics"""
        return jsonify({
            'success': True,
            'data': metrics.LAYER2_SOLUTIONS
        })
    
    @app.route('/api/metrics/sharding')
    def api_sharding_metrics():
        """Get sharding solution metrics"""
        return jsonify({
            'success': True,
            'data': metrics.SHARDING_SOLUTIONS
        })
    
    @app.route('/api/metrics/trilemma')
    def api_trilemma():
        """Get blockchain trilemma data"""
        return jsonify({
            'success': True,
            'data': metrics.get_trilemma_data()
        })
    
    @app.route('/api/metrics/comparison')
    def api_comparison():
        """Get comparison table data"""
        return jsonify({
            'success': True,
            'data': metrics.get_comparison_summary()
        })
    
    @app.route('/api/metrics/security')
    def api_security():
        """Get security attack vectors"""
        return jsonify({
            'success': True,
            'data': metrics.SECURITY_VECTORS
        })
    
    @app.route('/api/calculate/layer2', methods=['POST'])
    def api_calculate_layer2():
        """Calculate Layer 2 performance"""
        data = request.get_json()
        tx_volume = data.get('tx_volume', 1000000)
        batch_size = data.get('batch_size', 100)
        gas_price = data.get('gas_price', 20)
        
        result = calculator.calculate_layer2_performance(
            tx_volume, batch_size, gas_price
        )
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    @app.route('/api/calculate/sharding', methods=['POST'])
    def api_calculate_sharding():
        """Calculate sharding performance"""
        data = request.get_json()
        tx_volume = data.get('tx_volume', 1000000)
        num_shards = data.get('num_shards', 64)
        tps_per_shard = data.get('tps_per_shard', 100)
        
        result = calculator.calculate_sharding_performance(
            tx_volume, num_shards, tps_per_shard
        )
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    @app.route('/api/calculate/hybrid', methods=['POST'])
    def api_calculate_hybrid():
        """Calculate hybrid model performance"""
        data = request.get_json()
        tx_volume = data.get('tx_volume', 1000000)
        num_shards = data.get('num_shards', 32)
        layer2_multiplier = data.get('layer2_multiplier', 50)
        
        result = calculator.calculate_hybrid_model(
            tx_volume, num_shards, layer2_multiplier
        )
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    @app.route('/api/calculate/compare', methods=['POST'])
    def api_compare_all():
        """Compare all scalability solutions"""
        data = request.get_json()
        tx_volume = data.get('tx_volume', 1000000)
        
        result = calculator.compare_all_solutions(tx_volume)
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    @app.route('/api/calculate/trilemma', methods=['POST'])
    def api_calculate_trilemma():
        """Calculate trilemma balance score"""
        data = request.get_json()
        scalability = data.get('scalability', 50)
        security = data.get('security', 50)
        decentralization = data.get('decentralization', 50)
        
        result = calculator.calculate_trilemma_score(
            scalability, security, decentralization
        )
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Resource not found'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    print("\n" + "="*60)
    print("🚀 Blockchain Scalability Showcase")
    print("📄 Research Paper by Neha Sachdeva")
    print("="*60)
    print("\n📊 API Endpoints Available:")
    print("  • GET  /api/metrics/all")
    print("  • GET  /api/metrics/layer2")
    print("  • GET  /api/metrics/sharding")
    print("  • GET  /api/metrics/trilemma")
    print("  • POST /api/calculate/layer2")
    print("  • POST /api/calculate/sharding")
    print("  • POST /api/calculate/hybrid")
    print("  • POST /api/calculate/compare")
    print("\n🌐 Starting server...\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
