from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper

class ResearchAgent:
    def __init__(self):
        # Initialize the 'Brain'
        self.llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")
        self.search = SerpAPIWrapper()
        
    def get_tools(self):
        # Give the agent abilities (Tools)
        return [
            Tool(
                name="Current Search",
                func=self.search.run,
                description="useful for when you need to answer questions about current events or specific technical docs"
            )
        ]

    def run_mission(self, objective):
        tools = self.get_tools()
        
        # Initialize an agent that can "reason" and decide which tool to use
        agent = initialize_agent(
            tools, 
            self.llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=True
        )
        
        print(f"🤖 Agent starting mission: {objective}")
        return agent.run(objective)

if __name__ == "__main__":
    bot = ResearchAgent()
    result = bot.run_mission("Research the latest pricing model for Snowflake API in 2024")
    print(f"Final Report: {result}")
