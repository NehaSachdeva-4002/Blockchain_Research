"""
Helper utility functions for the application
"""

def format_number(num, precision=2):
    """
    Format number with K, M, B suffixes
    
    Args:
        num: Number to format
        precision: Decimal places
        
    Returns:
        str: Formatted number
    """
    if num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.{precision}f}B"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.{precision}f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.{precision}f}K"
    else:
        return f"{num:.{precision}f}"

def format_currency(amount, currency='USD'):
    """
    Format currency values
    
    Args:
        amount: Amount to format
        currency: Currency symbol
        
    Returns:
        str: Formatted currency
    """
    if currency == 'USD':
        if amount < 0.01:
            return f"${amount:.4f}"
        return f"${amount:.2f}"
    elif currency == 'GWEI':
        return f"{amount:,.2f} Gwei"
    return f"{amount:.2f}"

def calculate_percentage(part, whole):
    """
    Calculate percentage
    
    Args:
        part: Part value
        whole: Whole value
        
    Returns:
        float: Percentage
    """
    if whole == 0:
        return 0
    return (part / whole) * 100

def get_performance_color(value, metric_type='tps'):
    """
    Get color based on performance metric
    
    Args:
        value: Metric value
        metric_type: Type of metric
        
    Returns:
        str: Color code
    """
    colors = {
        'excellent': '#10b981',  # Green
        'good': '#8b5cf6',       # Purple
        'average': '#f59e0b',    # Orange
        'poor': '#ef4444'        # Red
    }
    
    if metric_type == 'tps':
        if value >= 10000:
            return colors['excellent']
        elif value >= 1000:
            return colors['good']
        elif value >= 100:
            return colors['average']
        else:
            return colors['poor']
    
    return colors['good']

def calculate_improvement(old_value, new_value):
    """
    Calculate improvement percentage
    
    Args:
        old_value: Original value
        new_value: New value
        
    Returns:
        dict: Improvement metrics
    """
    if old_value == 0:
        return {'percentage': 0, 'multiplier': 0}
    
    improvement = ((new_value - old_value) / old_value) * 100
    multiplier = new_value / old_value
    
    return {
        'percentage': round(improvement, 2),
        'multiplier': round(multiplier, 2)
    }
