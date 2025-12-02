from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

# loading all key to env
load_dotenv()

# define one model
llm = OpenAIChat(id="gpt-4o-mini")

# create one user_id
user_id = "user_1"

# Create one db
db = SqliteDb(db_file="chat_history_db/demo.db")

# Define agent
agent = Agent(
    model=llm,
    name="Agent with multiple sessions",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    stream=True,
    markdown=True,
)

# Create sessions
session_transformer = "session_transformer"
session_rag = "session_rag"

# now conversation 1 --> session_id = session_transformer
agent.print_response(
    input="Explain the transformer architecture to me in 100 words", session_id=session_transformer)
agent.print_response(
    input="Tell me what is self attention mechanism, tell me in one paragraph only", session_id=session_transformer)
agent.print_response(
    input="Tell me what is this all conversation all about?", session_id=session_transformer)


# now conversation 2 --> session_id = session_rag

agent.print_response(
    input="What is Rag all about, explain it me in 50 words", session_id=session_rag)
agent.print_response(
    input="When can we use rag in our application, make reponser short and precise", session_id=session_rag)
agent.print_response(
    input="what is this conversation all about?", session_id=session_rag)


print()
print()
print()

print("============================= Trnasformer conversation =========================================")
messages = agent.get_chat_history(session_id=session_transformer)
for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role : {role}, message : {content}")

print()
print()
print()

print("============================= RAG conversation =========================================")
messages = agent.get_chat_history(session_id=session_rag)
for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role : {role}, message : {content}")
