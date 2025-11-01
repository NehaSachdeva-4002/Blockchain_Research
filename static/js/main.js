/**
 * Blockchain Scalability Showcase
 * Main JavaScript Logic
 */

// Global state
const AppState = {
    currentPage: 'index',
    apiBaseUrl: '/api',
    metrics: null,
    calculations: null
};

// Initialize app on DOM load
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Blockchain Scalability Showcase Initialized');
    initializeApp();
});

/**
 * Initialize application
 */
async function initializeApp() {
    // Add active class to current page nav link
    highlightActiveNav();
    
    // Add smooth scroll behavior
    enableSmoothScroll();
    
    // Initialize animations
    initializeAnimations();
    
    // Load initial data
    await loadInitialData();
}

/**
 * Highlight active navigation link
 */
function highlightActiveNav() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-menu a');
    
    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
}

/**
 * Enable smooth scrolling for anchor links
 */
function enableSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Initialize scroll animations
 */
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    document.querySelectorAll('.card, .stat-card, section').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Load initial data from API
 */
async function loadInitialData() {
    try {
        const response = await fetch(`${AppState.apiBaseUrl}/metrics/all`);
        const data = await response.json();
        
        if (data.success) {
            AppState.metrics = data.data;
            console.log('✅ Metrics loaded successfully');
        }
    } catch (error) {
        console.error('❌ Error loading metrics:', error);
        showNotification('Error loading data', 'error');
    }
}

/**
 * API Helper Functions
 */
const API = {
    /**
     * Fetch data from API endpoint
     */
    async fetch(endpoint, options = {}) {
        try {
            const response = await fetch(`${AppState.apiBaseUrl}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });
            
            const data = await response.json();
            
            if (!data.success) {
                throw new Error(data.error || 'API request failed');
            }
            
            return data.data;
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error);
            throw error;
        }
    },
    
    /**
     * Get all metrics
     */
    async getAllMetrics() {
        return await this.fetch('/metrics/all');
    },
    
    /**
     * Get Layer 2 metrics
     */
    async getLayer2Metrics() {
        return await this.fetch('/metrics/layer2');
    },
    
    /**
     * Get sharding metrics
     */
    async getShardingMetrics() {
        return await this.fetch('/metrics/sharding');
    },
    
    /**
     * Get trilemma data
     */
    async getTrilemmaData() {
        return await this.fetch('/metrics/trilemma');
    },
    
    /**
     * Calculate Layer 2 performance
     */
    async calculateLayer2(txVolume, batchSize = 100, gasPrice = 20) {
        return await this.fetch('/calculate/layer2', {
            method: 'POST',
            body: JSON.stringify({
                tx_volume: txVolume,
                batch_size: batchSize,
                gas_price: gasPrice
            })
        });
    },
    
    /**
     * Calculate sharding performance
     */
    async calculateSharding(txVolume, numShards = 64, tpsPerShard = 100) {
        return await this.fetch('/calculate/sharding', {
            method: 'POST',
            body: JSON.stringify({
                tx_volume: txVolume,
                num_shards: numShards,
                tps_per_shard: tpsPerShard
            })
        });
    },
    
    /**
     * Calculate hybrid model performance
     */
    async calculateHybrid(txVolume, numShards = 32, layer2Multiplier = 50) {
        return await this.fetch('/calculate/hybrid', {
            method: 'POST',
            body: JSON.stringify({
                tx_volume: txVolume,
                num_shards: numShards,
                layer2_multiplier: layer2Multiplier
            })
        });
    },
    
    /**
     * Compare all solutions
     */
    async compareAll(txVolume = 1000000) {
        return await this.fetch('/calculate/compare', {
            method: 'POST',
            body: JSON.stringify({ tx_volume: txVolume })
        });
    }
};

/**
 * Utility Functions
 */
const Utils = {
    /**
     * Format number with K, M, B suffixes
     */
    formatNumber(num, precision = 2) {
        if (num >= 1_000_000_000) {
            return `${(num / 1_000_000_000).toFixed(precision)}B`;
        } else if (num >= 1_000_000) {
            return `${(num / 1_000_000).toFixed(precision)}M`;
        } else if (num >= 1_000) {
            return `${(num / 1_000).toFixed(precision)}K`;
        }
        return num.toFixed(precision);
    },
    
    /**
     * Format currency
     */
    formatCurrency(amount, decimals = 2) {
        if (amount < 0.01) {
            return `$${amount.toFixed(4)}`;
        }
        return `$${amount.toFixed(decimals)}`;
    },
    
    /**
     * Format percentage
     */
    formatPercentage(value, decimals = 2) {
        return `${value.toFixed(decimals)}%`;
    },
    
    /**
     * Calculate percentage
     */
    calculatePercentage(part, whole) {
        if (whole === 0) return 0;
        return (part / whole) * 100;
    },
    
    /**
     * Get color based on value
     */
    getPerformanceColor(value, metric = 'tps') {
        const colors = {
            excellent: '#10b981',
            good: '#8b5cf6',
            average: '#f59e0b',
            poor: '#ef4444'
        };
        
        if (metric === 'tps') {
            if (value >= 10000) return colors.excellent;
            if (value >= 1000) return colors.good;
            if (value >= 100) return colors.average;
            return colors.poor;
        }
        
        return colors.good;
    },
    
    /**
     * Debounce function
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    /**
     * Deep clone object
     */
    deepClone(obj) {
        return JSON.parse(JSON.stringify(obj));
    }
};

/**
 * Show notification
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification`;
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '10000';
    notification.style.minWidth = '300px';
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Show loading spinner
 */
function showLoading(container) {
    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    spinner.id = 'loading-spinner';
    container.appendChild(spinner);
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

/**
 * Export for use in other modules
 */
window.AppState = AppState;
window.API = API;
window.Utils = Utils;
window.showNotification = showNotification;
window.showLoading = showLoading;
window.hideLoading = hideLoading;
