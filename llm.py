def generate_feedback(idea, scores):
    f, i, m, r = scores

    # Innovation comment
    if i > 7:
        innovation_text = "strong innovation"
    elif i > 5:
        innovation_text = "moderate innovation"
    else:
        innovation_text = "limited innovation"

    # Market comment
    if m > 7:
        market_text = "high market potential"
    elif m > 5:
        market_text = "decent market potential"
    else:
        market_text = "limited market reach"

    # Risk comment
    if r > 7:
        risk_text = "high risk"
    elif r > 5:
        risk_text = "moderate risk"
    else:
        risk_text = "low risk"

    return f"""
    This idea demonstrates {innovation_text} with a score of {i:.1f}/10.
    
    It has {market_text} ({m:.1f}/10), indicating its potential audience size.
    
    Feasibility is rated at {f:.1f}/10, suggesting its practicality level.
    
    The overall risk is {risk_text} ({r:.1f}/10).
    
    Consider refining differentiation, execution strategy, and target market clarity.
    """