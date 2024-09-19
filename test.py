import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        properties={
            "response": content.Schema(type=content.Type.STRING),
        },
    ),
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are an expert at teaching science to kids...",
)

history = []

print("Bot: Hello, how can I help you?")

while True:
    user_input = input("You: ")

    chat_session = model.start_chat(history=history)

    response = chat_session.send_message(user_input)

    model_response = response.text
    print(f'Bot: {model_response}\n')

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})