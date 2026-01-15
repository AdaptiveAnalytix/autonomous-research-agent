# Autonomous Research Agent 🕵️

![LangChain](https://img.shields.io/badge/langchain-agents-green.svg)
![AI](https://img.shields.io/badge/GenAI-Autonomous-purple.svg)

## 🧠 Concept
This repository demonstrates an **Autonomous Agent** architecture. Unlike standard chatbots, this system utilizes the **ReAct (Reasoning + Acting)** framework. It can formulate a plan, use external tools (Google Search API), and synthesize findings without human intervention.

## ⚙️ How it Works
1.  **Goal Setting**: User inputs a complex objective (e.g., "Analyze competitor pricing").
2.  **Tool Selection**: The LLM decides if it needs to search the web or calculate data.
3.  **Loop**: It iterates through `Thought` -> `Action` -> `Observation` cycles.
4.  **Result**: Returns a synthesized report.

## 🛠 Dependencies
* Python 3.10+
* LangChain
* OpenAI API
* SerpAPI (for web search capability)
