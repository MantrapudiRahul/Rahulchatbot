import pyttsx3
engine = pyttsx3.init()
import os
import google.generativeai as genai
# Configure the API key
genai.configure(api_key="AIzaSyCXZb0F-uArxYtai5MX0czreCBszDJc4cQ")
# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
while True:
    # Get input from the user
    user_input = input("You: ")
    # Check if the user wants to exit
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat.")
        break
    # Send the user input to the model and get a response
    response = chat_session.send_message(user_input)
    # Print the model's response
    print("AI:", response.text)
    engine.say(response.text)
    engine.runAndWait()