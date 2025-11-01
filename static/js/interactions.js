/**
 * User Input Handlers and Interactions
 */

/**
 * Slider handler with real-time updates
 */
class SliderHandler {
    constructor(sliderId, displayId, callback) {
        this.slider = document.getElementById(sliderId);
        this.display = document.getElementById(displayId);
        this.callback = callback;
        
        if (this.slider) {
            this.init();
        }
    }
    
    init() {
        // Update display on input
        this.slider.addEventListener('input', (e) => {
            const value = parseInt(e.target.value);
            this.updateDisplay(value);
        });
        
        // Trigger callback on change
        this.slider.addEventListener('change', (e) => {
            const value = parseInt(e.target.value);
            if (this.callback) {
                this.callback(value);
            }
        });
        
        // Initial display
        this.updateDisplay(parseInt(this.slider.value));
    }
    
    updateDisplay(value) {
        if (this.display) {
            this.display.textContent = Utils.formatNumber(value, 0);
        }
    }
    
    getValue() {
        return parseInt(this.slider.value);
    }
    
    setValue(value) {
        this.slider.value = value;
        this.updateDisplay(value);
    }
}

/**
 * Form handler for calculation inputs
 */
class CalculationForm {
    constructor(formId, onSubmit) {
        this.form = document.getElementById(formId);
        this.onSubmit = onSubmit;
        
        if (this.form) {
            this.init();
        }
    }
    
    init() {
        this.form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(this.form);
            const data = Object.fromEntries(formData.entries());
            
            // Convert numeric fields
            Object.keys(data).forEach(key => {
                if (!isNaN(data[key])) {
                    data[key] = parseFloat(data[key]);
                }
            });
            
            if (this.onSubmit) {
                await this.onSubmit(data);
            }
        });
    }
    
    getData() {
        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData.entries());
        
        Object.keys(data).forEach(key => {
            if (!isNaN(data[key])) {
                data[key] = parseFloat(data[key]);
            }
        });
        
        return data;
    }
    
    setData(data) {
        Object.keys(data).forEach(key => {
            const input = this.form.querySelector(`[name="${key}"]`);
            if (input) {
                input.value = data[key];
            }
        });
    }
    
    reset() {
        this.form.reset();
    }
}

/**
 * Tab navigation handler
 */
class TabHandler {
    constructor(tabContainerId) {
        this.container = document.getElementById(tabContainerId);
        this.tabs = [];
        this.contents = [];
        
        if (this.container) {
            this.init();
        }
    }
    
    init() {
        this.tabs = this.container.querySelectorAll('[data-tab]');
        
        this.tabs.forEach(tab => {
            tab.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = tab.getAttribute('data-tab');
                this.showTab(targetId);
            });
        });
        
        // Show first tab by default
        if (this.tabs.length > 0) {
            const firstTabId = this.tabs[0].getAttribute('data-tab');
            this.showTab(firstTabId);
        }
    }
    
    showTab(tabId) {
        // Hide all content
        document.querySelectorAll('[data-tab-content]').forEach(content => {
            content.style.display = 'none';
        });
        
        // Remove active class from all tabs
        this.tabs.forEach(tab => {
            tab.classList.remove('active');
        });
        
        // Show target content
        const targetContent = document.getElementById(tabId);
        if (targetContent) {
            targetContent.style.display = 'block';
        }
        
        // Add active class to clicked tab
        const activeTab = this.container.querySelector(`[data-tab="${tabId}"]`);
        if (activeTab) {
            activeTab.classList.add('active');
        }
    }
}

/**
 * Modal handler
 */
class ModalHandler {
    constructor(modalId) {
        this.modal = document.getElementById(modalId);
        this.closeBtn = null;
        
        if (this.modal) {
            this.init();
        }
    }
    
    init() {
        // Find close button
        this.closeBtn = this.modal.querySelector('.modal-close');
        
        if (this.closeBtn) {
            this.closeBtn.addEventListener('click', () => this.close());
        }
        
        // Close on outside click
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) {
                this.close();
            }
        });
        
        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isOpen()) {
                this.close();
            }
        });
    }
    
    open() {
        this.modal.style.display = 'flex';
        this.modal.classList.add('fade-in');
        document.body.style.overflow = 'hidden';
    }
    
    close() {
        this.modal.style.display = 'none';
        this.modal.classList.remove('fade-in');
        document.body.style.overflow = '';
    }
    
    isOpen() {
        return this.modal.style.display === 'flex';
    }
}

