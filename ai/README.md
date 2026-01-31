# ReachNova AI Module

**Lightweight, explainable AI for awareness and trust.**  
Built for the Hyperspace Innovation Hackathon.

---

## Overview

This module powers ReachNova's awareness and engagement features with **simple, rule-based AI**—no heavy ML models, no LLMs, no external APIs. Everything is transparent and easy to explain to judges and stakeholders.

### Three AI Features

| Feature | Purpose |
|--------|---------|
| **Campaign Understanding AI** | Converts campaign data into human-readable summaries for awareness cards and social sharing |
| **Impact & Trust Scoring AI** | Generates a 0–100 score based on participation, target achievement, and duration |
| **Engagement Prediction** | Predicts future participation percentage using trend-based logic |

---

## Quick Start

### Run the Demo

```bash
cd ai
python run_ai.py
```

This runs all three AI features on dummy campaign data and prints the results.

### Use in Code

```python
from dummy_data import get_dummy_campaigns, get_participation_history
from ai_engine import campaign_to_summary, compute_impact_trust_score, predict_engagement, analyze_campaign

# Get dummy campaigns
campaigns = get_dummy_campaigns()

# 1) Human-readable summary
summary = campaign_to_summary(campaigns[0])
print(summary)

# 2) Impact & Trust score (0-100)
score, explanation = compute_impact_trust_score(campaigns[0])
print(f"Score: {score}/100 - {explanation}")

# 3) Engagement prediction
history = get_participation_history(campaigns[0]["id"])
pred_rate, pred_explanation = predict_engagement(campaigns[0], history, weeks_ahead=2)
print(f"Predicted participation: {pred_rate}%")

# Or run full analysis at once
result = analyze_campaign(campaigns[0])
```

---

## Files

| File | Description |
|------|-------------|
| `dummy_data.py` | Sample campaign data and participation history for testing |
| `ai_engine.py` | All three AI functions (Campaign Understanding, Impact & Trust, Engagement Prediction) |
| `run_ai.py` | Demo script to run the AI on dummy data |
| `README.md` | This file |

---

## How the AI Works (Explainable Logic)

### 1. Campaign Understanding AI

- Maps campaign fields into a structured template (category, audience, progress, rewards)
- Uses participation rate to choose a progress label (e.g. "Building momentum", "Nearly complete")
- Output is plain text suitable for awareness cards and social media

### 2. Impact & Trust Scoring AI

- **Participation achievement (0–50 pts):** Higher score when more of the target is reached
- **Time utilization (0–25 pts):** Compares current progress to expected progress based on elapsed time
- **Trust signals (0–25 pts):** Based on reward tier and organization type (e.g. government/ministry)

### 3. Engagement Prediction

- Uses weekly participation history
- Weights recent weeks more (momentum)
- Computes trend (growing vs declining vs flat)
- Projects participation rate N weeks ahead

---

## Technical Notes

- **Python 3.7+** (standard library only, no external packages)
- **No ML models, chatbots, or LLM agents**
- **No external APIs** — all data is from `dummy_data.py`

---

## Hackathon Pitch Points

- **Explainable:** Every score and prediction has a clear, rule-based rationale  
- **Lightweight:** Fast, no cloud APIs, easy to run offline  
- **Trust-focused:** Designed to build awareness and trust in social campaigns  
- **Integration-ready:** Simple functions that can plug into the main ReachNova app  
