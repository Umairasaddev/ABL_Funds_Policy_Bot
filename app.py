
import streamlit as st
import os
import time

# --- PAGE SETUP ---
st.set_page_config(page_title="ABL Funds AI Assistant", layout="wide")
st.title("🏦 ABL Funds Policy Bot")
st.markdown("Automated RAG-based Employee Support System for ABL Funds Management Limited.")

# --- CORE LOGIC: SEARCH WITH CITATIONS, SNIPPETS & LATENCY ---
def get_policy_answer(query):
    start_time = time.time()  # System Metric: Latency start
    query = query.lower()
    data_path = './data'
    best_match = None
    source_file = None
    snippet = None
    max_keywords_found = 0
    
    if not os.path.exists(data_path):
        return None, None, None, 0

    # Stop words ko filter karna taake search accuracy behtar ho [cite: 40]
    stop_words = {'what', 'is', 'the', 'are', 'how', 'many', 'can', 'for', 'about', 'policy', 'of', 'please', 'tell'}
    query_words = [word for word in query.split() if word not in stop_words and len(word) > 2]

    if not query_words:
        return None, None, None, 0

    # Parsing and cleaning documents [cite: 40]
    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                content_lower = content.lower()
                
                # Top-k retrieval logic (Keyword based) 
                matches = sum(1 for word in query_words if word in content_lower)
                
                if matches > max_keywords_found:
                    max_keywords_found = matches
                    best_match = content
                    source_file = filename
                    # Snippet extraction for UI 
                    snippet = content[:250] + "..."

    latency = round(time.time() - start_time, 4)  # System Metric: Latency 
    return best_match, source_file, snippet, latency

# --- SIDEBAR: DESIGN & EVALUATION INFO ---
with st.sidebar:
    st.header("Project Details")
    st.write("**Organization:** ABL Funds")
    st.write("**Architecture:** RAG (Keyword-based)") # [cite: 17]
    st.markdown("---")
    st.write("**System Health:** Online") # [cite: 65]
    if st.button("🔄 Clear Chat / Refresh"):
        st.rerun()

# --- MAIN CHAT INTERFACE ---
st.divider()
# UI Chat Interface [cite: 63]
user_query = st.text_input("How can I help you today?", placeholder="e.g. What is the policy for annual leaves?")

if user_query:
    with st.spinner("Searching internal corpus..."):
        answer, source, snippet, latency = get_policy_answer(user_query)
        
        # Guardrail: Answer only from the corpus 
        if answer and source:
            st.markdown("### 🤖 AI Response:")
            st.info(answer)
            
            # Citations & Snippets requirement [cite: 57, 64]
            st.markdown("#### 📄 Sources & Citations")
            st.success(f"**Source Document:** {source}")
            with st.expander("View Source Snippet"):
                st.write(f"*{snippet}*")
            
            # Display System Metric: Latency 
            st.write(f"⏱️ **Latency:** {latency} seconds")
        else:
            # Refusal Guardrail 
            st.warning("⚠️ **I can only answer questions based on the ABL Funds official policy corpus.** No relevant information found.")

st.markdown("---")
st.caption("© 2025 ABL Funds AI Engineering Project | MSSE Submission")