/**
 * Chart Initialization & Updates
 * Using Chart.js for visualizations
 */

// Chart.js default configuration
Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.font.size = 14;
Chart.defaults.color = '#6b7280';

// Color scheme from config
const COLORS = {
    layer1: '#3b82f6',
    layer2: '#8b5cf6',
    sharding: '#10b981',
    hybrid: '#f59e0b',
    comparison: '#ef4444',
    gradient: {
        layer1: 'rgba(59, 130, 246, 0.2)',
        layer2: 'rgba(139, 92, 246, 0.2)',
        sharding: 'rgba(16, 185, 129, 0.2)',
        hybrid: 'rgba(245, 158, 11, 0.2)'
    }
};

/**
 * Chart Manager Object
 */
const ChartManager = {
    charts: {},
    
    /**
     * Create TPS comparison bar chart
     */
    createTPSComparisonChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        // Destroy existing chart
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Transactions Per Second (TPS)',
                    data: data.values,
                    backgroundColor: data.colors || [
                        COLORS.layer1,
                        COLORS.layer2,
                        COLORS.layer2,
                        COLORS.sharding,
                        COLORS.hybrid
                    ],
                    borderRadius: 8,
                    borderSkipped: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.parsed.y.toLocaleString()} TPS`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return Utils.formatNumber(value, 0);
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create cost comparison line chart
     */
    createCostComparisonChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Layer 1 Cost',
                    data: data.layer1,
                    borderColor: COLORS.layer1,
                    backgroundColor: COLORS.gradient.layer1,
                    fill: true,
                    tension: 0.4
                }, {
                    label: 'Layer 2 Cost',
                    data: data.layer2,
                    borderColor: COLORS.layer2,
                    backgroundColor: COLORS.gradient.layer2,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.dataset.label}: ${Utils.formatCurrency(context.parsed.y)}`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return Utils.formatCurrency(value);
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create trilemma radar chart
     */
    createTrilemmaRadarChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        const datasets = Object.keys(data).map((key, index) => {
            const colors = [COLORS.layer1, COLORS.layer2, COLORS.sharding, COLORS.hybrid];
            return {
                label: key,
                data: [
                    data[key].scalability,
                    data[key].security,
                    data[key].decentralization
                ],
                borderColor: colors[index % colors.length],
                backgroundColor: COLORS.gradient[Object.keys(COLORS.gradient)[index % 4]],
                pointBackgroundColor: colors[index % colors.length],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors[index % colors.length]
            };
        });
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Scalability', 'Security', 'Decentralization'],
                datasets: datasets
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    }
                },
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 100,
                        ticks: {
                            stepSize: 20
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create horizontal comparison chart
     */
    createHorizontalComparisonChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.metric,
                    data: data.values,
                    backgroundColor: [
                        COLORS.layer1,
                        COLORS.layer2,
                        COLORS.sharding,
                        COLORS.hybrid
                    ],
                    borderRadius: 8
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        }
                    },
                    y: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create stacked area chart for throughput evolution
     */
    createThroughputEvolutionChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [
                    {
                        label: 'Base Layer',
                        data: data.baseLayer,
                        borderColor: COLORS.layer1,
                        backgroundColor: COLORS.gradient.layer1,
                        fill: true,
                        tension: 0.4
                    },
                    {
                        label: 'Layer 2 Addition',
                        data: data.layer2,
                        borderColor: COLORS.layer2,
                        backgroundColor: COLORS.gradient.layer2,
                        fill: true,
                        tension: 0.4
                    },
                    {
                        label: 'Sharding Addition',
                        data: data.sharding,
                        borderColor: COLORS.sharding,
                        backgroundColor: COLORS.gradient.sharding,
                        fill: true,
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false
                    }
                },
                scales: {
                    y: {
                        stacked: true,
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return Utils.formatNumber(value, 0) + ' TPS';
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create doughnut chart for market share
     */
    createMarketShareChart(canvasId, data) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.values,
                    backgroundColor: [
                        COLORS.layer1,
                        COLORS.layer2,
                        COLORS.sharding,
                        COLORS.hybrid
                    ],
                    borderWidth: 2,
                    borderColor: '#fff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${percentage}%`;
                            }
                        }
                    }
                }
            }
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Create gauge chart for performance score
     */
    createGaugeChart(canvasId, value, max = 100) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;
        
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }
        
        const percentage = (value / max) * 100;
        const color = percentage >= 80 ? COLORS.sharding :
                      percentage >= 60 ? COLORS.layer2 :
                      percentage >= 40 ? COLORS.hybrid : COLORS.comparison;
        
        this.charts[canvasId] = new Chart(ctx, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [value, max - value],
                    backgroundColor: [color, '#e5e7eb'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                circumference: 180,
                rotation: 270,
                cutout: '75%',
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    }
                }
            },
            plugins: [{
                id: 'gaugeText',
                afterDraw: (chart) => {
                    const { ctx, chartArea: { width, height } } = chart;
                    ctx.save();
                    ctx.font = 'bold 32px Inter';
                    ctx.fillStyle = color;
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText(`${value}`, width / 2, height / 2 + 20);
                    ctx.font = '14px Inter';
                    ctx.fillStyle = '#6b7280';
                    ctx.fillText('Score', width / 2, height / 2 + 50);
                    ctx.restore();
                }
            }]
        });
        
        return this.charts[canvasId];
    },
    
    /**
     * Update chart data
     */
    updateChart(canvasId, newData) {
        const chart = this.charts[canvasId];
        if (!chart) return;
        
        if (newData.labels) {
            chart.data.labels = newData.labels;
        }
        
        if (newData.datasets) {
            chart.data.datasets = newData.datasets;
        } else if (newData.values) {
            chart.data.datasets[0].data = newData.values;
        }
        
        chart.update('none'); // Update without animation
    },
    
    /**
     * Destroy chart
     */
    destroyChart(canvasId) {
        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
            delete this.charts[canvasId];
        }
    },
    
    /**
     * Destroy all charts
     */
    destroyAll() {
        Object.keys(this.charts).forEach(canvasId => {
            this.destroyChart(canvasId);
        });
    }
};

// Export
window.ChartManager = ChartManager;
window.CHART_COLORS = COLORS;
