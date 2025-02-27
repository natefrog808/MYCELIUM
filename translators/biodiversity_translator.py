import time

class BiodiversityTranslator:
    """
    Translates biodiversity data into neural feedback patterns 
    for the MYCELIUM system's Translation Layer.
    """
    
    def __init__(self):
        # Define healthy ranges for different ecosystem types
        self.diversity_thresholds = {
            "temperate_forest": {
                "species_count": {"optimal": (20, 50), "low_threshold": 10},
                "bird_species": {"optimal": (15, 30), "low_threshold": 8},
                "insect_orders": {"optimal": (8, 12), "low_threshold": 5},
                "shannon_index": {"optimal": (2.5, 4.0), "low_threshold": 2.0}
            },
            "grassland": {
                "species_count": {"optimal": (15, 40), "low_threshold": 8},
                "bird_species": {"optimal": (10, 25), "low_threshold": 6},
                "insect_orders": {"optimal": (7, 10), "low_threshold": 4},
                "shannon_index": {"optimal": (2.0, 3.5), "low_threshold": 1.5}
            },
            "wetland": {
                "species_count": {"optimal": (25, 60), "low_threshold": 15},
                "bird_species": {"optimal": (20, 40), "low_threshold": 12},
                "insect_orders": {"optimal": (8, 12), "low_threshold": 5},
                "shannon_index": {"optimal": (2.8, 4.5), "low_threshold": 2.2}
            },
            "desert_scrub": {
                "species_count": {"optimal": (10, 30), "low_threshold": 5},
                "bird_species": {"optimal": (8, 20), "low_threshold": 4},
                "insect_orders": {"optimal": (5, 8), "low_threshold": 3},
                "shannon_index": {"optimal": (1.5, 3.0), "low_threshold": 1.0}
            }
        }
        
        # Feedback parameters
        self.max_complexity = 10.0  # Maximum feedback complexity
        self.base_complexity = 3.0  # Baseline complexity
        
        # Previous readings for trend analysis
        self.previous_readings = {
            "depletion_level": None,
            "timestamp": None
        }
    
    def analyze_biodiversity(self, biodiversity_data, ecosystem_type):
        """
        Analyze biodiversity health based on species counts and diversity indices.
        
        Parameters:
        - biodiversity_data: Dict with species counts and diversity metrics
        - ecosystem_type: Type of ecosystem (e.g., 'temperate_forest')
        
        Returns:
        - depletion_level: Float between 0 (healthy) and 1 (severe depletion)
        """
        if ecosystem_type not in self.diversity_thresholds:
            raise ValueError(f"Unknown ecosystem type: {ecosystem_type}")
        
        thresholds = self.diversity_thresholds[ecosystem_type]
        depletion_scores = []
        
        # Check overall species count if available
        if "species_count" in biodiversity_data:
            species_count = biodiversity_data["species_count"]
            species_thresholds = thresholds["species_count"]
            optimal_low, optimal_high = species_thresholds["optimal"]
            low_threshold = species_thresholds["low_threshold"]
            
            if species_count < low_threshold:
                # Below threshold - higher depletion score
                depletion = min(1.0, (low_threshold - species_count) / low_threshold)
                depletion_scores.append(depletion * 1.2)  # Weight species count slightly higher
            elif species_count < optimal_low:
                # Below optimal but above threshold
                depletion = (optimal_low - species_count) / (optimal_low - low_threshold)
                depletion_scores.append(depletion * 0.8)
            else:
                # Within or above optimal range
                depletion_scores.append(0.0)
        
        # Check bird species diversity if available
        if "bird_species" in biodiversity_data:
            bird_count = biodiversity_data["bird_species"]
            bird_thresholds = thresholds["bird_species"]
            optimal_low, optimal_high = bird_thresholds["optimal"]
            low_threshold = bird_thresholds["low_threshold"]
            
            if bird_count < low_threshold:
                depletion = min(1.0, (low_threshold - bird_count) / low_threshold)
                depletion_scores.append(depletion)
            elif bird_count < optimal_low:
                depletion = (optimal_low - bird_count) / (optimal_low - low_threshold)
                depletion_scores.append(depletion * 0.7)
            else:
                depletion_scores.append(0.0)
        
        # Check insect diversity if available
        if "insect_orders" in biodiversity_data:
            insect_count = biodiversity_data["insect_orders"]
            insect_thresholds = thresholds["insect_orders"]
            optimal_low, optimal_high = insect_thresholds["optimal"]
            low_threshold = insect_thresholds["low_threshold"]
            
            if insect_count < low_threshold:
                depletion = min(1.0, (low_threshold - insect_count) / low_threshold)
                depletion_scores.append(depletion * 1.1)  # Weight insects as important indicators
            elif insect_count < optimal_low:
                depletion = (optimal_low - insect_count) / (optimal_low - low_threshold)
                depletion_scores.append(depletion * 0.8)
            else:
                depletion_scores.append(0.0)
        
        # Check Shannon diversity index if available (more comprehensive)
        if "shannon_index" in biodiversity_data:
            shannon = biodiversity_data["shannon_index"]
            shannon_thresholds = thresholds["shannon_index"]
            optimal_low, optimal_high = shannon_thresholds["optimal"]
            low_threshold = shannon_thresholds["low_threshold"]
            
            if shannon < low_threshold:
                depletion = min(1.0, (low_threshold - shannon) / low_threshold)
                depletion_scores.append(depletion * 1.3)  # Weight Shannon index higher
            elif shannon < optimal_low:
                depletion = (optimal_low - shannon) / (optimal_low - low_threshold)
                depletion_scores.append(depletion * 0.9)
            else:
                depletion_scores.append(0.0)
        
        # If acoustic metrics are available (soundscape richness)
        if "acoustic_diversity" in biodiversity_data:
            acoustic = biodiversity_data["acoustic_diversity"]
            # Scale from 0-1 where 1 is maximum acoustic diversity
            depletion = max(0, 1 - acoustic)
            depletion_scores.append(depletion)
        
        # Calculate weighted average if any scores exist
        if depletion_scores:
            return sum(depletion_scores) / len(depletion_scores)
        else:
            # No biodiversity data available
            return 0.5  # Default to moderate concern if no data
    
    def generate_feedback_pattern(self, depletion_level, previous_depletion=None):
        """
        Generate haptic feedback pattern based on biodiversity analysis.
        
        Parameters:
        - depletion_level: Float between 0 (healthy) and 1 (severe depletion)
        - previous_depletion: Previous depletion level for trend detection
        
        Returns:
        - pattern: Dict with haptic feedback parameters
        """
        # Check for recovery trend
        if previous_depletion is not None and depletion_level < previous_depletion and previous_depletion > 0.3:
            recovery_ratio = min(1.0, (previous_depletion - depletion_level) / previous_depletion)
            
            # Generate recovery pattern - a gradually increasing richness
            return {
                "type": "expanding_harmony",
                "complexity": self.base_complexity + (self.max_complexity - self.base_complexity) * (1 - depletion_level),
                "rhythm": "building",
                "layers": max(2, int((1 - depletion_level) * 8)),
                "duration": 4.0,
                "location": "whole_body",
                "description": "A gradually expanding sensation of harmony, like a forest awakening",
                "emotion": "hope"
            }
        
        if depletion_level < 0.2:
            # Healthy biodiversity - rich, layered sensation
            return {
                "type": "harmony",
                "complexity": self.max_complexity * 0.8,
                "rhythm": "layered",
                "layers": max(3, int((1 - depletion_level) * 10)),
                "duration": 3.0,
                "frequency_range": "full_spectrum",
                "location": "whole_body",
                "description": "A rich, expansive symphony of sensations, like standing in a vibrant ecosystem",
                "emotion": "wonder"
            }
        elif depletion_level < 0.5:
            # Moderate biodiversity - simplified harmony
            return {
                "type": "simplified_harmony",
                "complexity": self.max_complexity * 0.5,
                "rhythm": "regular",
                "layers": max(2, int((1 - depletion_level) * 6)),
                "duration": 2.5,
                "frequency_range": "limited",
                "location": "torso_and_arms",
                "description": "A pleasant but simplified pattern, like a garden with fewer species",
                "emotion": "contentment"
            }
        else:
            # Low biodiversity - sparse, monotonous pulse
            return {
                "type": "monotony",
                "complexity": self.base_complexity + (self.max_complexity - self.base_complexity) * (1 - depletion_level),
                "rhythm": "repetitive",
                "layers": max(1, int((1 - depletion_level) * 3)),
                "duration": 2.0,
                "frequency_range": "narrow",
                "location": "arms_only",
                "description": "A sparse, monotonous pulse signaling ecological simplification",
                "emotion": "concern" if depletion_level < 0.7 else "alarm"
            }
    
    def translate(self, sensor_data, timestamp=None):
        """
        Main translation function - converts raw biodiversity data to neural feedback pattern.
        
        Parameters:
        - sensor_data: Dict containing biodiversity metrics and ecosystem type
        - timestamp: Current timestamp (optional)
        
        Returns:
        - feedback: Dict with haptic feedback parameters
        """
        biodiversity_data = {k: v for k, v in sensor_data.items() 
                            if k not in ["ecosystem_type", "timestamp"]}
        ecosystem_type = sensor_data.get("ecosystem_type")
        
        if not biodiversity_data or ecosystem_type is None:
            raise ValueError("Missing required sensor data: biodiversity metrics and ecosystem_type")
        
        # Track previous depletion level for trend analysis
        previous_depletion = self.previous_readings["depletion_level"]
        
        # Analyze current biodiversity health
        depletion_level = self.analyze_biodiversity(biodiversity_data, ecosystem_type)
        
        # Generate feedback pattern with trend awareness
        feedback = self.generate_feedback_pattern(depletion_level, previous_depletion)
        
        # Store current readings for future comparison
        self.previous_readings = {
            "depletion_level": depletion_level,
            "timestamp": timestamp or time.time()
        }
        
        # Add trend information if available
        if previous_depletion is not None:
            trend = depletion_level - previous_depletion
            if abs(trend) > 0.05:  # Significant change
                feedback["trend"] = {
                    "direction": "improving" if trend < 0 else "worsening",
                    "magnitude": abs(trend),
                }
        
        return feedback


if __name__ == "__main__":
    # Example usage
    translator = BiodiversityTranslator()
    
    biodiversity_data = {
        "ecosystem_type": "temperate_forest",
        "species_count": 28,
        "bird_species": 18,
        "insect_orders": 8,
        "shannon_index": 2.8,
        "acoustic_diversity": 0.65
    }
    
    feedback = translator.translate(biodiversity_data)
    print(feedback)
