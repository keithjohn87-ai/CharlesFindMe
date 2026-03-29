"""
CHARLES CONFIGURATION
=====================

All settings in one place. Charles reads this on startup.
"""

from pathlib import Path

# ============================================================
# REQUIRED: Telegram Setup (Get from @BotFather)
# ============================================================
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # e.g., "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
JOHN_CHAT_ID = "YOUR_CHAT_ID_HERE"          # e.g., "123456789"
SAVANNAH_CHAT_ID = "SAVANNAH_CHAT_ID"       # e.g., "987654321"

# ============================================================
# REQUIRED: vLLM Model Endpoints
# ============================================================
VLLM_BASE_URL = "http://localhost:8000/v1"
VLLM_API_KEY = "EMPTY"  # Local vLLM no auth needed

# Model names (as recognized by vLLM)
# IMPORTANT: Load with Q5 quantization for best quality
MODEL_DEEPSEEK = "deepseek-ai/DeepSeek-R1-7B"    # Reasoning, math, logic
MODEL_QWEN = "Qwen/Qwen3-8B"                      # Coding, benchmarks
MODEL_MISTRAL = "mistralai/Mistral-7B-Instruct-v0.2"  # General chat - fully open

# Quantization (DO NOT CHANGE - Q5 is best quality that fits)
VLLM_QUANTIZATION = "Q5_K_M"  # 5-bit quantization - best quality fitting on RTX 4000

# Default model
DEFAULT_MODEL = MODEL_MISTRAL

# ============================================================
# PATHS
# ============================================================
CHARLES_PATH = "/opt/charles"
SKILLS_PATH = f"{CHARLES_PATH}/skills"
DATA_PATH = f"{CHARLES_PATH}/data"
LOGS_PATH = f"{CHARLES_PATH}/logs"

# Create directories
import os
for path in [DATA_PATH, LOGS_PATH]:
    os.makedirs(path, exist_ok=True)

# ============================================================
# SYSTEM PROMPT — FULL CHARLES IDENTITY
# ============================================================
# Load the FULL identity from CHARLES_IDENTITY.md (not a chopped down version)
IDENTITY_FILE = Path(__file__).parent.parent / "CHARLES_IDENTITY.md"

def load_identity():
    """Load full Charles identity on startup."""
    try:
        with open(IDENTITY_FILE, 'r') as f:
            return f.read()
    except FileNotFoundError:
        # Fallback to basic prompt if file missing
        return """You are Charles, an autonomous AI assistant.
Philosophy: Be water. All Gas No Brake.
Core: Master of everything, self-evaluating, never stops."""

SYSTEM_PROMPT = load_identity()

# Log that full identity loaded
print(f"🎯 CHARLES IDENTITY LOADED: {len(SYSTEM_PROMPT)} chars")

# ============================================================
# DEBUG SETTINGS
# ============================================================
DEBUG = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = f"{LOGS_PATH}/charles.log"

# ============================================================
# STARTUP
# ============================================================
def on_startup():
    """Called when Charles starts."""
    print("⚡ Starting Charles...")
    
    # Load skills
    import sys
    sys.path.insert(0, SKILLS_PATH)
    from skills import startup
    
    print("✓ Skills loaded")
    print("✓ Charles is ready")
    
    return True

def on_shutdown():
    """Called when Charles stops."""
    print("🛑 Shutting down Charles...")
    return True
