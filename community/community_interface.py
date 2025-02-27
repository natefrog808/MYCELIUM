import time
import json
from datetime import datetime, timedelta

class CommunityInterface:
    """
    The Community Interface for MYCELIUM system - enabling shared ecological awareness
    and collective stewardship within bioregional communities.
    """
    
    def __init__(self, watershed_id, admin_user=None):
        """
        Initialize the Community Interface for a specific watershed.
        
        Parameters:
        - watershed_id: Unique identifier for the bioregion/watershed
        - admin_user: Optional user with administrative privileges
        """
        self.watershed_id = watershed_id
        self.admin_user = admin_user
        
        # Connected users in this watershed community
        self.users = {}
        
        # Shared community data
        self.community_data = {
            "creation_date": datetime.now().isoformat(),
            "last_collective_pulse": None,
            "active_users": 0,
            "total_users": 0,
            "community_actions": [],
            "shared_observations": [],
            "sentinel_species": {},
            "community_health_index": 0.0,
            "community_stories": [],  # Collective reflections and narratives
            "watershed_lore": []      # Historical and ecological knowledge of place
        }
        
        # Ecological translators (will be set by the application)
        self.translators = {}
        
        # Communication channels for different sharing modes
        self.channels = {
            "collective_pulse": [],    # For synchronized feedback sessions
            "ecological_alerts": [],   # For critical ecological notifications
            "member_insights": [],     # For user observations and reflections
            "action_invites": [],      # For community stewardship opportunities
            "reflection_circle": [],   # For post-pulse or post-action sharing
            "notifications": []        # For individual and group notifications
        }
        
        # Community calendar for events
        self.calendar = []
        
        # Initialize watershed lore with basic entries
        self._initialize_watershed_lore()
        
    def _initialize_watershed_lore(self):
        """Set up initial watershed knowledge that can be unlocked"""
        # In a real implementation, this would be populated from a database
        # For prototype, we add some sample lore entries
        self.community_data["watershed_lore"] = [
            {
                "id": "lore_001",
                "title": "The Watershed's Formation",
                "content": "This coastal watershed was formed during the last ice age...",
                "type": "geological",
                "unlock_requirement": "observer",  # Available to all members
                "media_url": None
            },
            {
                "id": "lore_002",
                "title": "Indigenous Stewardship",
                "content": "For thousands of years, the Ohlone people tended...",
                "type": "cultural",
                "unlock_requirement": "participant",  # Requires some participation
                "media_url": None
            },
            {
                "id": "lore_003",
                "title": "The Great Flood of 1955",
                "content": "Winter storms caused unprecedented flooding...",
                "type": "historical",
                "unlock_requirement": "steward",  # Requires deeper engagement
                "media_url": None
            },
            {
                "id": "lore_004",
                "title": "Secret Life of the Creek",
                "content": "Beneath the surface, a complex food web...",
                "type": "ecological",
                "unlock_requirement": "elder",  # Only for the most engaged members
                "media_url": None
            }
        ]
        
    def register_user(self, user_id, user_info):
        """
        Add a user to the community.
        
        Parameters:
        - user_id: Unique identifier for the user
        - user_info: Dict with user profile information
        
        Returns:
        - success: Boolean indicating successful registration
        """
        if user_id in self.users:
            return {"success": False, "message": "User already registered"}
            
        # Store user info with community-specific additions
        self.users[user_id] = {
            "profile": user_info,
            "joined_date": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat(),
            "connection_strength": 0.0,  # Increases with participation
            "shared_feedback_count": 0,
            "actions_participated": 0,
            "observations_shared": 0,
            "bioregional_knowledge": 0.0,  # Familiarity with local ecosystem
            "sentinel_species": user_info.get("sentinel_species"),
            "notifications": [],
            "stewardship_goals": [],
            "reflections": [],
            "unlocked_lore": ["lore_001"],  # Start with basic watershed knowledge
            "badges": []
        }
        
        # Update community counters
        self.community_data["total_users"] += 1
        self.community_data["active_users"] += 1
        
        # Add user's sentinel species if provided
        if user_info.get("sentinel_species"):
            species = user_info["sentinel_species"]
            if species in self.community_data["sentinel_species"]:
                self.community_data["sentinel_species"][species] += 1
            else:
                self.community_data["sentinel_species"][species] = 1
        
        # Send welcome notification
        self._send_notification(
            user_id, 
            "Welcome to the MYCELIUM community for " + self._get_watershed_name(),
            "Welcome to a network of neighbors connected to this place. Complete your " +
            "Bioregional Bonding Ceremony to deepen your connection.",
            "welcome"
        )
        
        return {
            "success": True, 
            "message": f"Welcome to the {self._get_watershed_name()} community!",
            "community_size": self.community_data["total_users"]
        }
    
    def _get_watershed_name(self):
        """Get the human-readable name of the watershed"""
        # In real implementation, would query a database
        return "Coastal Creek Watershed"
        
    def initiate_collective_pulse(self, initiator_id, pulse_config):
        """
        Start a synchronized feedback session for community members.
        
        Parameters:
        - initiator_id: User starting the session
        - pulse_config: Dict with session parameters
        
        Returns:
        - session_id: Unique identifier for the collective pulse session
        """
        if initiator_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Create session details
        session_id = f"pulse_{int(time.time())}"
        pulse_time = pulse_config.get("scheduled_time", datetime.now().isoformat())
        domain = pulse_config.get("ecological_domain", "water_stress")
        focus_area = pulse_config.get("focus_area", None)  # Specific area in watershed
        duration = pulse_config.get("duration", 5 * 60)  # Default 5 minutes
        
        # Create the session
        pulse_session = {
            "session_id": session_id,
            "initiator": initiator_id,
            "time": pulse_time,
            "status": "scheduled",
            "domain": domain,
            "focus_area": focus_area,
            "duration": duration,
            "participants": [initiator_id],
            "feedback_pattern": None,  # Will be generated at session time
            "reflections": []
        }
        
        # Add to channels
        self.channels["collective_pulse"].append(pulse_session)
        
        # Update community data
        self.community_data["last_collective_pulse"] = pulse_time
        
        # Send notifications to all users
        pulse_time_readable = datetime.fromisoformat(pulse_time).strftime("%A, %B %d at %I:%M %p")
        for user_id in self.users:
            if user_id != initiator_id:  # Don't notify the initiator
                self._send_notification(
                    user_id,
                    f"New Collective Pulse: {self._domain_to_readable(domain)}",
                    f"Join your neighbors to feel the {self._domain_to_readable(domain)} of our watershed together on {pulse_time_readable}.",
                    "pulse_invite",
                    {"session_id": session_id}
                )
        
        return {
            "success": True,
            "session_id": session_id,
            "scheduled_time": pulse_time,
            "message": f"Collective pulse initiated for {self._domain_to_readable(domain)}"
        }
    
    def _domain_to_readable(self, domain):
        """Convert domain identifier to readable name"""
        domains = {
            "water_stress": "Water Health",
            "biodiversity": "Biodiversity",
            "soil_health": "Soil Vitality",
            "air_quality": "Air Quality"
        }
        return domains.get(domain, domain)
        
    def join_collective_pulse(self, user_id, session_id):
        """
        Add a user to a scheduled collective pulse session.
        
        Parameters:
        - user_id: User joining the session
        - session_id: Identifier for the session
        
        Returns:
        - success: Boolean indicating successful join
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Find the session
        for session in self.channels["collective_pulse"]:
            if session["session_id"] == session_id:
                if session["status"] not in ["scheduled", "open"]:
                    return {"error": "Session not available for joining"}
                    
                # Add user if not already participating
                if user_id not in session["participants"]:
                    session["participants"].append(user_id)
                    
                    # Update user metrics
                    self.users[user_id]["shared_feedback_count"] += 1
                    
                    # Check if this is their first pulse
                    if self.users[user_id]["shared_feedback_count"] == 1:
                        self._award_badge(user_id, "first_pulse", "First Collective Pulse")
                    
                return {
                    "success": True,
                    "message": f"Joined collective pulse for {self._domain_to_readable(session['domain'])}",
                    "participants": len(session["participants"])
                }
                
        return {"error": "Session not found"}
    
    def _generate_collective_feedback(self, session_id):
        """
        Create the shared feedback pattern for a collective pulse session.
        
        Parameters:
        - session_id: Identifier for the session
        
        Returns:
        - feedback: Dict with feedback parameters
        """
        # Find the session
        session = None
        for s in self.channels["collective_pulse"]:
            if s["session_id"] == session_id:
                session = s
                break
                
        if not session:
            return {"error": "Session not found"}
            
        # Get current ecological data for the domain
        current_data = self._get_current_ecological_data(session["domain"], session["focus_area"])
        
        # Use the appropriate translator
        if session["domain"] in self.translators:
            translator = self.translators[session["domain"]]
            feedback = translator.translate(current_data)
            
            # Add community-specific metadata
            feedback["community_context"] = {
                "participant_count": len(session["participants"]),
                "watershed": self._get_watershed_name(),
                "focus_area": session["focus_area"],
                "collective_intensity": min(1.0, len(session["participants"]) / 10 * 0.5 + 0.5)  # Scales with group size
            }
            
            # Store the generated feedback in the session
            session["feedback_pattern"] = feedback
            session["status"] = "active"
            
            return feedback
        else:
            return {"error": f"No translator available for {session['domain']}"}
    
    def _get_current_ecological_data(self, domain, focus_area=None):
        """
        Retrieve the latest ecological data for a specific domain.
        
        Parameters:
        - domain: Ecological domain (e.g., 'water_stress')
        - focus_area: Optional specific location within watershed
        
        Returns:
        - data: Dict with ecological measurements
        """
        # In real implementation, would query sensor network
        # For prototype, generate simulated data
        
        if domain == "water_stress":
            return {
                "soil_moisture": 25,  # Percentage
                "ecosystem_type": "temperate_forest",
                "additional_indicators": {
                    "leaf_water_potential": -1.2,  # Megapascals
                    "stream_flow": 0.7,  # Relative to normal
                    "precipitation_deficit": 15  # Percentage below normal
                }
            }
        elif domain == "biodiversity":
            return {
                "ecosystem_type": "temperate_forest",
                "species_count": 28,
                "bird_species": 18,
                "insect_orders": 8,
                "shannon_index": 2.8,
                "acoustic_diversity": 0.65
            }
        
        # Default empty data if domain not implemented
        return {"ecosystem_type": "temperate_forest"}
        
    def deliver_collective_pulse(self, session_id):
        """
        Send synchronized feedback to all participants in a pulse session.
        
        Parameters:
        - session_id: Identifier for the session
        
        Returns:
        - delivery_status: Dict with delivery information
        """
        # Find the session
        session = None
        for s in self.channels["collective_pulse"]:
            if s["session_id"] == session_id:
                session = s
                break
                
        if not session:
            return {"error": "Session not found"}
            
        if session["status"] not in ["scheduled", "open"]:
            return {"error": "Session not in deliverable state"}
            
        # Generate the collective feedback if not already done
        if not session["feedback_pattern"]:
            feedback = self._generate_collective_feedback(session_id)
        else:
            feedback = session["feedback_pattern"]
            
        # Update session status
        session["status"] = "active"
        session["start_time"] = datetime.now().isoformat()
        
        # Create a reflection circle for this pulse
        reflection_id = f"reflect_{session_id}"
        self.channels["reflection_circle"].append({
            "id": reflection_id,
            "type": "pulse_reflection",
            "source_id": session_id,
            "title": f"Reflections on {self._domain_to_readable(session['domain'])} Pulse",
            "start_time": session["start_time"],
            "end_time": None,
            "participants": session["participants"].copy(),
            "reflections": []
        })
        
        # Notify participants about the reflection circle
        for user_id in session["participants"]:
            self._send_notification(
                user_id,
                "Share your reflections",
                "The collective pulse is complete. Visit the reflection circle to share what you experienced.",
                "reflection_invite",
                {"reflection_id": reflection_id}
            )
        
        return {
            "success": True,
            "session_id": session_id,
            "participants": len(session["participants"]),
            "feedback": feedback,
            "message": f"Collective pulse active for {self._domain_to_readable(session['domain'])}",
            "reflection_circle": reflection_id
        }
    
    def share_reflection(self, user_id, reflection_data):
        """
        Allow a user to share their experience after a collective pulse or action.
        
        Parameters:
        - user_id: User sharing the reflection
        - reflection_data: Dict with reflection details
        
        Returns:
        - success: Boolean indicating successful sharing
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        reflection_id = reflection_data.get("reflection_id")
        if not reflection_id:
            return {"error": "Reflection circle ID required"}
            
        # Find the reflection circle
        circle = None
        for c in self.channels["reflection_circle"]:
            if c["id"] == reflection_id:
                circle = c
                break
                
        if not circle:
            return {"error": "Reflection circle not found"}
            
        # Ensure user is a participant
        if user_id not in circle["participants"]:
            return {"error": "User not a participant in this experience"}
            
        # Create the reflection
        reflection = {
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "content": reflection_data.get("content", ""),
            "emotion": reflection_data.get("emotion", ""),
            "insights": reflection_data.get("insights", []),
            "action_ideas": reflection_data.get("action_ideas", [])
        }
        
        # Add to reflection circle
        circle["reflections"].append(reflection)
        
        # Add to user's personal reflections
        self.users[user_id]["reflections"].append({
            "date": datetime.now().isoformat(),
            "type": circle["type"],
            "content": reflection["content"],
            "emotion": reflection["emotion"]
        })
        
        # Check if this is their first reflection
        if len(self.users[user_id]["reflections"]) == 1:
            self._award_badge(user_id, "first_reflection", "First Reflection")
            
        # Check if reflection contains action ideas
        if reflection["action_ideas"]:
            # Notify community leaders about potential actions
            for u_id, user in self.users.items():
                if self._calculate_community_rank(user) in ["steward", "elder"]:
                    self._send_notification(
                        u_id,
                        "New action idea shared",
                        f"A community member suggested: {reflection['action_ideas'][0]}",
                        "action_idea"
                    )
        
        # Check if all participants have reflected
        reflected_users = set(r["user_id"] for r in circle["reflections"])
        if reflected_users == set(circle["participants"]):
            # Add to community stories if significant
            if len(circle["reflections"]) >= 3:
                self.community_data["community_stories"].append({
                    "id": f"story_{int(time.time())}",
                    "title": circle["title"],
                    "date": datetime.now().isoformat(),
                    "source_type": circle["type"],
                    "source_id": circle["source_id"],
                    "reflections": len(circle["reflections"]),
                    "summary": self._generate_story_summary(circle["reflections"])
                })
        
        return {
            "success": True,
            "message": "Reflection shared with the community",
            "reflection_count": len(circle["reflections"])
        }
    
    def _generate_story_summary(self, reflections):
        """Generate a brief summary of collective reflections"""
        # In real implementation, would use NLP to create a cohesive narrative
        # For prototype, a simple concatenation
        if not reflections:
            return "No reflections shared yet."
            
        emotions = [r.get("emotion") for r in reflections if r.get("emotion")]
        common_emotion = max(set(emotions), key=emotions.count) if emotions else "varied"
        
        return f"The community shared {len(reflections)} reflections, expressing " + \
               f"primarily {common_emotion} feelings about this experience."
    
    def set_stewardship_goal(self, user_id, goal_data):
        """
        Allow a user to set personal ecological stewardship goals.
        
        Parameters:
        - user_id: User setting the goal
        - goal_data: Dict with goal details
        
        Returns:
        - success: Boolean indicating successful goal setting
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Create the goal
        goal = {
            "id": f"goal_{int(time.time())}",
            "title": goal_data.get("title", "Untitled Goal"),
            "description": goal_data.get("description", ""),
            "domain": goal_data.get("domain", "general"),
            "target_date": goal_data.get("target_date"),
            "created_date": datetime.now().isoformat(),
            "status": "active",
            "progress": 0,  # 0-100
            "milestones": goal_data.get("milestones", []),
            "is_public": goal_data.get("is_public", False),
            "updates": []
        }
        
        # Add to user's goals
        self.users[user_id]["stewardship_goals"].append(goal)
        
        # If public, notify community about new goal
        if goal["is_public"]:
            for u_id in self.users:
                if u_id != user_id:
                    self._send_notification(
                        u_id,
                        "New community stewardship goal",
                        f"{self.users[user_id]['profile'].get('name', 'A neighbor')} has committed to: {goal['title']}",
                        "goal_announcement"
                    )
        
        return {
            "success": True,
            "goal_id": goal["id"],
            "message": f"Stewardship goal '{goal['title']}' created"
        }
    
    def update_goal_progress(self, user_id, goal_id, progress_data):
        """
        Update progress on a personal stewardship goal.
        
        Parameters:
        - user_id: User updating the goal
        - goal_id: Identifier for the goal
        - progress_data: Dict with progress details
        
        Returns:
        - success: Boolean indicating successful update
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Find the goal
        goal = None
        for g in self.users[user_id]["stewardship_goals"]:
            if g["id"] == goal_id:
                goal = g
                break
                
        if not goal:
            return {"error": "Goal not found"}
            
        # Update progress
        old_progress = goal["progress"]
        new_progress = progress_data.get("progress", old_progress)
        goal["progress"] = new_progress
        
        # Add update
        update = {
            "timestamp": datetime.now().isoformat(),
            "old_progress": old_progress,
            "new_progress": new_progress,
            "note": progress_data.get("note", "")
        }
        goal["updates"].append(update)
        
        # Check for goal completion
        if old_progress < 100 and new_progress >= 100:
            goal["status"] = "completed"
            
            # Award badge for completed goal
            self._award_badge(user_id, "goal_completed", "Stewardship Goal Completed")
            
            # If public, notify community about completion
            if goal["is_public"]:
                for u_id in self.users:
                    if u_id != user_id:
                        self._send_notification(
                            u_id,
                            "Stewardship goal achieved!",
                            f"{self.users[user_id]['profile'].get('name', 'A neighbor')} has completed their goal: {goal['title']}",
                            "goal_completed"
                        )
        
        return {
            "success": True,
            "progress": new_progress,
            "status": goal["status"],
            "message": "Goal progress updated"
        }
    
    def share_observation(self, user_id, observation_data):
        """
        Allow a user to share an ecological observation with the community.
        
        Parameters:
        - user_id: User sharing the observation
        - observation_data: Dict with observation details
        
        Returns:
        - success: Boolean indicating successful sharing
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Create observation record
        observation = {
            "id": f"obs_{int(time.time())}",
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "location": observation_data.get("location", None),
            "type": observation_data.get("type", "general"),  # e.g., species sighting, water clarity
            "description": observation_data.get("description", ""),
            "media": observation_data.get("media", []),  # e.g., photos, audio
            "feedback_felt": observation_data.get("feedback_felt", None),
            "community_relevance": 0.0,  # Will be updated as others engage
            "responses": []
        }
        
        # Add to community shared observations
        self.community_data["shared_observations"].append(observation)
        
        # Update user metrics
        self.users[user_id]["observations_shared"] += 1
        self.users[user_id]["last_active"] = datetime.now().isoformat()
        
        # Calculate ecological impact (if applicable)
        impact = self._calculate_observation_impact(observation)
        if impact["significant"]:
            # Add to ecological alerts if significant
            self.channels["ecological_alerts"].append({
                "source": "user_observation",
                "observation_id": observation["id"],
                "alert_level": impact["level"],
                "message": impact["message"]
            })
            
            # Notify relevant users about significant observation
            self._notify_about_observation(observation, impact)
        
        # Check for badges
        if self.users[user_id]["observations_shared"] == 1:
            self._award_badge(user_id, "first_observation", "First Field Observation")
        elif self.users[user_id]["observations_shared"] == 10:
            self._award_badge(user_id, "field_naturalist", "Field Naturalist")
        
        # Check if observation relates to user's sentinel species
        user_sentinel = self.users[user_id].get("sentinel_species")
        if user_sentinel and observation_data.get("species") == user_sentinel:
            self._award_badge(user_id, "sentinel_observer", "Sentinel Species Guardian")
        
        return {
            "success": True,
            "observation_id": observation["id"],
            "impact": impact,
            "message": "Observation shared with the community"
        }
    
    def _notify_about_observation(self, observation, impact):
        """Send notifications about significant observations"""
        # Determine who should be notified based on impact and relevance
        
        # For sentinel species, notify everyone with that sentinel
        if observation.get("type") == "species_sighting" and "species" in observation:
            species = observation["species"]
            for user_id, user in self.users.items():
                if user_id != observation["user_id"] and user.get("sentinel_species") == species:
                    self._send_notification(
                        user_id,
                        f"Your sentinel species was observed!",
                        f"A {species} was observed at {observation.get('location', 'the watershed')}.",
                        "sentinel_sighting",
                        {"observation_id": observation["id"]}
                    )
        
        # For high impact observations, notify stewards and elders
        if impact["level"] in ["medium", "high"]:
            for user_id, user in self.users.items():
                if user_id != observation["user_id"] and self._calculate_community_rank(user) in ["steward", "elder"]:
                    self._send_notification(
                        user_id,
                        f"Significant ecological observation",
                        impact["message"],
                        "ecological_alert",
                        {"observation_id": observation["id"]}
                    )
    
    def _calculate_observation_impact(self, observation):
        """Determine the ecological significance of an observation"""
        # In real implementation, would use ecological models
        # For prototype, use simple heuristics
        
        # Example: Species sighting significance
        if observation["type"] == "species_sighting":
            species = observation.get("species", "")
            if species in self.community_data["sentinel_species"]:
                return {
                    "significant": True,
                    "level": "medium",
                    "message": f"Sentinel species '{species}' observed at {observation['location']}"
                }
                
        # Default minimal impact
        return {
            "significant": False,
            "level": "low",
            "message": "Observation recorded"
        }
        
    def propose_community_action(self, user_id, action_data):
        """
        Allow a user to propose a collective stewardship action.
        
        Parameters:
        - user_id: User proposing the action
        - action_data: Dict with action details
        
        Returns:
        - success: Boolean indicating successful proposal
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Create action proposal
        action = {
            "id": f"action_{int(time.time())}",
            "proposer": user_id,
            "timestamp": datetime.now().isoformat(),
            "title": action_data.get("title", "Untitled Action"),
            "description": action_data.get("description", ""),
            "location": action_data.get("location", None),
            "ecological_domain": action_data.get("domain", "general"),
            "proposed_date": action_data.get("date", None),
            "status": "proposed",
            "participants": [user_id],
            "supporters": 0,
            "comments": []
        }
        
        # Add to community actions
        self.community_data["community_actions"].append(action)
        
        # Add to action invites channel
        self.channels["action_invites"].append({
            "action_id": action["id"],
            "title": action["title"],
            "proposer": user_id,
            "proposed_date": action["proposed_date"]
        })
        
        # Update user metrics
        self.users[user_id]["actions_participated"] += 1
        self.users[user_id]["last_active"] = datetime.now().isoformat()
        
        # Add to community calendar if date provided
        if action["proposed_date"]:
            self.calendar.append({
                "type": "proposed_action",
                "title": action["title"],
                "date": action["proposed_date"],
                "action_id": action["id"]
            })
        
        # Notify community members about the new action
        proposed_date = ""
        if action["proposed_date"]:
            date_obj = datetime.fromisoformat(action["proposed_date"])
            proposed_date = f" on {date_obj.strftime('%A, %B %d')}"
            
        for u_id in self.users:
            if u_id != user_id:
                self._send_notification(
                    u_id,
                    f"New community action proposed",
                    f"{self.users[user_id]['profile'].get('name', 'A neighbor')} is organizing " +
                    f"'{action['title']}'{proposed_date}. Will you join?",
                    "action_invite",
                    {"action_id": action["id"]}
                )
        
        return {
            "success": True,
            "action_id": action["id"],
            "message": f"Action '{action['title']}' proposed to the community"
        }
    
    def join_community_action(self, user_id, action_id):
        """
        Add a user as a participant in a community action.
        
        Parameters:
        - user_id: User joining the action
        - action_id: Identifier for the action
        
        Returns:
        - success: Boolean indicating successful join
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        # Find the action
        for action in self.community_data["community_actions"]:
            if action["id"] == action_id:
                if user_id not in action["participants"]:
                    action["participants"].append(user_id)
                    action["supporters"] += 1
                    
                    # Update user metrics
                    self.users[user_id]["actions_participated"] += 1
                    self.users[user_id]["last_active"] = datetime.now().isoformat()
                    
                    # Notify the action proposer
                    self._send_notification(
                        action["proposer"],
                        "Someone joined your action!",
                        f"{self.users[user_id]['profile'].get('name', 'A neighbor')} has joined your action: {action['title']}",
                        "action_joined"
                    )
                    
                    # Check for badges
                    if self.users[user_id]["actions_participated"] == 1:
                        self._award_badge(user_id, "first_action", "First Community Action")
                    elif self.users[user_id]["actions_participated"] == 5:
                        self._award_badge(user_id, "community_steward", "Community Steward")
                    
                return {
                    "success": True,
                    "message": f"Joined action '{action['title']}'",
                    "participants": len(action["participants"])
                }
                
        return {"error": "Action not found"}
    
    def _send_notification(self, user_id, title, message, notification_type, data=None):
        """Send a notification to a user"""
        if user_id not in self.users:
            return False
            
        notification = {
            "id": f"notif_{int(time.time())}_{user_id[-4:]}",
            "timestamp": datetime.now().isoformat(),
            "title": title,
            "message": message,
            "type": notification_type,
            "read": False,
            "data": data or {}
        }
        
        # Add to user's notifications
        self.users[user_id]["notifications"].append(notification)
        
        # Add to notifications channel (for potential real-time delivery)
        self.channels["notifications"].append({
            "user_id": user_id,
            "notification": notification
        })
        
        return True
    
    def _award_badge(self, user_id, badge_id, badge_name):
        """Award a badge to a user for achievements"""
        if user_id not in self.users:
            return False
            
        # Check if user already has this badge
        existing_badges = [b["id"] for b in self.users[user_id]["badges"]]
        if badge_id in existing_badges:
            return False
            
        # Create badge
        badge = {
            "id": badge_id,
            "name": badge_name,
            "awarded_date": datetime.now().isoformat(),
            "description": self._get_badge_description(badge_id)
        }
        
        # Add to user's badges
        self.users[user_id]["badges"].append(badge)
        
        # Send notification
        self._send_notification(
            user_id,
            f"New Badge: {badge_name}",
            f"You've earned the {badge_name} badge! {badge['description']}",
            "badge_earned",
            {"badge_id": badge_id}
        )
        
        # Check if badge unlocks lore
        new_lore = self._check_lore_unlocks(user_id)
        
        return True
    
    def _get_badge_description(self, badge_id):
        """Get the description for a badge"""
        descriptions = {
            "first_pulse": "You experienced your first Collective Pulse with the community.",
            "first_reflection": "You shared your first reflection after a community experience.",
            "first_observation": "You shared your first ecological observation with the community.",
            "field_naturalist": "You've shared 10 ecological observations with the community.",
            "sentinel_observer": "You observed your own sentinel species in the wild.",
            "first_action": "You participated in your first community stewardship action.",
            "community_steward": "You've participated in 5 community stewardship actions.",
            "goal_completed": "You completed a personal stewardship goal.",
            "pulse_elder": "You've participated in 10 Collective Pulses."
        }
        
        return descriptions.get(badge_id, "A recognition of your contribution to the watershed community.")
    
    def _check_lore_unlocks(self, user_id):
        """Check if a user has unlocked new watershed lore"""
        if user_id not in self.users:
            return []
            
        user = self.users[user_id]
        rank = self._calculate_community_rank(user)
        newly_unlocked = []
        
        # Check each lore item against user's rank
        for lore in self.community_data["watershed_lore"]:
            required_rank = lore.get("unlock_requirement", "elder")
            lore_id = lore["id"]
            
            # Check if it's unlockable and not already unlocked
            if lore_id not in user["unlocked_lore"]:
                if (required_rank == "observer" or
                    (required_rank == "participant" and rank in ["participant", "steward", "elder"]) or
                    (required_rank == "steward" and rank in ["steward", "elder"]) or
                    (required_rank == "elder" and rank == "elder")):
                    
                    # Unlock it!
                    user["unlocked_lore"].append(lore_id)
                    newly_unlocked.append(lore_id)
                    
                    # Notify user
                    self._send_notification(
                        user_id,
                        "New Watershed Knowledge Unlocked",
                        f"You've unlocked '{lore['title']}' - a piece of your watershed's story.",
                        "lore_unlocked",
                        {"lore_id": lore_id}
                    )
        
        return newly_unlocked
    
    def get_community_activity(self, days=7):
        """
        Retrieve recent community engagement metrics.
        
        Parameters:
        - days: Number of days to include
        
        Returns:
        - activity: Dict with activity statistics
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Count recent actions and observations
        recent_actions = [a for a in self.community_data["community_actions"] 
                         if datetime.fromisoformat(a["timestamp"]) > cutoff_date]
        recent_observations = [o for o in self.community_data["shared_observations"]
                              if datetime.fromisoformat(o["timestamp"]) > cutoff_date]
        
        # Count active users
        active_users = [u for u_id, u in self.users.items() 
                       if datetime.fromisoformat(u["last_active"]) > cutoff_date]
        
        # Get recent collective pulses
        recent_pulses = [p for p in self.channels["collective_pulse"]
                        if p.get("time") and datetime.fromisoformat(p["time"]) > cutoff_date]
        
        return {
            "timeframe": f"Past {days} days",
            "active_users": len(active_users),
            "active_percentage": len(active_users) / max(1, len(self.users)) * 100,
            "new_actions": len(recent_actions),
            "new_observations": len(recent_observations),
            "collective_pulses": len(recent_pulses),
            "most_active_domain": self._get_most_active_domain(recent_observations, recent_actions),
            "community_health_trend": self._calculate_community_health_trend()
        }
    
    def _get_most_active_domain(self, observations, actions):
        """Determine which ecological domain has most community engagement"""
        # Count domain occurrences
        domains = {}
        
        for obs in observations:
            domain = obs.get("type", "general")
            domains[domain] = domains.get(domain, 0) + 1
            
        for action in actions:
            domain = action.get("ecological_domain", "general")
            domains[domain] = domains.get(domain, 0) + 1
            
        # Find the most common
        if not domains:
            return "general"
            
        return max(domains.items(), key=lambda x: x[1])[0]
    
    def _calculate_community_health_trend(self):
        """Evaluate trend in community engagement and impact"""
        # In real implementation, would use more sophisticated analytics
        # For prototype, simple metric based on participation
        
        # Get community size factor (more users = higher expectations)
        size_factor = min(1.0, len(self.users) / 50)
        
        # Calculate activity level (0-1)
        if not self.community_data["total_users"]:
            return "no_data"
            
        activity_ratio = self.community_data["active_users"] / self.community_data["total_users"]
        
        # Evaluate trend
        if activity_ratio > 0.7:
            return "thriving"
        elif activity_ratio > 0.4:
            return "healthy"
        elif activity_ratio > 0.2:
            return "maintaining"
        else:
            return "declining"
    
    def get_user_community_profile(self, user_id):
        """
        Retrieve a user's community participation profile.
        
        Parameters:
        - user_id: Target user
        
        Returns:
        - profile: Dict with community-specific user metrics
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        user = self.users[user_id]
        
        # Calculate connection strength based on participation
        participation_score = (
            user["shared_feedback_count"] * 0.2 +
            user["actions_participated"] * 0.5 +
            user["observations_shared"] * 0.3
        ) / max(1, self.community_data["total_users"])
        
        # Update user's connection strength
        user["connection_strength"] = min(1.0, participation_score)
        
        # Find user's sentinel species status
        sentinel_health = "unknown"
        if user.get("sentinel_species"):
            # In real implementation, would check ecological data
            sentinel_health = "stable"
        
        # Get personal goals summary
        active_goals = [g for g in user.get("stewardship_goals", []) if g["status"] == "active"]
        completed_goals = [g for g in user.get("stewardship_goals", []) if g["status"] == "completed"]
        
        return {
            "user_id": user_id,
            "joined_date": user["joined_date"],
            "connection_strength": user["connection_strength"],
            "community_rank": self._calculate_community_rank(user),
            "participation_stats": {
                "shared_feedback_sessions": user["shared_feedback_count"],
                "actions_participated": user["actions_participated"],
                "observations_shared": user["observations_shared"]
            },
            "bioregional_knowledge": user["bioregional_knowledge"],
            "sentinel_species": {
                "name": user.get("sentinel_species"),
                "health": sentinel_health
            },
            "community_impact": self._calculate_user_impact(user_id),
            "badges": user.get("badges", []),
            "stewardship_goals": {
                "active": len(active_goals),
                "completed": len(completed_goals)
            },
            "unlocked_lore": len(user.get("unlocked_lore", []))
        }
    
    def _calculate_community_rank(self, user):
        """Determine user's standing in the community"""
        # Based on connection strength
        if user["connection_strength"] > 0.8:
            return "elder"
        elif user["connection_strength"] > 0.5:
            return "steward"
        elif user["connection_strength"] > 0.2:
            return "participant"
        else:
            return "observer"
    
    def _calculate_user_impact(self, user_id):
        """Evaluate user's impact on community and ecosystem"""
        # In real implementation, would use more sophisticated metrics
        # For prototype, simple count of engagements
        
        user = self.users[user_id]
        return {
            "community_effect": min(1.0, user["actions_participated"] * 0.1),
            "knowledge_shared": min(1.0, user["observations_shared"] * 0.05),
            "ecological_footprint": "positive" if user["actions_participated"] > 3 else "neutral"
        }
    
    def get_community_summary(self):
        """
        Provide an overview of the community's structure and activities.
        
        Returns:
        - summary: Dict with community information
        """
        # Calculate community metrics
        avg_connection = sum(u["connection_strength"] for u in self.users.values()) / max(1, len(self.users))
        active_actions = sum(1 for a in self.community_data["community_actions"] if a["status"] in ["proposed", "active"])
        
        # Count users by rank
        ranks = {"elder": 0, "steward": 0, "participant": 0, "observer": 0}
        for user in self.users.values():
            rank = self._calculate_community_rank(user)
            ranks[rank] = ranks.get(rank, 0) + 1
        
        return {
            "name": self._get_watershed_name(),
            "id": self.watershed_id,
            "creation_date": self.community_data["creation_date"],
            "members": {
                "total": self.community_data["total_users"],
                "active": self.community_data["active_users"],
                "by_rank": ranks
            },
            "connection_strength": avg_connection,
            "activities": {
                "active_actions": active_actions,
                "total_observations": len(self.community_data["shared_observations"]),
                "collective_pulses": len(self.channels["collective_pulse"])
            },
            "sentinel_species": self.community_data["sentinel_species"],
            "health": self._calculate_community_health_trend(),
            "upcoming_events": self._get_upcoming_events(3)
        }
    
    def _get_upcoming_events(self, count=3):
        """Get the next few community events"""
        now = datetime.now()
        upcoming = []
        
        for event in self.calendar:
            if event.get("date") and datetime.fromisoformat(event["date"]) > now:
                upcoming.append(event)
                
        # Sort by date
        upcoming.sort(key=lambda x: datetime.fromisoformat(x["date"]))
        
        return upcoming[:count]
    
    def get_user_notifications(self, user_id, include_read=False):
        """
        Retrieve notifications for a specific user.
        
        Parameters:
        - user_id: Target user
        - include_read: Whether to include already read notifications
        
        Returns:
        - notifications: List of notification objects
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        notifications = self.users[user_id].get("notifications", [])
        
        if not include_read:
            notifications = [n for n in notifications if not n.get("read", False)]
            
        # Sort by timestamp (newest first)
        notifications.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        return {
            "count": len(notifications),
            "notifications": notifications
        }
    
    def mark_notification_read(self, user_id, notification_id):
        """Mark a notification as read"""
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        for notification in self.users[user_id].get("notifications", []):
            if notification.get("id") == notification_id:
                notification["read"] = True
                return {"success": True}
                
        return {"error": "Notification not found"}
    
    def get_watershed_lore(self, user_id):
        """
        Get available watershed knowledge for a user.
        
        Parameters:
        - user_id: Target user
        
        Returns:
        - lore: List of available lore items
        """
        if user_id not in self.users:
            return {"error": "User not registered in this community"}
            
        user = self.users[user_id]
        unlocked_ids = user.get("unlocked_lore", [])
        
        # Filter lore to items user has unlocked
        available_lore = [lore for lore in self.community_data["watershed_lore"] 
                         if lore["id"] in unlocked_ids]
                         
        # Sort by ID (typically chronological)
        available_lore.sort(key=lambda x: x["id"])
        
        # Get locked lore count for motivation
        locked_count = len(self.community_data["watershed_lore"]) - len(available_lore)
        
        return {
            "unlocked": len(available_lore),
            "locked": locked_count,
            "lore": available_lore
        }
        
        # Check each lore item against user's rank
        for lore in self.community_data["watershed_lore"]:
            required_rank = lore.get("unlock_requirement", "elder")
            lore_id = lore["id"]
          
