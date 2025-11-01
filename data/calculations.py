"""
Scalability calculations and performance modeling
"""
import math

class ScalabilityCalculator:
    """
    Calculate blockchain performance metrics based on user inputs
    and research paper formulas
    """
    
    @staticmethod
    def calculate_layer2_performance(tx_volume, batch_size=100, gas_price=20):
        """
        Calculate Layer 2 rollup performance metrics
        
        Args:
            tx_volume: Number of transactions
            batch_size: Transactions per batch
            gas_price: Gas price in gwei
            
        Returns:
            dict: Performance metrics
        """
        # Optimistic Rollup calculations
        num_batches = math.ceil(tx_volume / batch_size)
        
        # Cost reduction: 10-100x (use average of 55x)
        l1_cost = tx_volume * gas_price * 21000  # Standard ETH transfer
        l2_cost = l1_cost / 55  # Average cost reduction
        
        # TPS calculation (2000-4000 range, use 3000 average)
        avg_tps = 3000
        processing_time = tx_volume / avg_tps
        
        optimistic_metrics = {
            'solution': 'Optimistic Rollup',
            'tps': avg_tps,
            'processing_time_seconds': round(processing_time, 2),
            'num_batches': num_batches,
            'l1_cost_gwei': round(l1_cost, 2),
            'l2_cost_gwei': round(l2_cost, 2),
            'cost_savings_percent': 98.18,  # (1 - 1/55) * 100
            'finality_time': '7 days',
            'withdrawal_delay': '7 days',
            'security_inheritance': 'Full L1 security'
        }
        
        # ZK Rollup calculations (similar TPS, better finality)
        zk_cost = l1_cost / 60  # Slightly better cost reduction
        
        zk_metrics = {
            'solution': 'ZK Rollup',
            'tps': avg_tps,
            'processing_time_seconds': round(processing_time, 2),
            'num_batches': num_batches,
            'l1_cost_gwei': round(l1_cost, 2),
            'l2_cost_gwei': round(zk_cost, 2),
            'cost_savings_percent': 98.33,
            'finality_time': 'instant',
            'withdrawal_delay': 'minutes',
            'security_inheritance': 'Full L1 security + ZK proofs'
        }
        
        return {
            'optimistic': optimistic_metrics,
            'zk': zk_metrics,
            'comparison': {
                'faster_finality': 'ZK Rollup',
                'faster_withdrawal': 'ZK Rollup',
                'lower_cost': 'ZK Rollup',
                'maturity': 'Optimistic Rollup'
            }
        }
    
    @staticmethod
    def calculate_sharding_performance(tx_volume, num_shards=64, tps_per_shard=100):
        """
        Calculate sharding performance metrics
        
        Args:
            tx_volume: Number of transactions
            num_shards: Number of parallel shards
            tps_per_shard: Transactions per second per shard
            
        Returns:
            dict: Performance metrics
        """
        # Total TPS scales linearly with shard count
        total_tps = num_shards * tps_per_shard
        
        # Processing time
        processing_time = tx_volume / total_tps
        
        # Estimate cross-shard transactions (assume 20% require cross-shard)
        cross_shard_ratio = 0.20
        cross_shard_txs = int(tx_volume * cross_shard_ratio)
        intra_shard_txs = tx_volume - cross_shard_txs
        
        # Cross-shard latency is 1.5x higher
        cross_shard_latency_multiplier = 1.5
        avg_latency = (intra_shard_txs * 1.0 + cross_shard_txs * cross_shard_latency_multiplier) / tx_volume
        
        # Throughput improvement based on paper findings (19.5%)
        base_throughput = 15  # Ethereum base
        improved_throughput = total_tps * 1.195
        
        # Latency reduction (25% from paper)
        base_latency = 15  # seconds
        reduced_latency = base_latency * 0.75
        
        metrics = {
            'solution': f'Sharding ({num_shards} shards)',
            'num_shards': num_shards,
            'tps_per_shard': tps_per_shard,
            'total_tps': total_tps,
            'processing_time_seconds': round(processing_time, 2),
            'intra_shard_txs': intra_shard_txs,
            'cross_shard_txs': cross_shard_txs,
            'cross_shard_percentage': cross_shard_ratio * 100,
            'avg_latency_multiplier': round(avg_latency, 2),
            'throughput_improvement_percent': 19.5,
            'latency_reduction_percent': 25,
            'base_layer_comparison': {
                'base_tps': base_throughput,
                'sharded_tps': total_tps,
                'improvement_factor': round(total_tps / base_throughput, 1)
            },
            'scalability': 'Linear with shard count',
            'security_model': 'Random validator assignment per shard'
        }
        
        return metrics
    
    @staticmethod
    def calculate_hybrid_model(tx_volume, num_shards=32, layer2_multiplier=50):
        """
        Calculate hybrid (Layer 2 + Sharding) performance
        
        Args:
            tx_volume: Number of transactions
            num_shards: Number of shards in base layer
            layer2_multiplier: Additional scaling from Layer 2
            
        Returns:
            dict: Performance metrics
        """
        # Base sharded layer TPS
        base_tps_per_shard = 100
        base_sharded_tps = num_shards * base_tps_per_shard
        
        # Layer 2 on top of each shard
        hybrid_tps = base_sharded_tps * layer2_multiplier
        
        processing_time = tx_volume / hybrid_tps
        
        metrics = {
            'solution': 'Hybrid Model (Layer 2 + Sharding)',
            'base_layer': f'Sharded ({num_shards} shards)',
            'layer2': 'Rollups on each shard',
            'base_sharded_tps': base_sharded_tps,
            'layer2_multiplier': layer2_multiplier,
            'total_hybrid_tps': hybrid_tps,
            'processing_time_seconds': round(processing_time, 2),
            'scalability_type': 'Exponential (multiplicative)',
            'cost_efficiency': 'Optimal (combined benefits)',
            'security': 'Layered (L1 sharding + L2 proofs)',
            'use_case': 'Web3 global infrastructure',
            'examples': ['Solana + Layer 2', 'Shardeum', 'Future Ethereum']
        }
        
        return metrics
    
    @staticmethod
    def compare_all_solutions(tx_volume=1000000):
        """
        Compare all scalability solutions for given transaction volume
        
        Args:
            tx_volume: Number of transactions to process
            
        Returns:
            dict: Comprehensive comparison
        """
        calc = ScalabilityCalculator()
        
        # Base Layer
        base_tps = 15
        base_time = tx_volume / base_tps
        
        # Layer 2
        layer2 = calc.calculate_layer2_performance(tx_volume)
        
        # Sharding
        sharding = calc.calculate_sharding_performance(tx_volume, num_shards=64)
        
        # Hybrid
        hybrid = calc.calculate_hybrid_model(tx_volume, num_shards=32, layer2_multiplier=50)
        
        comparison = {
            'transaction_volume': tx_volume,
            'solutions': {
                'base_layer': {
                    'name': 'Ethereum Base Layer',
                    'tps': base_tps,
                    'processing_time_seconds': round(base_time, 2),
                    'processing_time_hours': round(base_time / 3600, 2)
                },
                'layer2_optimistic': layer2['optimistic'],
                'layer2_zk': layer2['zk'],
                'sharding': sharding,
                'hybrid': hybrid
            },
            'rankings': {
                'fastest': 'Hybrid Model',
                'most_secure': 'Layer 2 ZK Rollup',
                'most_decentralized': 'Sharding',
                'best_cost': 'Layer 2 ZK Rollup',
                'production_ready': 'Layer 2 Optimistic Rollup',
                'future_potential': 'Hybrid Model'
            }
        }
        
        return comparison
    
    @staticmethod
    def calculate_trilemma_score(scalability, security, decentralization):
        """
        Calculate overall blockchain trilemma balance score
        
        Args:
            scalability: 0-100 score
            security: 0-100 score
            decentralization: 0-100 score
            
        Returns:
            dict: Trilemma analysis
        """
        # Balanced score (geometric mean)
        balanced_score = (scalability * security * decentralization) ** (1/3)
        
        # Identify weakest dimension
        scores = {
            'scalability': scalability,
            'security': security,
            'decentralization': decentralization
        }
        weakest = min(scores, key=scores.get)
        strongest = max(scores, key=scores.get)
        
        # Calculate trade-off coefficient
        variance = sum((s - balanced_score) ** 2 for s in scores.values()) / 3
        
        return {
            'balanced_score': round(balanced_score, 2),
            'individual_scores': scores,
            'weakest_dimension': weakest,
            'strongest_dimension': strongest,
            'trade_off_variance': round(variance, 2),
            'is_balanced': variance < 100,  # Low variance = more balanced
            'recommendation': f"Optimize {weakest} to improve overall balance"
        }
