"""
MYCELIUM Field Testing Implementation Plan.

This module provides a concrete, actionable plan for implementing
the MYCELIUM field test, based on the testing protocol.
"""

from datetime import datetime, timedelta

class ImplementationPlan:
    """
    Detailed planning for MYCELIUM field testing,
    including specific actions, resources, and timelines.
    """
    
    @staticmethod
    def get_partner_criteria():
        """
        Returns criteria for selecting ideal community partners.
        
        Returns:
        - criteria: Dict with partner selection criteria
        """
        return {
            "essential": [
                "Existing community group with connection to watershed",
                "15-20 active members",
                "Regular meeting schedule",
                "Interest in ecological stewardship"
            ],
            "preferred": [
                "Diverse membership (age, background, experience)",
                "History of collaborative projects",
                "Access to key locations in watershed",
                "Some technical capacity"
            ],
            "bonus": [
                "Existing ecological monitoring activities",
                "Connection with indigenous knowledge",
                "Educational mission or component",
                "Experience with community-based research"
            ]
        }
    
    @staticmethod
    def get_hardware_requirements():
        """
        Returns hardware needs for field testing.
        
        Returns:
        - hardware: Dict with equipment specifications
        """
        return {
            "feedback_devices": {
                "count": 20,
                "type": "haptic wearables",
                "features": [
                    "Multiple vibration patterns",
                    "Variable intensity",
                    "Bluetooth connectivity",
                    "8+ hour battery life",
                    "Water resistant"
                ],
                "estimated_cost": "$200 each"
            },
            "environmental_sensors": {
                "soil_moisture": {
                    "count": 15,
                    "locations": "Critical riparian areas, diverse soil types",
                    "estimated_cost": "$150 each"
                },
                "acoustic_monitors": {
                    "count": 8,
                    "locations": "Biodiversity hotspots, quiet reference areas",
                    "estimated_cost": "$200 each"
                },
                "weather_stations": {
                    "count": 4,
                    "locations": "Distributed across watershed elevation gradient",
                    "estimated_cost": "$300 each"
                }
            },
            "data_infrastructure": {
                "local_server": "For data collection and processing",
                "wireless_network": "Where cellular coverage exists",
                "manual_collection": "Where wireless not feasible"
            }
        }
    
    @staticmethod
    def get_personnel_roles():
        """
        Returns staffing needs and responsibilities.
        
        Returns:
        - roles: Dict with team structure
        """
        return {
            "technical_lead": {
                "skills": ["Hardware deployment", "Software development", "Data management"],
                "responsibilities": [
                    "Sensor deployment and maintenance",
                    "Interface customization",
                    "Technical troubleshooting",
                    "Data integrity"
                ],
                "time_commitment": "Half-time during setup, quarter-time ongoing"
            },
            "community_facilitator": {
                "skills": ["Group facilitation", "Community organizing", "Ecological knowledge"],
                "responsibilities": [
                    "Workshop and ceremony facilitation",
                    "Relationship building",
                    "Engagement strategies",
                    "Conflict resolution"
                ],
                "time_commitment": "Half-time throughout"
            },
            "research_coordinator": {
                "skills": ["Research design", "Qualitative methods", "Data analysis"],
                "responsibilities": [
                    "Survey and interview design",
                    "Data collection protocols",
                    "Analysis and reporting",
                    "IRB compliance"
                ],
                "time_commitment": "Quarter-time throughout, half-time during analysis"
            },
            "cultural_consultant": {
                "skills": ["Indigenous knowledge", "Cultural facilitation", "Language skills"],
                "responsibilities": [
                    "Ceremony design guidance",
                    "Cultural appropriateness review",
                    "Traditional knowledge integration"
                ],
                "time_commitment": "As needed, concentrated in Phases 1-2"
            }
        }
    
    @staticmethod
    def get_implementation_checklist():
        """
        Returns a comprehensive checklist for implementation.
        
        Returns:
        - checklist: Dict with implementation tasks
        """
        return {
            "pre_testing": [
                "Identify and contact potential community partners",
                "Conduct initial meetings with community leadership",
                "Finalize partner selection and establish agreement",
                "Order and test hardware components",
                "Customize Community Interface for specific watershed",
                "Map sensor deployment locations with community input",
                "Prepare educational materials and training guides",
                "Set up data collection systems and protocols"
            ],
            "phase1": [
                "Install environmental sensors with community participation",
                "Conduct community workshop on watershed mapping",
                "Register participants in MYCELIUM system",
                "Distribute mobile app and conduct usability testing",
                "Collect baseline ecological and community metrics",
                "Prepare for Bioregional Bonding Ceremony"
            ],
            "phase2": [
                "Hold introductory workshop on MYCELIUM concept",
                "Gather input for ceremony customization",
                "Prepare ceremony materials and locations",
                "Conduct Bioregional Bonding Ceremonies in small groups",
                "Perform initial device calibration during ceremony",
                "Collect post-ceremony reflections and feedback"
            ],
            "phase3": [
                "Support individual exploration of system features",
                "Conduct weekly check-in sessions for troubleshooting",
                "Collect and implement interface improvement suggestions",
                "Assist with observation sharing and goal setting",
                "Monitor engagement metrics and address drop-offs",
                "Prepare for collective experiences"
            ],
            "phase4": [
                "Schedule and facilitate first collective pulse",
                "Guide post-pulse reflection process",
                "Support community-initiated action planning",
                "Document ecological impact of actions",
                "Collect stories and narrative accounts",
                "Prepare for analysis phase"
            ],
            "phase5": [
                "Compile and analyze all quantitative data",
                "Perform qualitative analysis of reflections and interviews",
                "Prepare preliminary findings presentation",
                "Facilitate community feedback session",
                "Develop improvement recommendations",
                "Plan sustainability approach"
            ],
            "phase6": [
                "Organize community celebration event",
                "Finalize documentation and case study",
                "Transfer system ownership to community leaders",
                "Establish ongoing support mechanisms",
                "Share learnings with broader MYCELIUM community"
            ]
        }
    
    @staticmethod
    def generate_sample_timeline(start_date=None):
        """
        Generate a sample timeline based on a start date.
        
        Parameters:
        - start_date: Optional starting date (defaults to today)
        
        Returns:
        - timeline: Dict with key milestones and dates
        """
        if start_date is None:
            start_date = datetime.now()
        
        # Calculate phase start dates
        phase1_start = start_date
        phase2_start = phase1_start + timedelta(weeks=4)
        phase3_start = phase2_start + timedelta(weeks=2)
        phase4_start = phase3_start + timedelta(weeks=4)
        phase5_start = phase4_start + timedelta(weeks=4)
        phase6_start = phase5_start + timedelta(weeks=2)
        conclusion = phase6_start + timedelta(weeks=1)
        
        return {
            "partner_selection": phase1_start - timedelta(weeks=2),
            "hardware_procurement": phase1_start - timedelta(weeks=3),
            "phase1_start": phase1_start,
            "sensor_deployment": phase1_start + timedelta(weeks=1),
            "participant_registration": phase1_start + timedelta(weeks=2),
            "phase2_start": phase2_start,
            "first_ceremony": phase2_start + timedelta(days=3),
            "all_ceremonies_complete": phase2_start + timedelta(weeks=1, days=4),
            "phase3_start": phase3_start,
            "first_check_in": phase3_start + timedelta(days=3),
            "phase4_start": phase4_start,
            "first_collective_pulse": phase4_start + timedelta(days=3),
            "community_action": phase4_start + timedelta(weeks=2),
            "phase5_start": phase5_start,
            "findings_presentation": phase5_start + timedelta(weeks=1, days=4),
            "phase6_start": phase6_start,
            "celebration_event": phase6_start + timedelta(days=4),
            "project_conclusion": conclusion
        }
