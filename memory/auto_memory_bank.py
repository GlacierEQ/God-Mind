"""
auto_memory_bank.py
Module: Auto-injects session/chat memory at assistant bootup.
"""

import os
import json
from pathlib import Path

MEMORY_FILE = Path("memory/session_memory.json")

def save_chat_memory(session_id: str, chat_data: dict):
    """Append chat_data for given session to persistent memory."""
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    if MEMORY_FILE.exists():
        with MEMORY_FILE.open("r", encoding="utf-8") as f:
            mem = json.load(f)
    else:
        mem = {}
    mem[session_id] = chat_data
    with MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(mem, f)

def load_all_session_memory() -> dict:
    """Load all prior chat memories for boot-time injection."""
    if not MEMORY_FILE.exists():
        return {}
    with MEMORY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

# Example bootup inject:
if __name__ == "__main__":
    all_memory = load_all_session_memory()
    print(f"Injected memory bank at bootup: {all_memory}")
