from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.in_memory import InMemoryDb

# load key to env
load_dotenv()

# create session id
session_id = "session_1"

# create db
db = InMemoryDb()

# create model
llm = OpenAIChat(id="gpt-4o-mini")

# create agent
agent = Agent(
    model=llm,
    name="agent with memory",
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=3,
    db=db,
    stream=True,
    markdown=True
)

agent.print_response(input="my name is Brij Patel")

agent.print_response(input="Tell me What is my name?")


messages = agent.get_chat_history(session_id=session_id)

for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role : {role}, Message : {content}")
