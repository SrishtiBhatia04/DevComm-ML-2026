# Task 2 - AI Chatbot with Image Support

## Overview

This task focuses on building an interactive AI chatbot application using a web-based interface. The application allows users to engage in text-based conversations while also supporting image uploads for basic visual analysis.

The goal of this task was to integrate language and vision capabilities into a single interface and demonstrate how different models can be used for different types of inputs.

---

## Technologies Used

The application was built using the following tools and libraries:

- Streamlit → for creating the web interface  
- Ollama → for running local AI models  
- PIL (Python Imaging Library) → for handling image uploads and display  

---

## Models Used

### Llama 3

Used for handling text-based conversations. It processes user input and generates responses while maintaining conversation history.

### LLaVA

Used for image analysis. It takes an uploaded image and generates a descriptive response based on its contents.

---

## Features Implemented

The application includes the following functionality:

- A Streamlit-based user interface for interaction  
- Text-based chatbot with maintained conversation history  
- Image upload support for JPG, JPEG, and PNG formats  
- Image display within the interface  
- Image analysis using a vision-language model  
- Separate handling of text and image inputs within the same app  

---

## Application Flow

The application first initializes a chat interface and stores conversation history using Streamlit session state.

When a user enters text input, it is sent to the Llama 3 model, and the response is generated while preserving the conversation context.

When an image is uploaded, it is displayed in the interface and temporarily saved. The image is then passed to the LLaVA model, which generates a description of the image.

Both functionalities are handled within the same interface, allowing the user to switch between text interaction and image-based analysis seamlessly.

---

## Summary

This task demonstrates the integration of multiple AI capabilities within a single application. By combining conversational AI with image understanding, the project showcases how different models can be used together to create a more interactive and versatile user experience.
