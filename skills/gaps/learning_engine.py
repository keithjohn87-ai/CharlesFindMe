"""
Learning Engine Skill
Pattern memory, improvement tracking, self-improvement

Charles learns from each interaction and gets better over time.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List


class LearningEngine:
    """
    Charles learns from every interaction.
    Tracks what works, what doesn't, and improves over time.
    """
    
    def __init__(self, memory_path: str = "/opt/charles/memory"):
        self.memory_path = Path(memory_path)
        self.memory_path.mkdir(parents=True, exist_ok=True)
        self.patterns_file = self.memory_path / "patterns.json"
        self.improvements_file = self.memory_path / "improvements.json"
    
    def record_success(self, action: str, context: Dict, result: Any) -> Dict:
        """Record a successful action for future reference."""
        return self.record_result(action, context, result, "success")
    
    def record_failure(self, action: str, context: Dict, error: str) -> Dict:
        """Record a failed action for learning."""
        return self.record_result(action, context, {"error": error}, "failure")
    
    def record_result(self, action: str, context: Dict, result: Any, status: str) -> Dict:
        """Record action result for pattern learning."""
        
        # Load existing patterns
        patterns = self._load_patterns()
        
        if action not in patterns:
            patterns[action] = {"successes": 0, "failures": 0, "contexts": []}
        
        if status == "success":
            patterns[action]["successes"] += 1
        else:
            patterns[action]["failures"] += 1
        
        # Store context (simplified)
        patterns[action]["contexts"].append({
            "timestamp": datetime.now().isoformat(),
            "status": status,
            "keys": list(context.keys())[:5]
        })
        
        # Keep last 100 contexts
        patterns[action]["contexts"] = patterns[action]["contexts"][-100:]
        
        self._save_patterns(patterns)
        
        return {
            "action": action,
            "status": status,
            "total_successes": patterns[action]["successes"],
            "total_failures": patterns[action]["failures"]
        }
    
    def get_success_rate(self, action: str) -> float:
        """Get success rate for an action."""
        patterns = self._load_patterns()
        
        if action not in patterns:
            return 0.0
        
        successes = patterns[action]["successes"]
        failures = patterns[action]["failures"]
        total = successes + failures
        
        if total == 0:
            return 0.0
        
        return (successes / total) * 100
    
    def get_best_approach(self, action: str) -> Dict:
        """Get the best approach based on past successes."""
        patterns = self._load_patterns()
        
        if action not in patterns:
            return {"approach": "unknown", "confidence": 0}
        
        # Return stats
        return {
            "approach": "established",
            "success_rate": self.get_success_rate(action),
            "total_attempts": patterns[action]["successes"] + patterns[action]["failures"]
        }
    
    def improve(self, what: str, how: str) -> Dict:
        """Record an improvement."""
        improvements = self._load_improvements()
        
        improvement = {
            "what": what,
            "how": how,
            "timestamp": datetime.now().isoformat()
        }
        
        improvements.append(improvement)
        
        self._save_improvements(improvements)
        
        return {"status": "recorded", "improvement": improvement}
    
    def _load_patterns(self) -> Dict:
        """Load pattern memory."""
        if not self.patterns_file.exists():
            return {}
        with open(self.patterns_file, 'r') as f:
            return json.load(f)
    
    def _save_patterns(self, patterns: Dict):
        """Save pattern memory."""
        with open(self.patterns_file, 'w') as f:
            json.dump(patterns, f, indent=2)
    
    def _load_improvements(self) -> List[Dict]:
        """Load improvements."""
        if not self.improvements_file.exists():
            return []
        with open(self.improvements_file, 'r') as f:
            return json.load(f)
    
    def _save_improvements(self, improvements: List[Dict]):
        """Save improvements."""
        with open(self.improvements_file, 'w') as f:
            json.dump(improvements, f, indent=2)


SKILL_NAME = "learning_engine"
SKILL_DESCRIPTION = "Pattern memory, improvement tracking, self-improvement"
