import streamlit as st
from anthropic import Anthropic

# --- Page Config ---
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background-color: #0d0d0d;
        color: #f0f0f0;
    }

    h1 {
        font-family: 'Space Mono', monospace !important;
        color: #00ff88 !important;
        letter-spacing: -1px;
    }

    .stChatMessage {
        background-color: #1a1a1a !important;
        border-radius: 12px !important;
        border: 1px solid #2a2a2a !important;
        margin-bottom: 8px !important;
    }

    .stChatInputContainer {
        border-top: 1px solid #2a2a2a;
        padding-top: 12px;
    }

    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #f0f0f0 !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 8px !important;
    }

    .stButton > button {
        background-color: #00ff88 !important;
        color: #0d0d0d !important;
        font-family: 'Space Mono', monospace !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
    }

    .stSidebar {
        background-color: #111111 !important;
    }

    code {
        color: #00ff88 !important;
    }

    .subtitle {
        font-family: 'Inter', sans-serif;
        color: #888;
        font-size: 14px;
        margin-top: -15px;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# --- Init Client ---
client = Anthropic()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful, friendly, and smart AI assistant. Answer clearly and concisely."

# --- Sidebar ---
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    st.markdown("---")

    system_prompt = st.text_area(
        "System Prompt",
        value=st.session_state.system_prompt,
        height=150,
        help="Customize the AI's personality and behavior."
    )
    st.session_state.system_prompt = system_prompt

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("**Model:** `claude-sonnet-4-20250514`")
    st.markdown("**Messages:** " + str(len(st.session_state.messages)))

# --- Header ---
st.title("🤖 AI Chatbot")
st.markdown('<p class="subtitle">Powered by Claude · Built with Streamlit</p>', unsafe_allow_html=True)

# --- Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system=st.session_state.system_prompt,
                messages=st.session_state.messages
            )
            reply = response.content[0].text
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
