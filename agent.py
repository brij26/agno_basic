from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

# load all the keys to env
load_dotenv()

# define model for our agent
llm = OpenAIChat(id="gpt-4o-mini")

# define db for our agent
db = SqliteDb(db_file="chat_history.db")

# define user id
user_id = "User1"

# create one session
session_id = "session_1"

# create agent
agent = Agent(
    model=llm,
    name="agent with memory",
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    session_id=session_id,
    user_id=user_id,
    stream=True,
    markdown=True
)

# do some conversation over here
agent.print_response(input="My name is Brij Patel")
agent.print_response(input="Tell me what is my name?")


# access the message from the db
messages = agent.get_chat_history(session_id=session_id)

for message in messages:
    role, content = message.role, message.content
    print(f"Role : {role}, /n Message : {content}")