/**
 * Comparison calculator with debounced updates
 */
class ComparisonCalculator {
    constructor(options = {}) {
        this.txVolumeSlider = null;
        this.shardsSlider = null;
        this.resultContainer = null;
        this.updateDelay = options.updateDelay || 500;
        
        this.init();
    }
    
    init() {
        // Initialize sliders
        this.txVolumeSlider = new SliderHandler(
            'txVolumeSlider',
            'txVolumeDisplay',
            Utils.debounce(() => this.calculate(), this.updateDelay)
        );
        
        this.shardsSlider = new SliderHandler(
            'shardsSlider',
            'shardsDisplay',
            Utils.debounce(() => this.calculate(), this.updateDelay)
        );
        
        this.resultContainer = document.getElementById('calculationResults');
        
        // Initial calculation
        this.calculate();
    }
    
    async calculate() {
        if (!this.resultContainer) return;
        
        const txVolume = this.txVolumeSlider ? this.txVolumeSlider.getValue() : 1000000;
        const numShards = this.shardsSlider ? this.shardsSlider.getValue() : 64;
        
        showLoading(this.resultContainer);
        
        try {
            // Calculate all solutions
            const layer2Data = await API.calculateLayer2(txVolume);
            const shardingData = await API.calculateSharding(txVolume, numShards);
            const hybridData = await API.calculateHybrid(txVolume);
            
            this.displayResults({
                layer2: layer2Data,
                sharding: shardingData,
                hybrid: hybridData
            });
            
        } catch (error) {
            console.error('Calculation error:', error);
            showNotification('Error calculating results', 'error');
        } finally {
            hideLoading();
        }
    }
    
    displayResults(data) {
        if (!this.resultContainer) return;
        
        // Create results HTML
        const html = `
            <div class="grid grid-3">
                <div class="stat-card">
                    <div class="stat-label">Layer 2 (Optimistic)</div>
                    <div class="stat-value">${Utils.formatNumber(data.layer2.optimistic.tps, 0)}</div>
                    <div class="stat-label">TPS</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Sharding</div>
                    <div class="stat-value">${Utils.formatNumber(data.sharding.total_tps, 0)}</div>
                    <div class="stat-label">TPS</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Hybrid Model</div>
                    <div class="stat-value">${Utils.formatNumber(data.hybrid.total_hybrid_tps, 0)}</div>
                    <div class="stat-label">TPS</div>
                </div>
            </div>
        `;
        
        this.resultContainer.innerHTML = html;
    }
}

/**
 * Live performance monitor
 */
class PerformanceMonitor {
    constructor(containerId, updateInterval = 2000) {
        this.container = document.getElementById(containerId);
        this.updateInterval = updateInterval;
        this.intervalId = null;
        
        if (this.container) {
            this.start();
        }
    }
    
    start() {
        this.update();
        this.intervalId = setInterval(() => this.update(), this.updateInterval);
    }
    
    stop() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }
    
    async update() {
        try {
            // Simulate live data (in production, fetch from real API)
            const data = {
                layer1_tps: 15 + Math.random() * 5,
                layer2_tps: 2500 + Math.random() * 1500,
                sharding_tps: 6000 + Math.random() * 1000
            };
            
            this.render(data);
        } catch (error) {
            console.error('Monitor update error:', error);
        }
    }
    
    render(data) {
        const html = `
            <div class="performance-metrics">
                <div class="metric">
                    <span class="metric-label">Layer 1:</span>
                    <span class="metric-value">${data.layer1_tps.toFixed(1)} TPS</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Layer 2:</span>
                    <span class="metric-value">${data.layer2_tps.toFixed(0)} TPS</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Sharding:</span>
                    <span class="metric-value">${data.sharding_tps.toFixed(0)} TPS</span>
                </div>
            </div>
        `;
        
        this.container.innerHTML = html;
    }
}

// Export classes
window.SliderHandler = SliderHandler;
window.CalculationForm = CalculationForm;
window.TabHandler = TabHandler;
window.ModalHandler = ModalHandler;
window.ComparisonCalculator = ComparisonCalculator;
window.PerformanceMonitor = PerformanceMonitor;
