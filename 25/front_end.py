
import streamlit as st
from multi_agent import run_agents

st.set_page_config(page_title="Multi-Agent Shop Assistant", layout="centered")

st.title("🛒 Multi-Agent Shopping Assistant")
st.write("This app checks item availability and nutritional info using multiple AI agents.")

def is_valid_item(item):
    return bool(item and item.strip())

def is_valid_quantity(quantity):
    try:
        return int(quantity) > 0
    except Exception:
        return False

error_message = None

with st.form("purchase_form"):
    item = st.text_input("Enter item name", value="banana")
    quantity = st.number_input("Enter quantity", min_value=1, value=1)
    submitted = st.form_submit_button("Check Item")

if submitted:
    if not is_valid_item(item):
        error_message = "Please enter a valid item name."
    elif not is_valid_quantity(quantity):
        error_message = "Please enter a valid quantity (greater than 0)."

    if error_message:
        st.error(error_message)
    else:
        with st.spinner("🤖 Agents are working..."):
            convo, stock, nutrition = run_agents(item, quantity)

        st.subheader("🧠 User Intent (Conversation Agent)")
        st.info(convo)

        st.subheader("📦 Inventory Check (Inventory Agent)")
        if "not in stock" in stock.lower() or "error" in stock.lower() or "could not parse" in stock.lower():
            st.error(stock)
        else:
            st.success(stock)

        st.subheader("🥗 Nutrition Facts (Nutrition Agent)")
        st.write(nutrition)
