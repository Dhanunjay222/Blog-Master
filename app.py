import streamlit as st
import google.generativeai as genai
import random
import os
import time

# ✅ Get API key from environment (SAFE)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found! Please add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# ✅ Use FREE model (important)
model = genai.GenerativeModel("gemini-1.5-flash")

# Joke function
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because he used up all his cache!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why don't programmers like nature? It has too many bugs.",
    ]
    return random.choice(jokes)

# Generate blog
def generate_blog(topic, words):
    st.write("### ⏳ Generating Your Blog...")
    st.write(f"🤖 Joke: **{get_joke()}**")

    prompt = f"Write a blog about '{topic}' in {words} words."

    try:
        time.sleep(2)  # prevent rate limit
        response = model.generate_content(prompt)

        if response and response.text:
            st.success("🎉 Blog Ready!")
            return response.text
        else:
            return "No content generated."

    except Exception as e:
        st.error(f"❌ Error: {e}")
        return None

# UI
def main():
    st.title("📖 BlogMaster: AI Blog Generator")

    # Optional image
    try:
        st.image("edited_blog_master.jpg", use_container_width=True)
    except:
        pass

    topic = st.text_input("Enter blog topic:")
    words = st.number_input("Word count", 100, 5000, 500)

    if st.button("Generate Blog"):
        if topic:
            blog = generate_blog(topic, words)
            if blog:
                st.write(blog)
        else:
            st.warning("Please enter a topic")

if __name__ == "__main__":
    main()
