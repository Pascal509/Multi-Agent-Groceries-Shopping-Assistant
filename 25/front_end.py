
import streamlit as st
from multi_agent import run_agents, check_inventory


# --- Streamlit App Setup ---

st.set_page_config(page_title="Multi-Agent Shop Assistant", layout="centered")
st.title("🛒 Multi-Agent Shopping Assistant")
st.write("This app checks item availability and nutritional info using multiple AI agents.")

# --- Sidebar Toggle ---
sidebar_option = st.sidebar.radio(
    "Navigation",
    ("Shop", "Cart", "Last Order", "Order History"),
    index=0
)

# --- Session State for Cart and Orders ---
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'order_history' not in st.session_state:
    st.session_state.order_history = []
if 'last_order' not in st.session_state:
    st.session_state.last_order = None


# --- Main Area Content Based on Sidebar ---
if sidebar_option == "Shop":
    # Step 1: User checks item (runs agents)
    with st.form("check_item_form"):
        item = st.text_input("Enter item name", value="banana")
        quantity = st.number_input("Enter quantity", min_value=1, value=1)
        check_item = st.form_submit_button("Check Item")

    # Store last checked item/quantity/results in session
    if 'last_checked' not in st.session_state:
        st.session_state.last_checked = None

    if check_item:
        with st.spinner("🤖 Agents are working..."):
            convo, stock, nutrition = run_agents(item, quantity)
        st.session_state.last_checked = {
            'item': item,
            'quantity': int(quantity),
            'convo': convo,
            'stock': stock,
            'nutrition': nutrition
        }


    # Show results if available
    if st.session_state.last_checked:
        checked = st.session_state.last_checked
        st.subheader("🧠 User Intent (Conversation Agent)")
        st.info(checked['convo'])
        st.subheader("📦 Inventory Check (Inventory Agent)")
        st.success(checked['stock'])
        st.subheader("🥗 Nutrition Facts (Nutrition Agent)")
        st.write(checked['nutrition'])

elif sidebar_option == "Cart":
    st.subheader("🛒 Your Cart")
    if st.session_state.cart:
        for i, entry in enumerate(st.session_state.cart):
            st.write(f"{entry['quantity']} x {entry['item']}")
        if st.button("Checkout"):
            order_results = []
            for entry in st.session_state.cart:
                convo, stock, nutrition = run_agents(entry['item'], entry['quantity'])
                if "is available" in stock:
                    st.session_state.order_history.append({
                        'item': entry['item'],
                        'quantity': entry['quantity'],
                        'status': 'Ordered',
                        'confirmation': convo,
                        'stock': stock
                    })
                    order_results.append((convo, stock))
                else:
                    order_results.append((convo, stock))
                    st.session_state.order_history.append({
                        'item': entry['item'],
                        'quantity': entry['quantity'],
                        'status': 'Failed',
                        'confirmation': convo,
                        'stock': stock
                    })
            st.session_state.last_order = order_results
            st.session_state.cart = []
            st.success("Order placed! See details below.")
    else:
        st.info("Your cart is empty.")

elif sidebar_option == "Last Order":
    st.subheader("🧾 Last Order Details")
    if st.session_state.last_order:
        for i, (convo, stock) in enumerate(st.session_state.last_order):
            st.markdown(f"**Item {i+1}:**")
            st.info(convo)
            st.success(stock)
    else:
        st.info("No orders placed yet.")

elif sidebar_option == "Order History":
    st.subheader("📜 Order History")
    if st.session_state.order_history:
        for i, order in enumerate(st.session_state.order_history[::-1]):
            st.markdown(f"**{order['item']} x {order['quantity']}** - {order['status']}")
            st.caption(order['stock'])
    else:
        st.info("No order history yet.")
