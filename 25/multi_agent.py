import os
import json
import csv
from datetime import datetime
from api_key import api_key, tavily
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools.tavily_search import TavilySearchResults

os.environ["GOOGLE_API_KEY"] = api_key
os.environ["TAVILY_API_KEY"] = tavily

llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    model="gemini-2.0-flash-001",
    max_tokens=500,
    top_p=0.9,
)

def check_inventory(item, quantity, csv_file=None):
    """
    Checks the inventory for the availability and price of a specific item and quantity.

    Args:
        item (str): The name of the item to check in the inventory.
        quantity (int): The quantity of the item to check for availability.
        csv_file (str, optional): The path to the CSV file containing inventory data. Defaults to shop.csv in the same directory.

    Returns:
        str: A message indicating whether the requested item and quantity are available, the available stock, price, or an error message.

    Notes:
        - The CSV file is expected to have columns "item", "quantity", and optionally "price".
        - The function performs a case-insensitive comparison for the item name.
    """
    import os
    import csv
    if csv_file is None:
        csv_file = os.path.join(os.path.dirname(__file__), "shop.csv")
    import re
    def normalize(s):
        # Remove trailing (s), s, and non-alphabetic characters, and lowercase
        s = s.strip().lower()
        s = re.sub(r"\(s\)$", "", s)  # Remove trailing (s)
        s = re.sub(r"s$", "", s)        # Remove trailing s
        s = re.sub(r"[^a-z0-9 ]", "", s)  # Remove non-alphanumeric except space
        s = s.strip()
        return s

    try:
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            item_norm = normalize(item)
            for row in reader:
                row_item_norm = normalize(row["item"])
                if row_item_norm == item_norm:
                    try:
                        available = int(float(row["quantity"]))
                    except Exception:
                        return f"Inventory data error: quantity for {row['item']} is not a number."
                    price = row.get("price")
                    price_str = f" at ₦{price}" if price else ""
                    if available >= int(quantity):
                        return f"{row['item']} is available. Requested: {quantity}, In stock: {available}{price_str}."
                    else:
                        return f"Only {available} units of {row['item']} are available{price_str}. Requested: {quantity}."
            return f"{item.title()} is not in stock."
    except Exception as e:
        return f"Error checking inventory: {str(e)}"


def inventory_check_natural_language(input_text):
    """
    Parses a natural language input string to extract an item and its quantity, 
    and checks the inventory for the specified item and quantity.

    The function looks for patterns in the input text that specify a quantity 
    followed by an item name, optionally followed by "are" or "is" and "available". 
    If a match is found, it extracts the quantity and item name, and calls the 
    `check_inventory` function with these values. If no match is found, it 
    returns an error message.

    Args:
      input_text (str): A natural language string describing the item and quantity 
                to check in the inventory.

    Returns:
      str: The result of the `check_inventory` function if parsing is successful, 
         or an error message if parsing fails.
    """
    import re
    match = re.search(r"(\d+)\s+(.+?)\s*(?:are|is)?\s*available", input_text.lower())
    if match:
        quantity = int(match.group(1))
        item = match.group(2).strip()
        return check_inventory(item, quantity)
    else:
        return "Could not parse item and quantity from input."

inventory_tool = Tool(
    name="Inventory Checker",
    func=inventory_check_natural_language,
    description="Check if the desired quantity of an item is in stock. Input should be like: 'Check if 3 bananas are available'."
)

search_tool = TavilySearchResults(max_results=3)
nutrition_tool = Tool(
    name="Nutrition Info",
    func=lambda query: search_tool.run(f"Nutritional information of {query}"),
    description="Searches for nutrition facts of a given item."
)

conversation_agent = initialize_agent(
    tools=[],
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(memory_key="chat_history"),
    verbose=True,
)

inventory_agent = initialize_agent(
    tools=[inventory_tool],
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(memory_key="chat_history"),
    verbose=True,
)

nutrition_agent = initialize_agent(
    tools=[nutrition_tool],
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(memory_key="chat_history"),
    verbose=True,
)

def run_agents(item: str, quantity: int):
    # Conversation agent only confirms the order
    convo = f"Order confirmation: {quantity} {item}(s) requested. Please proceed to check availability and details below."
    stock_query = f"Check if {quantity} {item}(s) are available in stock."
    stock = inventory_agent.run(stock_query)
    nutrition = nutrition_agent.run(item)
    return convo, stock, nutrition