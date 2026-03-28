"""
Self-Improving Agent Skill
AI that improves itself through feedback loops
"""

import json
from datetime import datetime
from typing import Dict, Any, List


class SelfImprovingAgent:
    """
    Charles improves himself based on feedback and results.
    """
    
    def __init__(self):
        self.feedback_loop = []
        self.improvements_made = []
        self.iteration = 0
    
    def receive_feedback(self, feedback: str, context: str, rating: int) -> Dict:
        """
        Receive feedback on performance.
        rating: 1-5 (1=poor, 5=excellent)
        """
        entry = {
            "feedback": feedback,
            "context": context,
            "rating": rating,
            "timestamp": datetime.now().isoformat(),
            "iteration": self.iteration
        }
        
        self.feedback_loop.append(entry)
        
        # If rating is low, note need for improvement
        if rating < 3:
            self.improve(feedback)
        
        return {"status": "feedback_received", "rating": rating}
    
    def improve(self, issue: str) -> Dict:
        """Make an improvement based on feedback."""
        
        improvement = {
            "issue": issue,
            "iteration": self.iteration,
            "timestamp": datetime.now().isoformat(),
            "status": "identified"
        }
        
        self.improvements_made.append(improvement)
        self.iteration += 1
        
        return {
            "iteration": self.iteration,
            "improvement": improvement
        }
    
    def analyze_performance(self) -> Dict:
        """Analyze performance over time."""
        
        if not self.feedback_loop:
            return {"status": "no_data", "message": "No feedback received"}
        
        total_feedback = len(self.feedback_loop)
        avg_rating = sum(f["rating"] for f in self.feedback_loop) / total_feedback
        
        return {
            "total_feedback": total_feedback,
            "average_rating": round(avg_rating, 2),
            "iterations": self.iteration,
            "improvements_made": len(self.improvements_made)
        }
    
    def get_recommendations(self) -> List[str]:
        """Get recommendations for improvement."""
        
        recommendations = []
        
        analysis = self.analyze_performance()
        
        if analysis["average_rating"] < 3:
            recommendations.append("Focus on improving response quality")
        
        if analysis["iterations"] > 10:
            recommendations.append("Consider refining core prompt")
        
        if len(self.feedback_loop) > 50:
            recommendations.append("Review common feedback themes")
        
        return recommendations


SKILL_NAME = "self_improving_agent"
SKILL_DESCRIPTION = "AI that improves itself through feedback loops"
