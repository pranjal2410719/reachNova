from dummy_data import get_dummy_campaigns, get_participation_history
from ai_engine import (
    campaign_to_summary,
    compute_impact_trust_score,
    predict_engagement,
    analyze_campaign,
)


def print_separator(title: str = ""):
    """Prints a clean separator line."""
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)
    print()


def main():
    """Runs all AI features on dummy campaigns and prints results."""
    campaigns = get_dummy_campaigns()
    
    print_separator("ReachNova AI Module - Demo")
    print("Running Campaign Understanding, Impact & Trust Scoring, and Engagement Prediction")
    print("Using dummy data - no external APIs")
    
    print_separator("1) Campaign Understanding AI")
    
    for campaign in campaigns[:2]:  # Show first 2
        summary = campaign_to_summary(campaign)
        print(f"Campaign: {campaign['name']}")
        print(summary)
        print()
    
    print_separator("2) Impact & Trust Scoring AI")
    
    for campaign in campaigns:
        score, explanation = compute_impact_trust_score(campaign)
        print(f"{campaign['name']}: {score}/100")
        print(f"  -> {explanation}")
        print()
    
    print_separator("3) Engagement Prediction AI")
    
    for campaign in campaigns[:3]:
        history = get_participation_history(campaign["id"])
        pred_rate, pred_explanation = predict_engagement(campaign, history, weeks_ahead=2)
        print(f"{campaign['name']}: Predicted participation {pred_rate:.1f}% (in 2 weeks)")
        print(f"  -> {pred_explanation}")
        print()
    
    print_separator("Full AI Analysis (Sample: Clean Village Initiative)")
    
    sample = campaigns[0]
    result = analyze_campaign(sample)
    
    print(f"Campaign: {result['campaign_name']}")
    print(f"Impact & Trust Score: {result['impact_trust_score']}/100")
    print(f"Predicted Participation Rate: {result['predicted_participation_rate']}%")
    print()
    print("Summary:")
    print(result["summary"])
    print()
    print("Score explanation:", result["score_explanation"])
    print("Prediction explanation:", result["prediction_explanation"])
    
    print_separator("Demo Complete")


if __name__ == "__main__":
    main()
