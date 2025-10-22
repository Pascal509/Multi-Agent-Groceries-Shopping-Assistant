# Multi-Agent Groceries Shopping Assistant

A professional, AI-powered shopping assistant web app for grocery stores and supermarkets. Built with Python, Streamlit, and LangChain, this app enables users to check inventory, get product information, manage a shopping cart, and place orders—all with a modern, user-friendly interface.

## Features

- **Multi-Agent System:** Utilizes LLM agents for inventory checks, product info, and order confirmation.
- **Real-Time Inventory:** Reads from a CSV-based inventory and updates stock on each order.
- **Shopping Cart:** Users can add multiple items to a cart and checkout in one go.
- **Order History:** Tracks and displays past orders in a dedicated UI section.
- **Input Validation:** Ensures only valid item names and quantities are processed.
- **Nutrition & Product Info:** Fetches nutritional or general info for any item using LLM-powered search.
- **Admin-Ready:** (Planned) UI for inventory management (add/update/remove items).
- **Extensible:** Easily add new agents, data sources, or features.

## Demo

![App Screenshot](img_md/cover.jpg)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/multi-agent-groceries-shopping-assistant.git
cd multi-agent-groceries-shopping-assistant
```

### 2. Install Dependencies
Make sure you have Python 3.10+ installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a file `25/api_key.py` with your API keys:
```python
api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
tavily = "YOUR_TAVILY_API_KEY"
```

### 4. Run the App Locally
```bash
cd 25
streamlit run front_end.py
```

The app will open in your browser at `http://localhost:8501`.

## Deployment

### Streamlit Community Cloud (Recommended)
1. Push your code to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Set the main file path to `25/front_end.py`.
4. Add your API keys as secrets or in `api_key.py`.
5. Click "Deploy".

### Vercel (Advanced)
Vercel is not natively designed for Streamlit, but you can use a FastAPI/Flask wrapper if needed. See the docs for details.

## Project Structure

```
25/
  front_end.py         # Streamlit UI
  multi_agent.py       # Agent logic and inventory/order management
  shop.csv             # Inventory data
  api_key.py           # API keys (not committed)
img_md/                # App images
requirements.txt       # Python dependencies
README.md              # This file
```

## Technologies Used
- Python 3.10+
- Streamlit
- LangChain
- Google Gemini API
- Tavily API
- Pandas

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License. See `LICENSE` file for details.

## Authors
- Pascal509 (repo owner)
- [Your Name] (contributor)

---

For questions or support, please open an issue on GitHub.
