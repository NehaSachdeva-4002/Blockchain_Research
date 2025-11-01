"""
Blockchain performance metrics based on research paper findings
"""

class BlockchainMetrics:
    """
    Static metrics from the research paper:
    "Blockchain Scalability Challenges and Solutions"
    """
    
    # Base Layer (Layer 1) Performance
    BASE_LAYER = {
        'bitcoin': {
            'name': 'Bitcoin',
            'tps': 7,
            'block_time': 600,  # 10 minutes in seconds
            'block_size_mb': 1,
            'consensus': 'Proof of Work',
            'finality_time': '60 minutes (6 confirmations)',
            'decentralization_score': 95,
            'security_score': 98
        },
        'ethereum': {
            'name': 'Ethereum 1.0',
            'tps': 15,
            'block_time': 15,  # 15 seconds
            'block_size_mb': 'variable',
            'consensus': 'Proof of Stake',
            'finality_time': '~13 minutes',
            'decentralization_score': 90,
            'security_score': 95
        },
        'visa': {
            'name': 'Visa (Traditional)',
            'tps': 24000,
            'block_time': 'N/A',
            'consensus': 'Centralized',
            'finality_time': 'instant',
            'decentralization_score': 0,
            'security_score': 85
        }
    }
    
    # Layer 2 Solutions
    LAYER2_SOLUTIONS = {
        'lightning_network': {
            'name': 'Lightning Network',
            'type': 'Payment Channels',
            'parent_chain': 'Bitcoin',
            'tps': 1000000,  # Theoretical unlimited
            'avg_transaction_cost_usd': 0.0001,
            'finality_time': 'instant',
            'security_model': 'Game-theoretic + timelocks',
            'withdrawal_delay': 'none',
            'cost_reduction': '99%',
            'complexity': 'Medium',
            'use_cases': ['Micropayments', 'Cross-border remittances'],
            'security_score': 80,
            'decentralization_score': 85
        },
        'polygon': {
            'name': 'Polygon',
            'type': 'Sidechain',
            'parent_chain': 'Ethereum',
            'tps': 7000,
            'avg_transaction_cost_usd': 0.01,
            'finality_time': '2-3 seconds',
            'security_model': 'Own validator set',
            'withdrawal_delay': '~30 minutes',
            'cost_reduction': '99.9%',
            'complexity': 'Low',
            'use_cases': ['DeFi', 'NFTs', 'Gaming'],
            'security_score': 70,
            'decentralization_score': 65
        },
        'optimism': {
            'name': 'Optimism',
            'type': 'Optimistic Rollup',
            'parent_chain': 'Ethereum',
            'tps': 2000,
            'avg_transaction_cost_usd': 0.10,
            'finality_time': '7 days (challenge period)',
            'security_model': 'Inherits L1 + fraud proofs',
            'withdrawal_delay': '7 days',
            'cost_reduction': '10-100x',
            'complexity': 'High',
            'use_cases': ['DeFi', 'General purpose dApps'],
            'security_score': 90,
            'decentralization_score': 85
        },
        'arbitrum': {
            'name': 'Arbitrum',
            'type': 'Optimistic Rollup',
            'parent_chain': 'Ethereum',
            'tps': 4000,
            'avg_transaction_cost_usd': 0.08,
            'finality_time': '7 days (challenge period)',
            'security_model': 'Inherits L1 + fraud proofs',
            'withdrawal_delay': '7 days',
            'cost_reduction': '10-100x',
            'complexity': 'High',
            'use_cases': ['DeFi', 'NFT marketplaces'],
            'security_score': 90,
            'decentralization_score': 80
        },
        'zksync': {
            'name': 'zkSync',
            'type': 'ZK Rollup',
            'parent_chain': 'Ethereum',
            'tps': 2000,
            'avg_transaction_cost_usd': 0.05,
            'finality_time': 'instant',
            'security_model': 'Inherits L1 + ZK proofs (SNARKs)',
            'withdrawal_delay': 'minutes',
            'cost_reduction': '10-100x',
            'complexity': 'Very High',
            'use_cases': ['Payments', 'DeFi', 'Privacy applications'],
            'security_score': 95,
            'decentralization_score': 80
        },
        'starknet': {
            'name': 'Starknet',
            'type': 'ZK Rollup',
            'parent_chain': 'Ethereum',
            'tps': 3000,
            'avg_transaction_cost_usd': 0.04,
            'finality_time': 'instant',
            'security_model': 'Inherits L1 + ZK proofs (STARKs)',
            'withdrawal_delay': 'minutes',
            'cost_reduction': '10-100x',
            'complexity': 'Very High',
            'use_cases': ['Complex computations', 'Gaming', 'DeFi'],
            'security_score': 95,
            'decentralization_score': 75
        }
    }
    
    # Sharding Solutions
    SHARDING_SOLUTIONS = {
        'ethereum_2': {
            'name': 'Ethereum 2.0',
            'status': 'In Development',
            'num_shards': 64,
            'tps_per_shard': 100,
            'total_tps': 6400,  # 64 shards * 100 TPS
            'consensus': 'Proof of Stake',
            'cross_shard_latency': 'Medium',
            'security_model': 'Random validator assignment',
            'implementation_status': 'Phased rollout',
            'throughput_improvement': '19.5%',
            'latency_reduction': '25%',
            'complexity': 'Very High',
            'security_score': 90,
            'decentralization_score': 95
        },
        'zilliqa': {
            'name': 'Zilliqa',
            'status': 'Live',
            'num_shards': 8,
            'tps_per_shard': 312,
            'total_tps': 2500,
            'consensus': 'Practical Byzantine Fault Tolerance (pBFT)',
            'cross_shard_latency': 'Low',
            'security_model': 'Random node assignment',
            'implementation_status': 'Production (Zilliqa 2.0)',
            'complexity': 'High',
            'use_cases': ['High-throughput transactions', 'DeFi', 'Gaming'],
            'security_score': 85,
            'decentralization_score': 80
        },
        'near': {
            'name': 'NEAR Protocol',
            'status': 'Live',
            'num_shards': 'Dynamic',
            'tps_per_shard': 100,
            'total_tps': 100000,  # Theoretical with many shards
            'consensus': 'Nightshade (PoS-based sharding)',
            'cross_shard_latency': 'Low',
            'security_model': 'Dynamic resharding + validator rotation',
            'implementation_status': 'Production',
            'complexity': 'Very High',
            'use_cases': ['Web3 applications', 'DeFi', 'NFTs'],
            'security_score': 88,
            'decentralization_score': 85
        },
        'elrond': {
            'name': 'Elrond (MultiversX)',
            'status': 'Live',
            'num_shards': 3,
            'tps_per_shard': 5000,
            'total_tps': 15000,
            'consensus': 'Secure Proof of Stake',
            'cross_shard_latency': 'Very Low',
            'security_model': 'Adaptive state sharding',
            'implementation_status': 'Production',
            'complexity': 'High',
            'use_cases': ['Enterprise', 'DeFi', 'Metaverse'],
            'security_score': 90,
            'decentralization_score': 82
        }
    }
    
    # Blockchain Trilemma Characteristics
    TRILEMMA = {
        'layer1_bitcoin': {
            'scalability': 10,      # Low
            'security': 98,         # Very High
            'decentralization': 95  # Very High
        },
        'layer1_ethereum': {
            'scalability': 20,
            'security': 95,
            'decentralization': 90
        },
        'layer2_optimistic': {
            'scalability': 85,
            'security': 90,
            'decentralization': 85
        },
        'layer2_zk': {
            'scalability': 85,
            'security': 95,
            'decentralization': 80
        },
        'layer2_sidechain': {
            'scalability': 90,
            'security': 70,
            'decentralization': 65
        },
        'sharding_ethereum': {
            'scalability': 88,
            'security': 90,
            'decentralization': 95
        },
        'sharding_zilliqa': {
            'scalability': 80,
            'security': 85,
            'decentralization': 80
        },
        'hybrid_model': {
            'scalability': 95,
            'security': 92,
            'decentralization': 88
        }
    }
    
    # Comparison Metrics Summary
    COMPARISON_TABLE = {
        'Layer 2 (Rollups)': {
            'throughput': 'Thousands TPS (2000-4000)',
            'performance': 'Low latency off-chain, batch settlement delay',
            'security': 'Inherits L1 security (rollups)',
            'complexity': 'Medium to High',
            'cross_chain': 'Bridges required, withdrawal delays',
            'cost_efficiency': 'Lower fees (10-100x reduction)',
            'ecosystem_adoption': 'Rapid, modular, many live projects',
            'best_for': 'Immediate scaling, DeFi, NFT use cases'
        },
        'Sharding': {
            'throughput': 'Linear TPS scaling (up to 100K+ TPS)',
            'performance': 'Fast per shard, cross-shard higher latency',
            'security': 'Distributed, randomized validators',
            'complexity': 'Very High (protocol overhaul)',
            'cross_chain': 'Cross-shard protocols (slow, complex)',
            'cost_efficiency': 'High after upgrade, complex operations',
            'ecosystem_adoption': 'Slow, incremental rollout',
            'best_for': 'Long-term ecosystem scaling'
        },
        'Hybrid (Layer 2 + Sharding)': {
            'throughput': 'Exponential scaling potential',
            'performance': 'Optimized for both intra and inter-shard',
            'security': 'Combined security models',
            'complexity': 'Very High',
            'cross_chain': 'Advanced protocols needed',
            'cost_efficiency': 'Optimal',
            'ecosystem_adoption': 'Emerging (Solana, Shardeum)',
            'best_for': 'Web3 global infrastructure'
        }
    }
    
    # Security Attack Vectors
    SECURITY_VECTORS = {
        'layer1': {
            '51% Attack': {'likelihood': 'Very Low', 'impact': 'Critical'},
            'Double Spend': {'likelihood': 'Very Low', 'impact': 'High'},
            'Network Congestion': {'likelihood': 'High', 'impact': 'Medium'}
        },
        'layer2_optimistic': {
            'Sequencer Centralization': {'likelihood': 'Medium', 'impact': 'Medium'},
            'Fraud Proof Failure': {'likelihood': 'Low', 'impact': 'High'},
            'Bridge Exploits': {'likelihood': 'Medium', 'impact': 'Critical'},
            'Smart Contract Bugs': {'likelihood': 'Medium', 'impact': 'High'}
        },
        'layer2_zk': {
            'Proof Generation Attack': {'likelihood': 'Very Low', 'impact': 'Critical'},
            'Trusted Setup Compromise': {'likelihood': 'Very Low', 'impact': 'Critical'},
            'Bridge Exploits': {'likelihood': 'Medium', 'impact': 'Critical'},
            'Complexity Bugs': {'likelihood': 'Medium', 'impact': 'High'}
        },
        'sharding': {
            'Single Shard Takeover': {'likelihood': 'Low', 'impact': 'High'},
            'Sybil Attack': {'likelihood': 'Low', 'impact': 'Critical'},
            'Cross-Shard Replay': {'likelihood': 'Low', 'impact': 'High'},
            'Network Partitioning': {'likelihood': 'Low', 'impact': 'Critical'},
            'Validator Coordination Failure': {'likelihood': 'Medium', 'impact': 'Medium'}
        }
    }
    
    @classmethod
    def get_all_solutions(cls):
        """Return all Layer 2 and sharding solutions"""
        return {
            'layer2': cls.LAYER2_SOLUTIONS,
            'sharding': cls.SHARDING_SOLUTIONS,
            'base': cls.BASE_LAYER
        }
    
    @classmethod
    def get_trilemma_data(cls):
        """Return trilemma data for all solutions"""
        return cls.TRILEMMA
    
    @classmethod
    def get_comparison_summary(cls):
        """Return comparison table data"""
        return cls.COMPARISON_TABLE
