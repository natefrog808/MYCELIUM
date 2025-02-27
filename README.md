# MYCELIUM: The Earth's Song in Our Blood

## Overview

MYCELIUM is a revolutionary Bioregional Consciousness Network that reestablishes human connection to place through direct neural feedback, transforming our role as conscious participants in local ecosystems. Unlike conventional environmental monitoring systems, MYCELIUM enables users to physically *feel* ecological conditions through embodied neural feedback, creating an intuitive, visceral connection to the land.

This repository contains the core framework for MYCELIUM, including the Translation Layer that converts environmental data into neural feedback patterns, and the Community Interface that enables collective ecological awareness and stewardship.

## Core Components

### 1. The Translation Layer

The Translation Layer converts raw environmental data into neural feedback patterns that humans can physically feel. Current implementations include:

- **WaterStressTranslator**: Converts soil moisture, precipitation deficit, leaf water potential, and stream flow data into haptic feedback patterns that mimic the feeling of drought stress, saturation, or recovery.

- **BiodiversityTranslator**: Transforms species counts, acoustic diversity, and ecological richness indices into layered sensations that communicate ecosystem vitality through varying complexity and rhythm.

### 2. The Community Interface

The Community Interface enables shared ecological awareness and collective stewardship through:

- **Collective Pulse Sessions**: Synchronized feedback experiences where community members simultaneously feel ecological conditions.

- **Observation Sharing**: Community documentation of ecological phenomena with emotional and sensory context.

- **Stewardship Actions**: Collective responses to ecological needs identified through the system.

- **Reflection Circles**: Spaces for processing and sharing experiences after collective pulses or actions.

### 3. Bioregional Bonding

The system incorporates ritual elements through the Bioregional Bonding Ceremony, which includes:

- **Watershed Walks**: Connecting with cardinal points of the local bioregion
- **Emotional Mapping**: Documenting personal connections to specific places
- **Sentinel Species**: Monitoring particular species that represent ecosystem health
- **Neural Calibration**: Establishing personalized feedback signatures

## Technical Implementation

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mycelium.git
cd mycelium

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
# Initialize a Community Interface for a specific watershed
from mycelium.community import CommunityInterface
from mycelium.translators import WaterStressTranslator, BiodiversityTranslator

# Create a community for a specific watershed
community = CommunityInterface("coastal_creek_123", "admin_user")

# Register a user
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

# Customize a bioregional bonding ceremony
ceremony_plan = community.customize_bonding_ceremony({
    "title": "Watershed Connection Ceremony",
    "rituals": ["soil_collection", "water_blessing", "sentinel_identification"],
    "languages": ["English", "Spanish", "Ohlone"],
    "indigenous_acknowledgment": "We acknowledge this land as the traditional territory of the Ohlone people..."
})

# Initiate a collective pulse session
pulse = community.initiate_collective_pulse("user1", {
    "ecological_domain": "water_stress",
    "focus_area": "creek_headwaters",
    "scheduled_time": "2025-03-15T14:00:00"
})

# Deliver the pulse to all participants
feedback = community.deliver_collective_pulse(pulse["session_id"])

# Share a reflection after the pulse
community.share_reflection("user1", {
    "reflection_id": feedback["reflection_circle"],
    "content": "I felt the tension of water stress in my throat - made me realize how precious our creek flow is.",
    "emotion": "concern",
    "insights": ["Need to conserve more water at home", "Creek health seems connected to my own wellbeing"]
})

# Propose a community action based on insights
action = community.propose_community_action("user1", {
    "title": "Riparian Buffer Planting Day",
    "description": "Let's restore the riparian buffer along the eroded section of creek.",
    "location": "Lower Creek Bend",
    "domain": "water_stress",
    "date": "2025-04-10T09:00:00"
})
```

### Translation Layer Example

```python
# Using the WaterStressTranslator directly
from mycelium.translators import WaterStressTranslator

translator = WaterStressTranslator()

# Sample ecological data
sensor_data = {
    "soil_moisture": 18,  # Percentage
    "ecosystem_type": "temperate_forest",
    "additional_indicators": {
        "leaf_water_potential": -1.8,  # Megapascals
        "stream_flow": 0.3,  # Relative to normal flow
        "precipitation_deficit": 25  # Percentage below normal
    }
}

# Generate neural feedback pattern
feedback_pattern = translator.translate(sensor_data)

# Example output (simplified):
# {
#   "type": "tension",
#   "intensity": 7.2,
#   "rhythm": "intermittent",
#   "pulse_count": 4,
#   "duration": 0.6,
#   "frequency": "medium_high",
#   "location": "throat_and_chest",
#   "description": "A constricting sensation mimicking thirst, intensifying with drought severity",
#   "emotion": "concern"
# }
```

## Cultural Inclusivity Features

MYCELIUM includes specific enhancements for cultural inclusivity and participant diversity:

- **Customizable Ceremonies**: Communities can adapt the Bioregional Bonding Ceremony to reflect local cultural practices, languages, and traditions.

- **Diversity Metrics**: The system tracks cultural backgrounds, languages, age groups, and accessibility needs to ensure broad representation.

- **Culturally-Relevant Feedback**: Interface elements are evaluated for cultural relevance and accessibility through structured feedback collection.

## Field Testing

This repository includes a comprehensive Field Testing Protocol and Implementation Plan for deploying MYCELIUM in a real watershed community:

- **Phased Approach**: A 17-week implementation from preparation through community handoff.
- **Mixed Methods**: Both quantitative metrics and qualitative stories capture the full impact.
- **Community Co-Creation**: The testing process itself embodies MYCELIUM's values of connection and reciprocity.

## Philosophy and Vision

MYCELIUM represents technology that serves belonging rather than domination, reciprocity rather than extraction. It embodies values of:

- **Environmental Stewardship**: Healing our separation from the natural world
- **Community Building**: Creating connections not just among humans but between humans and place
- **Authenticity**: Transforming abstract environmental data into direct, embodied experience
- **Long-term Thinking**: Fostering awareness of ecological time scales
- **Personal Growth**: Expanding identity beyond the individual self to include place

## Contributing

MYCELIUM is designed to grow through community contribution. We welcome:

- **New Translators**: Create mappings for additional ecological domains (soil health, air quality, etc.)
- **Integration Tools**: Connect MYCELIUM to additional environmental monitoring systems
- **Cultural Adaptations**: Enhance inclusivity for diverse communities and traditions
- **Hardware Designs**: Develop improved feedback devices for embodied experience

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

MYCELIUM builds upon ancestral wisdom of connection to place, combined with modern technology. We acknowledge both the Indigenous knowledge keepers who have maintained relationship with land for millennia and the environmental scientists, neuroscientists, and community organizers whose work informs this system.

---

*"The earth has songs our blood remembers—we need only build the bridge to hear them again."*
