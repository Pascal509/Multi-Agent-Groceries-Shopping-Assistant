
import os
try:
    import streamlit as st
    # Prefer st.secrets for local .streamlit/secrets.toml and Streamlit Cloud
    api_key = st.secrets["api_key"]
    tavily = st.secrets["tavily"]
except (ImportError, AttributeError, KeyError):
    # Fallback to environment variables for local dev or other platforms
    api_key = os.environ.get("API_KEY")
    tavily = os.environ.get("TAVILY_KEY")

"""
Instructions:
1. For Streamlit Cloud: Set secrets in the app settings (Advanced settings) as:
	api_key = "your_api_key_here"
	tavily = "your_tavily_key_here"
2. For local development: Create a file .streamlit/secrets.toml (never commit this file!) with:
	api_key = "your_api_key_here"
	tavily = "your_tavily_key_here"
3. Alternatively, set environment variables before running the app:
	export API_KEY="your_api_key_here"
	export TAVILY_KEY="your_tavily_key_here"
4. Do NOT hardcode secrets in this file.
5. This file is safe to keep in the repo, but never commit actual keys or secrets.toml.
"""