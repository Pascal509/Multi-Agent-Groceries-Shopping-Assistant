# Multi-Agent Groceries Shopping Assistant

An AI-powered groceries shopping assistant built with Streamlit, LangChain, and Google Gemini. This app helps users check inventory, retrieve nutritional information, and manage orders in real time using multiple intelligent agents.

## Features
- Multi-agent orchestration with LangChain
- Real-time inventory checking
- Nutrition information retrieval
- User-friendly Streamlit UI
- Robust input validation and error handling
- Session management for cart and orders
- Admin inventory management UI
- Secure API key handling
- Cloud deployment ready (Streamlit Cloud)

## Getting Started

### Prerequisites
- Python 3.10+
- Streamlit Cloud or local Python environment

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pascal509/Multi-Agent-Groceries-Shopping-Assistant.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API keys to `api_key.py` (see below for security).

### Running the App
```bash
streamlit run front_end.py
```

## Project Structure
```
GDG-build-with-ai/
├── 25/
│   ├── api-key.py           # API keys (should not be uploaded)
│   ├── build_with_ai_abj_Road2DevFest25.ipynb
│   ├── front_end.py         # Streamlit UI
│   ├── MultiAgent.ipynb
│   ├── multi_agent.py       # Main agent logic
│   ├── shop.csv             # Inventory data
├── img_md/                  # Images for UI
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

## In-Code Documentation

### `multi_agent.py`
```python
"""
Multi-Agent Groceries Shopping Assistant

This module orchestrates multiple AI agents to handle inventory checking, nutrition info retrieval, and order confirmation for a groceries shopping assistant app.

- Uses LangChain for agent management
- Integrates Google Gemini and Tavily APIs
- Handles input validation, error handling, and session state
"""
# ...existing code...
```

### `front_end.py`
```python
"""
Streamlit Frontend for Groceries Shopping Assistant

- Renders UI for users and admins
- Handles user input, cart management, and order history
- Displays inventory and nutrition info
"""
# ...existing code...
```

## Security & .gitignore
- **Never upload `api_key.py` or files containing secrets to GitHub.**
- Use environment variables or Streamlit secrets for production.

## License
MIT

## Author
Pascal509

---
For questions or contributions, open an issue or pull request on GitHub.
