# CONTEXT WINDOWS BY MODEL & AGENT
==================================

## THE 3 MODELS (on GEX44)

| Model | Context Window | Best For |
|-------|----------------|----------|
| **DeepSeek R1** (7B) | 64K tokens | Reasoning, math, logic |
| **Qwen3** (8B) | 32K-128K | Coding, benchmarks |
| **Llama 3.1** (8B) | 128K tokens | General chat |

---

## BY AGENT

### Charles (Main Agent)

Uses ONE model at a time based on task:

| Task | Model | Context Available |
|------|-------|-------------------|
| Reasoning | DeepSeek R1 | 64K |
| Coding | Qwen3 | 128K |
| General | Llama 3.1 | 128K |

Charles loads ~80 skills in system prompt = ~15K tokens max.

### Sub-Agents (Builder, Researcher, Ops)

Each loads 10-15 relevant skills only:

| Sub-Agent | Skills | Tokens Needed |
|-----------|--------|---------------|
| Builder | Code + Debug + Deploy | ~5K |
| Researcher | Research + Scrape + Analyze | ~5K |
| Ops | CRM + Tasks + Monitoring | ~5K |

Sub-agents don't need full context — just their skill definitions.

---

## Practical

| Scenario | Tokens Used | OK? |
|----------|-------------|-----|
| Charles + 80 skills + history | ~30K | ✅ under 64K |
| Builder sub-agent | ~5K | ✅ |
| DeepSeek R1 at limit | 64K max | ✅ |

No crowding issues. All models handle it.
