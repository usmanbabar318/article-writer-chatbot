import streamlit as st
import requests

st.set_page_config(page_title="Article Writer Bot", layout="wide")
st.title("🧠 SEO Health Article Writer Chatbot")

st.markdown("""
Enter your topic instructions below (e.g., write 1500-word SEO article on 'How to stop hair loss in men naturally' etc.)
""")

user_prompt = st.text_area("✍️ Your Instructions", height=300)

if st.button("📝 Generate Article"):
    with st.spinner("Generating article..."):
        headers = {
            "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mistral:instruct",  # You can change to other models like meta-llama/llama-3-8b-instruct
            "messages": [{"role": "user", "content": user_prompt}]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        try:
            content = result['choices'][0]['message']['content']
            st.markdown("### ✅ Generated Article")
            st.markdown(content)
            st.download_button("💾 Download as HTML", content, file_name="article.html")
        except Exception as e:
            st.error("Something went wrong! Please check your API key or try again.")
