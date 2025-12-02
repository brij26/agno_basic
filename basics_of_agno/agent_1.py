from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

# load environments keys

load_dotenv()

# defining llm
llm = OpenAIChat(id="gpt-4o-mini")

# defining agent
agent = Agent(
    model=llm,
    name="my_agent",
    markdown=True,
    stream=True
)
agent.print_response(
    "Hello, my name is Brij Patel")

agent.print_response("tell me what is my name?")
