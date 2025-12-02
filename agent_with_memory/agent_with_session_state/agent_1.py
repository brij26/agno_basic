from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv


# load all the keys to env
load_dotenv()

# define one model
llm = OpenAIChat(id="gpt-4o-mini")

# define session id
session_id = "1"

# define user id
user_id = "User1"

# define db
db = SqliteDb(db_file="temp.db")

# define session state
user_info = {
    "name": "brij",
    "age": 21
}


# create one agent
agent = Agent(
    model=llm,
    name="agent with session state",
    db=db,
    session_id=session_id,
    user_id=user_id,
    session_state=user_info,
    add_session_state_to_context=True,
    stream=True,
    markdown=True
)


agent.print_response(input="Tell me what is my name and age?")

# getting session state from the agent
print(agent.get_session_state(session_id=session_id))
