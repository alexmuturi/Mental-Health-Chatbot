import streamlit as st
import joblib
import random
import time

# Streamlit app title
st.title("Saidika")

#Load the chatbot model
model = joblib.load('model/SVC_model.pkl')

#Load the vectorizer
vectorizer = joblib.load('model/vectorizer.pkl')

# Function to predict intents based on user input

def predict_intent(user_input):
    # Vectorize the user input
    user_input_vec = vectorizer.transform([user_input])

    # Predict the intent
    intent = model.predict(user_input_vec)[0]

    return intent

# Function to generate responses based on predicted intents
def generate_response(intent):
    # Implement your logic here to generate appropriate responses based on the predicted intents
    if intent == 'alcoholism':
        response = "I am sorry for what you are going through. Dealing with alcoholism can be a big challenge for everyone. However, you can always get help to get out of the addiction. Do you mind sharing with me what kind of help you would want?"
    elif intent == 'diagnosedPTSD':
        response = "Goodbye! Take care."
    elif intent == 'socialanxiety':
        response = "I'm sorry, I don't have the information you're looking for."
    else:
        response = "I'm here to help. Please let me know how I can assist you."

    return response



# Set a default model
if "svc_model" not in st.session_state:
    st.session_state["svc_model"] = model



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.text_input("You:"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Predict intent based on user input
    intent = predict_intent(prompt)
    # Generate response based on predicted intent
    response = generate_response(intent)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add user and assistant messages to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})



