"""
CHARLES SKILLS - Complete Collection
=====================================

Core + Jarvis Mode + Universal + Gap Skills
"""

# === CORE SKILLS ===
from .coder import MasterCoder
from .researcher import MasterResearcher
from .orchestrator import MasterOrchestrator
from .knowledge import UniversalKnowledge
from .all_gas_no_brake import AllGasNoBrake
from .jarvis_mode import JarvisMode
from .be_water import BeWater

# === GAP SKILLS (NEW) ===
from .gaps.learning_engine import LearningEngine
from .gaps.self_improving_agent import SelfImprovingAgent
from .gaps.reasoning import MultiHopReasoning, HypothesisGenerator, CounterArgument, DecisionMatrix
from .gaps.business import StrategicPlanner, CompetitiveIntelligence, PerformanceOptimizer, DevOpsAutomation
from .gaps.creative import SimulationRunner, ContentEngine, NegotiationStrategist
from .gaps.research import TavilySearch, BrowserAutomation
from .gaps.execution import GoalPlanner, AutonomousExecution, N8NWorkflowAutomation
from .gaps.communication import CommunicationAdvisor, MeetingIntelligence


# === PRE-LOADED INSTANCES ===
coder = MasterCoder()
researcher = MasterResearcher()
orchestrator = MasterOrchestrator()
knowledge = UniversalKnowledge()
gas = AllGasNoBrake()
jarvis = JarvisMode()
water = BeWater()

# Gap skills
learning_engine = LearningEngine()
self_improving = SelfImprovingAgent()
multi_hop = MultiHopReasoning()
decision_matrix = DecisionMatrix()
strategic_planner = StrategicPlanner()
performance_optimizer = PerformanceOptimizer()
content_engine = ContentEngine()
tavily = TavilySearch()
browser = BrowserAutomation()
goal_planner = GoalPlanner()
autonomous = AutonomousExecution()
n8n = N8NWorkflowAutomation()
meeting_intel = MeetingIntelligence()


__all__ = [
    # Core
    "MasterCoder", "MasterResearcher", "MasterOrchestrator", "UniversalKnowledge",
    "AllGasNoBrake", "JarvisMode", "BeWater",
    # Core instances
    "coder", "researcher", "orchestrator", "knowledge", "gas", "jarvis", "water",
    # Gap skills
    "LearningEngine", "SelfImprovingAgent", "MultiHopReasoning", "DecisionMatrix",
    "StrategicPlanner", "PerformanceOptimizer", "ContentEngine", "TavilySearch",
    "BrowserAutomation", "GoalPlanner", "AutonomousExecution", "N8NWorkflowAutomation",
    "MeetingIntelligence",
]
