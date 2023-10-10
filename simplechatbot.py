import re
import random

# Define a dictionary of predefined rules and chatbotresponses
chatbotresponses = {
    r"(hello|hi|hey).*": ["Hello! How can I assist you today?", "Hi there!", "Hey! What can I do for you?"],
    r"(how are you).*": ["I'm just a computer program, but I'm here to help!", "I'm doing well, thank you for asking!"],
    r"(what is your name|who are you).*": ["I'm a chatbot created to assist you with information and tasks.", "I go by the name Chatbot."],
    r"(bye|goodbye).*": ["Goodbye! Have a great day!", "See you later!"],
    r"(help|what can you do).*": ["I can provide information on a wide range of topics. Try asking me something!", "I can answer questions and assist with tasks. Just let me know what you need."],
    r"(tell me a joke).*": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's one: What did one ocean say to the other ocean? Nothing, they just waved."],
    r"(weather|forecast).*": ["I can help you find the weather. Please provide me with your location.", "Sure, I can check the weather for you. Where are you located?"],
    r"(.*)(thanks|thank you).*": ["You're welcome! If you have any more questions, feel free to ask.", "No problem! If you need assistance in the future, don't hesitate to reach out."],
    r"(.*)(your favorite|best|top).*": ["I don't have favorites, but I can provide information on various topics. What are you interested in?"],
    r"(.*)(love you|awesome|amazing).*": ["Thank you! I'm here to assist you to the best of my abilities.", "I appreciate the compliment! How can I assist you today?"],
}

# Function to respond to user input
def respondtouser(user_input):
    for pattern, response_list in chatbotresponses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return random.choice(response_list)
    return "I'm sorry, I don't understand that."

# Main loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    chatbotresponse = respondtouser(user_input)
    print("Chatbot:", chatbotresponse)
