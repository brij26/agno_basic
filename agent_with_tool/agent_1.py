from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

# load all the keys to the env
load_dotenv()

# add duckduckgo tool
web_search = DuckDuckGoTools()

# define model
llm = OpenAIChat(id="gpt-4o-mini")

# define agent
agent = Agent(
    model=llm,
    name="agent with tool",
    tools=[web_search],
    instructions="you are expert in searching web. you have access to web search tool to get the latest information",
    stream=True,
    markdown=True
)

agent.print_response(input="What is today's top news")
