from typing import List, Dict, Any
from datetime import datetime, timedelta


def get_dummy_campaigns() -> List[Dict[str, Any]]:
    """
    Returns a list of dummy campaign objects for AI processing.
    Each campaign has the structure needed for awareness, trust scoring, and engagement prediction.
    """
    return [
        {
            "id": "camp_001",
            "name": "Clean Village Initiative",
            "organization": "Rural Development Trust",
            "category": "environment",
            "description": "Community-led waste management and sanitation drive across 50 villages",
            "target_audience": "Rural households, local panchayats",
            "target_participants": 10000,
            "current_participants": 4200,
            "start_date": "2025-01-01",
            "end_date": "2025-06-30",
            "status": "active",
            "reward_tokens_per_action": 5,
        },
        {
            "id": "camp_002",
            "name": "Digital Literacy for Senior Citizens",
            "organization": "National Education Council",
            "category": "education",
            "description": "Free smartphone and basic internet usage training for citizens above 60",
            "target_audience": "Senior citizens, caregivers",
            "target_participants": 5000,
            "current_participants": 3850,
            "start_date": "2024-11-15",
            "end_date": "2025-03-15",
            "status": "active",
            "reward_tokens_per_action": 10,
        },
        {
            "id": "camp_003",
            "name": "Blood Donation Awareness Month",
            "organization": "Health Ministry",
            "category": "health",
            "description": "Drive to encourage voluntary blood donation and register new donors",
            "target_audience": "Eligible adults 18-60 years",
            "target_participants": 25000,
            "current_participants": 9200,
            "start_date": "2025-01-15",
            "end_date": "2025-02-15",
            "status": "active",
            "reward_tokens_per_action": 20,
        },
        {
            "id": "camp_004",
            "name": "Skill Up - Women in Tech",
            "organization": "CSR Foundation",
            "category": "employment",
            "description": "Free coding bootcamp and placement support for women from underserved communities",
            "target_audience": "Women 18-35, no prior tech experience required",
            "target_participants": 500,
            "current_participants": 312,
            "start_date": "2024-12-01",
            "end_date": "2025-05-01",
            "status": "active",
            "reward_tokens_per_action": 50,
        },
        {
            "id": "camp_005",
            "name": "Tree Plantation Drive 2025",
            "organization": "Green Earth NGO",
            "category": "environment",
            "description": "Plant 1 lakh saplings across urban parks and school campuses",
            "target_audience": "Schools, colleges, resident welfare associations",
            "target_participants": 15000,
            "current_participants": 2500,
            "start_date": "2025-01-10",
            "end_date": "2025-07-10",
            "status": "active",
            "reward_tokens_per_action": 3,
        },
    ]


def get_participation_history(campaign_id: str) -> List[Dict[str, Any]]:
    """
    Returns dummy weekly participation history for a campaign.
    Used for engagement prediction based on trend.
    """
    histories = {
        "camp_001": [
            {"week": 1, "participants": 400},
            {"week": 2, "participants": 580},
            {"week": 3, "participants": 720},
            {"week": 4, "participants": 650},
            {"week": 5, "participants": 850},
            {"week": 6, "participants": 1000},
        ],
        "camp_002": [
            {"week": 1, "participants": 500},
            {"week": 2, "participants": 620},
            {"week": 3, "participants": 550},
            {"week": 4, "participants": 680},
            {"week": 5, "participants": 750},
            {"week": 6, "participants": 750},
        ],
        "camp_003": [
            {"week": 1, "participants": 2500},
            {"week": 2, "participants": 2200},
            {"week": 3, "participants": 2300},
            {"week": 4, "participants": 2100},
        ],
        "camp_004": [
            {"week": 1, "participants": 80},
            {"week": 2, "participants": 55},
            {"week": 3, "participants": 62},
            {"week": 4, "participants": 45},
            {"week": 5, "participants": 70},
        ],
        "camp_005": [
            {"week": 1, "participants": 300},
            {"week": 2, "participants": 450},
            {"week": 3, "participants": 550},
            {"week": 4, "participants": 600},
            {"week": 5, "participants": 600},
        ],
    }
    return histories.get(campaign_id, [])
