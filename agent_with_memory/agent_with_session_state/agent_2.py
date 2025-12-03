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
db = SqliteDb(db_file="shopping.db")

# define one tool that can add items to the session state


def add_items(session_state: dict, item_name: str) -> str:
    """ This function can add an item to the shopping list"""
    shopping_list = session_state['shopping_list']
    item = item_name.lower()
    if item in shopping_list:
        return f"{item} is already in shopping list"
    else:
        shopping_list.append(item)
        return f"{item} is added to the shopping list successfuly"


def remove_item(session_state: dict, item_name: str) -> str:
    """This function can remove an item from the shopping list"""
    shopping_list = session_state['shopping_list']
    item = item_name.lower()
    if item not in shopping_list:
        return f"{item} is not in shopping list"
    else:
        shopping_list.remove(item_name)
        return f"{item} is remove from successfully from the shopping list"

# define tool to read the shopping list


def read_item(session_state: dict) -> str:
    """List down all the items of the shopping list"""
    shopping_list = session_state['shopping_list']
    # check either shopping list is empty or not
    if shopping_list:
        list_of_items = "\n".join([f"- {item}" for item in shopping_list])
        return list_of_items

    else:
        return "Shopping list is empty"

# define tool to clear the shopping list


def clear_shopping_list(session_state: dict) -> str:
    """Clear the shopping list all items and gives you an empty list"""
    shopping_list = session_state['shopping_list']
    shopping_list.clear()

    return "Cleared the shopping list of all items"


# create one agent
agent = Agent(
    model=llm,
    name="agent with session state",
    db=db,
    session_id=session_id,
    user_id=user_id,
    session_state={"shopping_list": []},
    instructions="You are expert in maintaining a shpping list, and you have access of shopping list : {shopping list}",
    tools=[add_items, remove_item, read_item, clear_shopping_list],
    stream=True,
    markdown=True
)

agent.print_response(input="Add milk to the shopping list")

# print()
# state = agent.get_session_state(session_id=session_id)
# print(state['shopping_list'])


agent.print_response(input="Add eggs and bread to the shopping list")

# print()
# state = agent.get_session_state(session_id=session_id)
# print(state['shopping_list'])

agent.print_response(input="remove chocolate from the shopping list")

print()
state = agent.get_session_state(session_id=session_id)
print(state['shopping_list'])
