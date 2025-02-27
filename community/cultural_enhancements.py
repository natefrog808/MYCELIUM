import time
from datetime import datetime, timedelta

class CulturalEnhancementsIntegrator:
    """
    A utility class that adds cultural inclusivity and diversity enhancements to an existing
    CommunityInterface instance.
    """
    
    @staticmethod
    def integrate(community_interface):
        """
        Add cultural enhancement methods to a CommunityInterface instance.
        
        Parameters:
        - community_interface: An existing CommunityInterface instance
        
        Returns:
        - Enhanced CommunityInterface with new methods
        """
        # Add new methods to the instance
        community_interface.customize_bonding_ceremony = CulturalEnhancementsIntegrator._customize_bonding_ceremony
        community_interface.track_diversity_metrics = CulturalEnhancementsIntegrator._track_diversity_metrics
        community_interface.collect_interface_feedback = CulturalEnhancementsIntegrator._collect_interface_feedback
        community_interface.get_feedback_summary = CulturalEnhancementsIntegrator._get_feedback_summary
        community_interface._generate_ceremony_locations = CulturalEnhancementsIntegrator._generate_ceremony_locations
        community_interface._generate_diversity_recommendations = CulturalEnhancementsIntegrator._generate_diversity_recommendations
        
        # Initialize new data structures if needed
        if "interface_feedback" not in community_interface.community_data:
            community_interface.community_data["interface_feedback"] = []
        
        if "diversity_metrics" not in community_interface.community_data:
            community_interface.community_data["diversity_metrics"] = {
                "timestamp": datetime.now().isoformat(),
                "metrics": {}
            }
        
        if "bonding_ceremony" not in community_interface.community_data:
            community_interface.community_data["bonding_ceremony"] = None
        
        return community_interface
    
    @staticmethod
    def _customize_bonding_ceremony(self, community_input):
        """
        Customize the Bioregional Bonding Ceremony based on community preferences.
        
        Parameters:
        - community_input: Dict with ceremony preferences (e.g., rituals, languages, symbols)
        
        Returns:
        - ceremony_plan: Dict with tailored ceremony details
        """
        ceremony_plan = {
            "title": community_input.get("title", "Bioregional Bonding Ceremony"),
            "rituals": community_input.get("rituals", ["soil_collection", "sentinel_identification"]),
            "language": community_input.get("language", "English"),
            "symbols": community_input.get("symbols", []),
            "welcome_message": community_input.get("welcome_message", "Welcome to our shared watershed."),
            "created_by": "Community Collaboration",
            "timestamp": datetime.now().isoformat(),
            "cultural_elements": community_input.get("cultural_elements", []),
            "indigenous_acknowledgment": community_input.get("indigenous_acknowledgment", ""),
            "accessibility_accommodations": community_input.get("accessibility_accommodations", [])
        }
        
        # Store in community data for reference
        self.community_data["bonding_ceremony"] = ceremony_plan
        
        # Create ceremony locations based on watershed features
        ceremony_plan["locations"] = self._generate_ceremony_locations(
            ceremony_plan["rituals"], 
            community_input.get("preferred_locations", [])
        )
        
        # Notify all users about the customized ceremony
        for user_id in self.users:
            self._send_notification(
                user_id,
                f"Our {ceremony_plan['title']} is Ready",
                f"The community has shaped a bonding ceremony in {ceremony_plan['language']} " +
                f"with rituals like {', '.join(ceremony_plan['rituals'][:2])}. Join us!",
                "ceremony_invite",
                {"ceremony_id": f"ceremony_{int(time.time())}"}
            )
        
        return {"success": True, "ceremony_plan": ceremony_plan}
    
    @staticmethod
    def _generate_ceremony_locations(self, rituals, preferred_locations):
        """Helper method to match rituals with appropriate watershed locations"""
        # This would use watershed GIS data in a full implementation
        # For prototype, match rituals to location types
        
        # Map rituals to location types
        ritual_location_map = {
            "soil_collection": ["streambank", "hilltop", "forest_edge", "meadow"],
            "sentinel_identification": ["biodiversity_hotspot", "wildlife_corridor"],
            "water_blessing": ["spring", "confluence", "lake_shore"],
            "directional_acknowledgment": ["high_point", "open_space"],
            "ancestor_honoring": ["historical_site", "old_growth_tree"],
            "future_visioning": ["restoration_site", "community_garden"]
        }
        
        # Generate locations, prioritizing community preferences
        locations = []
        for ritual in rituals:
            suitable_types = ritual_location_map.get(ritual, ["general"])
            
            # Check if there's a preferred location matching this ritual
            matched = False
            for pref in preferred_locations:
                if pref.get("ritual") == ritual or pref.get("type") in suitable_types:
                    locations.append({
                        "name": pref.get("name", f"Community-selected {ritual} site"),
                        "type": pref.get("type", suitable_types[0]),
                        "coordinates": pref.get("coordinates", [0, 0]),
                        "ritual": ritual,
                        "description": pref.get("description", f"Location for {ritual}")
                    })
                    matched = True
                    break
            
            # If no preference matched, suggest a location
            if not matched:
                locations.append({
                    "name": f"Suggested {ritual} site",
                    "type": suitable_types[0],
                    "coordinates": [0, 0],  # Would be real coordinates in implementation
                    "ritual": ritual,
                    "description": f"Recommended location for {ritual}"
                })
        
        return locations
    
    @staticmethod
    def _track_diversity_metrics(self):
        """
        Track diversity metrics among participants to ensure varied perspectives.
        
        Returns:
        - metrics: Dict with diversity statistics
        """
        diversity_metrics = {
            "total_users": self.community_data["total_users"],
            "cultural_backgrounds": set(),
            "languages": set(),
            "age_groups": {"<18": 0, "18-30": 0, "31-50": 0, "51+": 0},
            "sentinel_species_diversity": len(self.community_data["sentinel_species"]),
            "focus_areas": set(),
            "accessibility_needs": set()
        }
        
        for user in self.users.values():
            profile = user["profile"]
            enhanced = profile.get("enhanced_profile", {})
            
            # Cultural background
            if enhanced.get("cultural_background"):
                diversity_metrics["cultural_backgrounds"].add(enhanced["cultural_background"])
            
            # Languages
            if enhanced.get("languages"):
                diversity_metrics["languages"].update(enhanced["languages"])
            
            # Age group
            if enhanced.get("age"):
                age = enhanced["age"]
                if age < 18:
                    diversity_metrics["age_groups"]["<18"] += 1
                elif age <= 30:
                    diversity_metrics["age_groups"]["18-30"] += 1
                elif age <= 50:
                    diversity_metrics["age_groups"]["31-50"] += 1
                else:
                    diversity_metrics["age_groups"]["51+"] += 1
            
            # Focus areas
            if profile.get("focus_areas"):
                diversity_metrics["focus_areas"].update(profile["focus_areas"])
            
            # Accessibility needs
            if enhanced.get("accessibility_needs"):
                diversity_metrics["accessibility_needs"].update(enhanced["accessibility_needs"])
        
        # Convert sets to counts for serialization
        diversity_metrics["cultural_backgrounds"] = len(diversity_metrics["cultural_backgrounds"])
        diversity_metrics["languages"] = len(diversity_metrics["languages"])
        diversity_metrics["focus_areas"] = len(diversity_metrics["focus_areas"])
        diversity_metrics["accessibility_needs"] = len(diversity_metrics["accessibility_needs"])
        
        # Store metrics in community data
        self.community_data["diversity_metrics"] = {
            "timestamp": datetime.now().isoformat(),
            "metrics": diversity_metrics
        }
        
        # Generate diversity recommendations if metrics suggest imbalance
        recommendations = self._generate_diversity_recommendations(diversity_metrics)
        if recommendations and self.admin_user:
            self._send_notification(
                self.admin_user,
                "Diversity Metrics Update",
                "Current participant diversity may need attention. See recommendations.",
                "diversity_alert",
                {"recommendations": recommendations}
            )
        
        return diversity_metrics
    
    @staticmethod
    def _generate_diversity_recommendations(self, metrics):
        """Generate recommendations for improving participant diversity"""
        recommendations = []
        
        # Check age balance
        young_participants = metrics["age_groups"]["<18"] + metrics["age_groups"]["18-30"]
        older_participants = metrics["age_groups"]["31-50"] + metrics["age_groups"]["51+"]
        total_with_age = sum(metrics["age_groups"].values())
        
        if total_with_age > 0:
            if young_participants / total_with_age < 0.2:
                recommendations.append("Consider recruiting younger participants (under 30)")
            if older_participants / total_with_age < 0.2:
                recommendations.append("Consider recruiting more participants over 30")
        
        # Check cultural diversity
        if metrics["cultural_backgrounds"] < 3 and metrics["total_users"] > 10:
            recommendations.append("Seek greater cultural diversity in recruitment")
        
        # Check languages
        if metrics["languages"] < 2 and metrics["total_users"] > 5:
            recommendations.append("Consider including multilingual participants")
        
        # Check accessibility
        if metrics["accessibility_needs"] == 0 and metrics["total_users"] > 10:
            recommendations.append("Ensure testing includes participants with accessibility needs")
        
        return recommendations
    
    @staticmethod
    def _collect_interface_feedback(self, user_id, feedback_data):
        """
        Collect user feedback on the Community Interface and flag for iteration.
        
        Parameters:
        - user_id: User providing feedback
        - feedback_data: Dict with feedback (e.g., rating, comments, feature)
        
        Returns:
        - success: Boolean indicating feedback was recorded
        """
        if user_id not in self.users:
            return {"error": "User not registered"}
        
        feedback = {
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "feature": feedback_data.get("feature", "general"),
            "rating": feedback_data.get("rating", 0),  # 1-5 scale
            "comment": feedback_data.get("comment", ""),
            "cultural_relevance_score": feedback_data.get("cultural_relevance", 0),  # 1-5 scale
            "accessibility_score": feedback_data.get("accessibility", 0),  # 1-5 scale
            "action_required": feedback_data.get("rating", 0) <= 3,  # Flag for review if low rating
            "tags": feedback_data.get("tags", [])
        }
        
        # Store feedback
        if "interface_feedback" not in self.community_data:
            self.community_data["interface_feedback"] = []
        self.community_data["interface_feedback"].append(feedback)
        
        # Notify admins if action is required
        if feedback["action_required"] and self.admin_user:
            self._send_notification(
                self.admin_user,
                "Interface Feedback Requires Attention",
                f"User {user_id} rated {feedback['feature']} {feedback['rating']}/5: {feedback['comment']}",
                "admin_alert",
                {"feedback_id": len(self.community_data["interface_feedback"]) - 1}
            )
        
        # Check for cultural relevance issues
        if feedback.get("cultural_relevance_score", 0) <= 2:
            if self.admin_user:
                self._send_notification(
                    self.admin_user,
                    "Cultural Relevance Concern",
                    f"Feature '{feedback['feature']}' received low cultural relevance rating",
                    "cultural_alert",
                    {"feedback_id": len(self.community_data["interface_feedback"]) - 1}
                )
        
        # Check for accessibility issues
        if feedback.get("accessibility_score", 0) <= 2:
            if self.admin_user:
                self._send_notification(
                    self.admin_user,
                    "Accessibility Concern",
                    f"Feature '{feedback['feature']}' may have accessibility issues",
                    "accessibility_alert",
                    {"feedback_id": len(self.community_data["interface_feedback"]) - 1}
                )
        
        # Award badge for providing detailed feedback
        if len(feedback["comment"]) > 50 or feedback.get("tags"):
            user = self.users[user_id]
            if "feedback_provider" not in [b["id"] for b in user.get("badges", [])]:
                self._award_badge(user_id, "feedback_provider", "Thoughtful Feedback Provider")
        
        return {"success": True, "message": "Thank you for your feedback!"}
    
    @staticmethod
    def _get_feedback_summary(self, feature=None, timeframe_days=None):
        """
        Generate a summary of interface feedback for iteration planning.
        
        Parameters:
        - feature: Optional feature to filter feedback
        - timeframe_days: Optional number of days to include
        
        Returns:
        - summary: Dict with feedback statistics and action items
        """
        if "interface_feedback" not in self.community_data:
            return {"error": "No feedback collected yet"}
        
        all_feedback = self.community_data["interface_feedback"]
        
        # Apply filters
        filtered_feedback = all_feedback
        if feature:
            filtered_feedback = [f for f in filtered_feedback if f["feature"] == feature]
        
        if timeframe_days:
            cutoff = datetime.now() - timedelta(days=timeframe_days)
            filtered_feedback = [
                f for f in filtered_feedback 
                if datetime.fromisoformat(f["timestamp"]) > cutoff
            ]
        
        if not filtered_feedback:
            return {"message": "No feedback matching criteria"}
        
        # Calculate statistics
        avg_rating = sum(f["rating"] for f in filtered_feedback) / len(filtered_feedback)
        
        # Group by feature
        feature_ratings = {}
        for f in filtered_feedback:
            feat = f["feature"]
            if feat not in feature_ratings:
                feature_ratings[feat] = {"ratings": [], "comments": []}
            feature_ratings[feat]["ratings"].append(f["rating"])
            if f["comment"]:
                feature_ratings[feat]["comments"].append(f["comment"])
        
        # Calculate average by feature
        feature_averages = {}
        for feat, data in feature_ratings.items():
            feature_averages[feat] = sum(data["ratings"]) / len(data["ratings"])
        
        # Identify features needing attention
        attention_needed = [
            feat for feat, avg in feature_averages.items() 
            if avg <= 3.0
        ]
        
        # Calculate cultural relevance and accessibility scores if available
        cultural_scores = [
            f["cultural_relevance_score"] for f in filtered_feedback 
            if "cultural_relevance_score" in f
        ]
        
        accessibility_scores = [
            f["accessibility_score"] for f in filtered_feedback 
            if "accessibility_score" in f
        ]
        
        avg_cultural = sum(cultural_scores) / len(cultural_scores) if cultural_scores else None
        avg_accessibility = sum(accessibility_scores) / len(accessibility_scores) if accessibility_scores else None
        
        # Collect frequently mentioned tags
        all_tags = []
        for f in filtered_feedback:
            all_tags.extend(f.get("tags", []))
        
        tag_counts = {}
        for tag in all_tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # Get top tags
        top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "feedback_count": len(filtered_feedback),
            "average_rating": avg_rating,
            "feature_averages": feature_averages,
            "attention_needed": attention_needed,
            "cultural_relevance": avg_cultural,
            "accessibility": avg_accessibility,
            "top_tags": top_tags,
            "timestamp": datetime.now().isoformat()
        }
