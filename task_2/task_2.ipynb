import streamlit as st
import ollama
from PIL import Image

st.title("AI Chatbot with Image Support 🤖🖼️")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Text input
user_input = st.text_input("You:")

# Image uploader
uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)

# Show uploaded image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Save temp image
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_image.getbuffer())

    # Run image model
    response = ollama.chat(
        model="llava",
        messages=[{
            "role": "user",
            "content": "Describe this image",
            "images": ["temp.jpg"]
        }]
    )

    st.write("🖼️ Image Analysis:")
    st.write(response["message"]["content"])


# Handle text chat
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=st.session_state.messages
    )

    bot_reply = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Show chat history
for msg in st.session_state.messages:
    st.write(f"**{msg['role']}**: {msg['content']}")
