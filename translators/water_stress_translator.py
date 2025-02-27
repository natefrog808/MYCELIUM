import time

class WaterStressTranslator:
    """
    Translates soil moisture and plant stress data into neural feedback patterns
    for the MYCELIUM system's Translation Layer.
    """
    
    def __init__(self):
        # Define healthy ranges for different ecosystem types
        self.ecosystem_moisture_ranges = {
            "temperate_forest": {"optimal": (30, 45), "stress_threshold": 25, "saturation_threshold": 55},
            "grassland": {"optimal": (20, 35), "stress_threshold": 15, "saturation_threshold": 45},
            "desert_scrub": {"optimal": (8, 20), "stress_threshold": 5, "saturation_threshold": 30},
            "wetland": {"optimal": (60, 85), "stress_threshold": 50, "saturation_threshold": 95},
            "rainforest": {"optimal": (50, 70), "stress_threshold": 45, "saturation_threshold": 80},
        }
        
        # Feedback intensity calibration
        self.max_intensity = 10.0  # Maximum feedback intensity
        self.base_intensity = 2.0  # Baseline intensity for subtle awareness
        
        # Duration parameters (in seconds)
        self.pulse_duration = 0.8
        self.pause_duration = 1.2
        
        # Store previous readings for trend analysis
        self.previous_readings = {
            "soil_moisture": None,
            "stress_level": None,
            "timestamp": None
        }
    
    def analyze_water_stress(self, soil_moisture, ecosystem_type, additional_indicators=None):
        """
        Analyze current water stress level based on soil moisture and ecosystem type.
        
        Parameters:
        - soil_moisture: Percentage of soil moisture (0-100)
        - ecosystem_type: Type of ecosystem (e.g., 'temperate_forest')
        - additional_indicators: Dict with optional indicators like leaf water potential,
                               stream flow rates, etc.
        
        Returns:
        - stress_level: Float between 0 (no stress) and 1 (extreme stress)
        - is_saturated: Boolean indicating waterlogging rather than drought
        - saturation_level: Float between 0 and 1 indicating saturation severity
        """
        if ecosystem_type not in self.ecosystem_moisture_ranges:
            raise ValueError(f"Unknown ecosystem type: {ecosystem_type}")
            
        ranges = self.ecosystem_moisture_ranges[ecosystem_type]
        optimal_low, optimal_high = ranges["optimal"]
        stress_threshold = ranges["stress_threshold"]
        saturation_threshold = ranges["saturation_threshold"]
        
        # Initialize base analysis values
        stress_level = 0.0
        is_saturated = False
        saturation_level = 0.0
        
        # Check for saturation (too much water)
        if soil_moisture > saturation_threshold:
            saturation_level = min(1.0, (soil_moisture - saturation_threshold) / 
                                (100 - saturation_threshold))
            is_saturated = True
        
        # Check for drought stress (too little water)
        elif soil_moisture < optimal_low:
            # Calculate stress level (0 to 1) based on distance from optimal range
            if soil_moisture <= stress_threshold:
                # Below stress threshold - more severe feedback
                stress_level = min(1.0, (stress_threshold - soil_moisture) / stress_threshold)
                # Use exponential scaling for severe stress to reflect non-linear ecological impact
                if stress_level > 0.7:
                    stress_level = min(1.0, 0.7 + (stress_level - 0.7) ** 0.7)
            else:
                # Between stress threshold and optimal - milder feedback
                stress_level = (optimal_low - soil_moisture) / (optimal_low - stress_threshold)
        
        # Integrate additional indicators if available
        if additional_indicators:
            # Leaf water potential (plant stress)
            leaf_potential = additional_indicators.get("leaf_water_potential")
            if leaf_potential is not None:
                # Adjust stress based on plant response
                if leaf_potential < -2.0:  # Severe plant stress threshold
                    stress_level = min(1.0, stress_level + 0.2)  # Amplify stress
                elif leaf_potential < -1.5:  # Moderate plant stress
                    stress_level = min(1.0, stress_level + 0.1)  # Slightly increase stress
            
            # Stream flow (watershed health)
            stream_flow = additional_indicators.get("stream_flow")
            if stream_flow is not None and stream_flow < 0.5:  # Below 50% of normal flow
                stress_level = min(1.0, stress_level * 1.3)  # Increase stress by up to 30%
            
            # Water table depth
            water_table = additional_indicators.get("water_table_depth")
            if water_table is not None:
                # If water table is falling (positive change in depth)
                if water_table > additional_indicators.get("normal_water_table_depth", 0) * 1.5:
                    stress_level = min(1.0, stress_level + 0.15)  # Indicate groundwater depletion
            
            # Precipitation deficit
            precip_deficit = additional_indicators.get("precipitation_deficit")
            if precip_deficit is not None and precip_deficit > 30:  # More than 30% below normal
                # This indicates persistent drought conditions
                stress_level = min(1.0, stress_level + (precip_deficit / 100) * 0.2)
                
        return stress_level, is_saturated, saturation_level
    
    def generate_feedback_pattern(self, stress_level, is_saturated, saturation_level=0.0, previous_stress=None):
        """
        Generate haptic feedback pattern based on water stress analysis.
        
        Parameters:
        - stress_level: Float between 0 (no stress) and 1 (extreme stress)
        - is_saturated: Boolean indicating if the issue is saturation not drought
        - saturation_level: Float between 0 and 1 indicating saturation severity
        - previous_stress: Float representing the previous stress level (for trend detection)
        
        Returns:
        - pattern: Dict with haptic feedback parameters
        """
        # Recovery pattern - detect improving conditions
        if previous_stress is not None and stress_level < previous_stress and previous_stress > 0.3 and stress_level < 0.3:
            # Significant recovery from stressed state
            recovery_ratio = min(1.0, (previous_stress - stress_level) / previous_stress)
            return {
                "type": "recovery",
                "intensity": self.base_intensity + (self.max_intensity - self.base_intensity) * recovery_ratio * 0.4,
                "rhythm": "slow_release",
                "pulse_count": 3,
                "duration": self.pulse_duration * 2,
                "frequency": "medium_low",
                "location": "whole_body",
                "description": "A gentle release from tension to warmth, signaling ecosystem recovery",
                "emotion": "relief"
            }
        
        if stress_level == 0 and not is_saturated:
            # No stress - gentle, affirming feedback
            return {
                "type": "affirmation",
                "intensity": self.base_intensity * 0.5,
                "rhythm": "steady",
                "pulse_count": 1,
                "duration": self.pulse_duration,
                "frequency": "low",
                "location": "whole_body",
                "description": "A gentle, affirming warmth indicating healthy water balance",
                "emotion": "contentment"
            }
        
        if is_saturated:
            # Saturation feedback - heavy, pressing sensation
            intensity = self.base_intensity + (self.max_intensity - self.base_intensity) * (saturation_level ** 1.5)  # Non-linear scaling
            return {
                "type": "pressure",
                "intensity": intensity,
                "rhythm": "wave",
                "pulse_count": 2,
                "duration": self.pulse_duration * 1.5,
                "frequency": "low",
                "location": "chest_and_limbs",
                "description": "A slow, heavy pressure mimicking the feeling of waterlogged soil",
                "emotion": "heaviness"
            }
        
        # Drought stress feedback - increasing tension/constriction with severity
        pulse_count = max(2, min(5, int(stress_level * 6)))  # More rapid pulses for higher stress
        
        # Non-linear intensity scaling to emphasize severe drought conditions
        intensity = self.base_intensity + (self.max_intensity - self.base_intensity) * (stress_level ** 1.5)
        
        return {
            "type": "tension",
            "intensity": intensity,
            "rhythm": "staccato" if stress_level > 0.7 else "intermittent",
            "pulse_count": pulse_count,
            "duration": self.pulse_duration * (1.0 - stress_level * 0.5),  # Shorter pulses for higher stress
            "frequency": "medium_high",
            "location": "throat_and_chest",
            "description": "A constricting sensation mimicking thirst, intensifying with drought severity",
            "emotion": "concern" if stress_level < 0.5 else "urgency"
        }
    
    def translate(self, sensor_data, timestamp=None):
        """
        Main translation function - converts raw sensor data to neural feedback pattern.
        
        Parameters:
        - sensor_data: Dict containing 'soil_moisture', 'ecosystem_type', and optionally
                     additional water-related indicators
        - timestamp: Current timestamp (optional)
        
        Returns:
        - feedback: Dict with haptic feedback parameters
        """
        soil_moisture = sensor_data.get("soil_moisture")
        ecosystem_type = sensor_data.get("ecosystem_type")
        additional_indicators = sensor_data.get("additional_indicators")
        
        if soil_moisture is None or ecosystem_type is None:
            raise ValueError("Missing required sensor data: soil_moisture and ecosystem_type")
            
        # Track the previous stress level for trend analysis
        previous_stress = self.previous_readings["stress_level"]
            
        # Analyze current water stress
        stress_level, is_saturated, saturation_level = self.analyze_water_stress(
            soil_moisture, ecosystem_type, additional_indicators
        )
        
        # Generate feedback pattern with trend awareness
        feedback = self.generate_feedback_pattern(
            stress_level, 
            is_saturated, 
            saturation_level,
            previous_stress
        )
        
        # Store current readings for future comparison
        self.previous_readings = {
            "soil_moisture": soil_moisture,
            "stress_level": stress_level,
            "timestamp": timestamp or time.time()
        }
        
        # Augment feedback with trend information
        if previous_stress is not None:
            trend = stress_level - previous_stress
            if abs(trend) > 0.1:  # Significant change
                feedback["trend"] = {
                    "direction": "improving" if trend < 0 else "worsening",
                    "magnitude": abs(trend),
                }
        
        return feedback
        
    def get_historical_trends(self, timeframe=None):
        """
        Provide information about water stress trends over time.
        This would be expanded as the system collects more historical data.
        
        Parameters:
        - timeframe: Optional timeframe to analyze (e.g., "daily", "weekly")
        
        Returns:
        - trend_data: Dict with trend information
        """
        # This is a placeholder for future expansion
        # In a full implementation, this would access a time-series database
        if self.previous_readings["stress_level"] is None:
            return {"trend": "unknown", "confidence": 0}
            
        # For now, just return the most recent trend
        return {
            "current_stress": self.previous_readings["stress_level"],
            "last_reading_time": self.previous_readings["timestamp"],
            "trend": "unknown",  # Would be calculated from historical data
            "confidence": 0  # Confidence in the trend assessment
        }


if __name__ == "__main__":
    # Example usage
    translator = WaterStressTranslator()
    
    sensor_data = {
        "soil_moisture": 18,
        "ecosystem_type": "temperate_forest",
        "additional_indicators": {
            "leaf_water_potential": -1.8,
            "stream_flow": 0.3
        }
    }
    
    feedback = translator.translate(sensor_data)
    print(feedback)
