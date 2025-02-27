"""
Example demonstrating basic usage of the MYCELIUM system.
"""

import time
from datetime import datetime, timedelta
import json
import sys
import os

# Add the parent directory to the path so we can import MYCELIUM
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from translators import WaterStressTranslator, BiodiversityTranslator
from community import CommunityInterface
from community.cultural_enhancements import CulturalEnhancementsIntegrator

def main():
    """Run a basic demonstration of MYCELIUM functionality"""
    print("Starting MYCELIUM demonstration...")
    
    # Create translators for different ecological domains
    water_translator = WaterStressTranslator()
    biodiversity_translator = BiodiversityTranslator()
    
    # Test water stress translation
    water_data = {
        "soil_moisture": 18,
        "ecosystem_type": "temperate_forest",
        "additional_indicators": {
            "leaf_water_potential": -1.8,
            "stream_flow": 0.3,
            "precipitation_deficit": 25
        }
    }
    
    water_feedback = water_translator.translate(water_data)
    print("\nWATER STRESS FEEDBACK:")
    print(json.dumps(water_feedback, indent=2))
    
    # Test biodiversity translation
    biodiversity_data = {
        "ecosystem_type": "temperate_forest",
        "species_count": 28,
        "bird_species": 18,
        "insect_orders": 8,
        "shannon_index": 2.8,
        "acoustic_diversity": 0.65
    }
    
    biodiversity_feedback = biodiversity_translator.translate(biodiversity_data)
    print("\nBIODIVERSITY FEEDBACK:")
    print(json.dumps(biodiversity_feedback, indent=2))
    
   # Create a community
    print("\nCreating community interface...")
    community = CommunityInterface("coastal_creek_123", "admin_user")
    
    # Add translators to the community
    community.translators = {
        "water_stress": water_translator,
        "biodiversity": biodiversity_translator
    }
    
    # Enhance with cultural inclusivity features
    community = CulturalEnhancementsIntegrator.integrate(community)
    
    # Register users
    print("Registering community members...")
    community.register_user("user1", {
        "name": "Alex",
        "sentinel_species": "Coast Live Oak",
        "focus_areas": ["water", "biodiversity"],
        "enhanced_profile": {
            "cultural_background": "Mixed Indigenous/European",
            "languages": ["English", "Spanish"],
            "age": 42,
            "relationship_to_place": "Third generation resident"
        }
    })
    
    community.register_user("user2", {
        "name": "Jordan",
        "sentinel_species": "California Newt",
        "focus_areas": ["biodiversity"],
        "enhanced_profile": {
            "cultural_background": "East Asian",
            "languages": ["English", "Mandarin"],
            "age": 28,
            "relationship_to_place": "New resident"
        }
    })
    
    community.register_user("user3", {
        "name": "Taylor",
        "sentinel_species": "Red-tailed Hawk",
        "focus_areas": ["wildlife", "air"],
        "enhanced_profile": {
            "cultural_background": "African American",
            "languages": ["English"],
            "age": 35,
            "relationship_to_place": "Environmental educator"
        }
    })
    
    # Track diversity
    diversity = community.track_diversity_metrics()
    print("\nCOMMUNITY DIVERSITY METRICS:")
    print(json.dumps(diversity, indent=2))
    
    # Customize bioregional bonding ceremony
    ceremony_plan = community.customize_bonding_ceremony({
        "title": "Watershed Connection Ceremony",
        "rituals": ["soil_collection", "water_blessing", "sentinel_identification"],
        "languages": ["English", "Spanish", "Ohlone"],
        "indigenous_acknowledgment": "We acknowledge this land as the traditional territory of the Ohlone people...",
        "cultural_elements": [
            "Traditional songs from community members",
            "Local plant identification with Indigenous names"
        ],
        "preferred_locations": [
            {
                "name": "Ancient Oak Grove",
                "type": "ancestor_honoring",
                "coordinates": [37.8651, -122.2536],
                "description": "Grove of 200-year-old oaks with cultural significance"
            },
            {
                "name": "Headwaters Spring",
                "type": "water_blessing",
                "coordinates": [37.8701, -122.2456],
                "description": "Source of the main creek"
            }
        ]
    })
    
    print("\nCUSTOMIZED CEREMONY PLAN:")
    print(json.dumps(ceremony_plan, indent=2))
    
    # Start a collective pulse session
    print("\nInitiating collective pulse...")
    pulse = community.initiate_collective_pulse("user1", {
        "ecological_domain": "water_stress",
        "focus_area": "creek_headwaters",
        "scheduled_time": (datetime.now() + timedelta(hours=1)).isoformat()
    })
    
    # Users join the pulse
    community.join_collective_pulse("user2", pulse["session_id"])
    community.join_collective_pulse("user3", pulse["session_id"])
    
    # Deliver the pulse (in a real implementation, this would happen at the scheduled time)
    print("Delivering collective pulse...")
    pulse_result = community.deliver_collective_pulse(pulse["session_id"])
    print("\nCOLLECTIVE PULSE FEEDBACK:")
    print(json.dumps(pulse_result["feedback"], indent=2))
    
    # Share reflection after pulse
    reflection = community.share_reflection("user1", {
        "reflection_id": pulse_result["reflection_circle"],
        "content": "I felt the tension of water stress in my throat - made me realize how precious our summer creek flow is.",
        "emotion": "concern",
        "insights": ["Need to conserve more water at home", "Creek health seems connected to my own wellbeing"],
        "action_ideas": ["Organize watershed-wide water conservation campaign"]
    })
    
    print("\nREFLECTION SHARED:")
    print(json.dumps(reflection, indent=2))
    
    # Set personal stewardship goal
    goal = community.set_stewardship_goal("user2", {
        "title": "Reduce Watershed Impact",
        "description": "Install rainwater catchment at home to reduce runoff",
        "domain": "water_stress",
        "target_date": (datetime.now() + timedelta(days=30)).isoformat(),
        "is_public": True,
        "milestones": [
            "Research systems - 20%",
            "Purchase equipment - 50%",
            "Installation - 80%",
            "First water harvested - 100%"
        ]
    })
    
    print("\nSTEWARDSHIP GOAL SET:")
    print(json.dumps(goal, indent=2))
    
    # Share observation
    observation = community.share_observation("user2", {
        "type": "species_sighting",
        "species": "California Newt",
        "location": "tributary_pool",
        "description": "Three newts observed at the north tributary pool - more than usual for this time of year.",
        "feedback_felt": "harmony"
    })
    
    print("\nOBSERVATION SHARED:")
    print(json.dumps(observation, indent=2))
    
    # Propose community action
    action = community.propose_community_action("user1", {
        "title": "Creek Cleanup Day",
        "description": "Let's remove invasive plants and trash from the creek banks.",
        "location": "main_tributary",
        "domain": "water_stress",
        "date": (datetime.now() + timedelta(days=10)).isoformat()
    })
    
    print("\nCOMMUNITY ACTION PROPOSED:")
    print(json.dumps(action, indent=2))
    
    # Join the action
    join = community.join_community_action("user2", action["action_id"])
    print("\nUSER JOINED ACTION:")
    print(json.dumps(join, indent=2))
    
    # Get community summary
    summary = community.get_community_summary()
    print("\nCOMMUNITY SUMMARY:")
    print(json.dumps(summary, indent=2))
    
    print("\nMYCELIUM demonstration complete!")

if __name__ == "__main__":
    main()
