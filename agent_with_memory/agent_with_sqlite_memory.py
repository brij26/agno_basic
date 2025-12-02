from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb


# load the key to env
load_dotenv()

# create a model
llm = OpenAIChat(id="gpt-4o-mini")

# create one session_id
session_id = "session_1"

# create memory
db = SqliteDb(db_file="chat_history_db/demo.db")
# create the agent with memory
agent = Agent(
    model=llm,
    name="Agent with sqlite db as memory",
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=3,
    db=db,
    stream=True,
    markdown=True
)

# agent.print_response(input="My name is Brij Patel")

# agent.print_response(input="Tell me What is my name?")


messages = agent.get_chat_history(session_id=session_id)

for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role : {role}, Message : {content}")
