from typing import Dict, Any, List, Tuple
from datetime import datetime



def campaign_to_summary(campaign: Dict[str, Any]) -> str:
    """
    Converts campaign data into a simple, human-readable summary for awareness.
    
    Rule-based: Uses structured template mapping based on category and key fields.
    Output is designed for quick sharing on social media or in-app awareness cards.
    """
    category_labels = {
        "environment": "Environmental",
        "education": "Education",
        "health": "Health",
        "employment": "Employment & Skills",
    }
    category = category_labels.get(campaign.get("category", ""), "Social Impact")
    
    participation_rate = _safe_participation_rate(campaign)
    progress_word = _get_progress_word(participation_rate)
    
    lines = [
        f"**{campaign.get('name', 'Campaign')}**",
        f"An {category} initiative by {campaign.get('organization', 'N/A')}.",
        "",
        campaign.get("description", "No description."),
        "",
        f"**Who can join:** {campaign.get('target_audience', 'General public')}",
        f"**Progress:** {progress_word} - {campaign.get('current_participants', 0):,} of "
        f"{campaign.get('target_participants', 0):,} participants ({participation_rate:.0f}%)",
        f"**Reward:** {campaign.get('reward_tokens_per_action', 0)} tokens per action",
    ]
    
    return "\n".join(lines)


def _get_progress_word(rate: float) -> str:
    """Maps participation rate to a simple progress label."""
    if rate >= 90:
        return "Nearly complete"
    if rate >= 70:
        return "Strong progress"
    if rate >= 50:
        return "Good progress"
    if rate >= 30:
        return "Building momentum"
    if rate >= 10:
        return "Getting started"
    return "Just launched"


def _safe_participation_rate(campaign: Dict[str, Any]) -> float:
    """Safely computes participation rate, avoiding division by zero."""
    target = campaign.get("target_participants") or 1
    current = campaign.get("current_participants") or 0
    return min(100.0, 100.0 * current / target)




def compute_impact_trust_score(campaign: Dict[str, Any]) -> Tuple[int, str]:
    """
    Generates an Impact & Trust score (0-100) based on participation, target, and duration.
    
    Rule-based formula:
    - Participation achievement (0-50 pts): How close to target
    - Momentum factor (0-25 pts): Early vs late in campaign lifecycle
    - Consistency bonus (0-25 pts): Reward steady progress
    
    Returns (score, short explanation).
    """
    participation_rate = _safe_participation_rate(campaign)
    days_elapsed, total_days = _get_campaign_duration_info(campaign)
    participation_score = min(50, participation_rate * 0.5)
    if total_days <= 0:
        time_score = 12
    else:
        expected_rate = (days_elapsed / total_days) * 100 
        if participation_rate >= expected_rate:
            # Ahead of schedule
            time_score = 25
        elif participation_rate >= expected_rate * 0.7:
            time_score = 18
        elif participation_rate >= expected_rate * 0.5:
            time_score = 12
        else:
            time_score = 6
    reward = campaign.get("reward_tokens_per_action", 0)
    if reward >= 20:
        trust_bonus = 10
    elif reward >= 10:
        trust_bonus = 8
    elif reward >= 5:
        trust_bonus = 6
    else:
        trust_bonus = 4
    
    org_name = campaign.get("organization", "")
    org_bonus = 15 if any(x in org_name.lower() for x in ["ministry", "council", "national"]) else 10
    
    trust_score = min(25, trust_bonus + (org_bonus // 2))
    
    total = int(participation_score + time_score + trust_score)
    total = min(100, total)
    
    explanation = (
        f"Score {total}/100: Participation {participation_rate:.0f}%, "
        f"time-utilization {time_score}/25, trust-signals {trust_score}/25."
    )
    
    return total, explanation


def _get_campaign_duration_info(campaign: Dict[str, Any]) -> Tuple[int, int]:
    """Returns (days_elapsed, total_days) for the campaign."""
    fmt = "%Y-%m-%d"
    try:
        start = datetime.strptime(campaign.get("start_date", ""), fmt)
        end = datetime.strptime(campaign.get("end_date", ""), fmt)
        now = datetime.now()
        total = (end - start).days
        elapsed = (now - start).days
        elapsed = max(0, min(elapsed, total))
        return elapsed, total
    except (ValueError, TypeError):
        return 30, 90  # Fallback




def predict_engagement(
    campaign: Dict[str, Any],
    participation_history: List[Dict[str, Any]],
    weeks_ahead: int = 2,
) -> Tuple[float, str]:
    """
    Predicts future participation percentage using simple rule-based logic.
    
    Logic:
    - If history exists: Use weighted average of recent trend vs baseline
    - Recent weeks get higher weight (momentum)
    - Clamp to [0, 100] and adjust for target
    
    Returns (predicted_participation_rate, explanation).
    """
    target = campaign.get("target_participants") or 1
    current = campaign.get("current_participants") or 0
    
    if not participation_history or len(participation_history) < 2:
        growth_factor = 1.0 + (weeks_ahead * 0.05)
        predicted_current = min(target, current * growth_factor)
        rate = 100.0 * predicted_current / target
        return min(100.0, rate), "No history; assumed moderate growth (5%/week)."
    
    totals = [h["participants"] for h in participation_history]
    n = len(totals)
    
    weights = [0.5 + 0.5 * (i / n) for i in range(n)]
    weighted_avg_per_week = sum(t * w for t, w in zip(totals, weights)) / sum(weights)
    
    mid = n // 2
    first_half_avg = sum(totals[:mid]) / mid if mid > 0 else totals[0]
    second_half_avg = sum(totals[mid:]) / (n - mid) if n > mid else totals[-1]
    
    if second_half_avg > first_half_avg:
        trend_factor = 1.05  
    elif second_half_avg < first_half_avg:
        trend_factor = 0.98  
    else:
        trend_factor = 1.0  
    
    predicted_weekly = weighted_avg_per_week * (trend_factor ** weeks_ahead)
    predicted_new = current + predicted_weekly * weeks_ahead
    predicted_total = min(target, predicted_new)
    rate = 100.0 * predicted_total / target
    
    trend_word = "growing" if trend_factor > 1 else ("declining" if trend_factor < 1 else "flat")
    explanation = (
        f"Based on {n} weeks of data ({trend_word} trend), "
        f"predicted {weeks_ahead}-week participation rate: {min(100.0, rate):.1f}%."
    )
    
    return min(100.0, rate), explanation



def analyze_campaign(
    campaign: Dict[str, Any],
    participation_history: List[Dict[str, Any]] | None = None,
) -> Dict[str, Any]:
    """
    Runs all three AI features on a campaign and returns combined results.
    """
    from dummy_data import get_participation_history
    
    history = participation_history or get_participation_history(campaign.get("id", ""))
    
    summary = campaign_to_summary(campaign)
    score, score_explanation = compute_impact_trust_score(campaign)
    pred_rate, pred_explanation = predict_engagement(campaign, history)
    
    return {
        "campaign_id": campaign.get("id"),
        "campaign_name": campaign.get("name"),
        "summary": summary,
        "impact_trust_score": score,
        "score_explanation": score_explanation,
        "predicted_participation_rate": round(pred_rate, 1),
        "prediction_explanation": pred_explanation,
    }
