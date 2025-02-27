# Basic-Chatbot
import nltk
from nltk.chat.util import Chat, reflections

# Download nltk data (only required the first time)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]],
    [r"what is your name?", ["I am a chatbot. You can call me ChatBot.", "I am ChatBot, your virtual assistant!"]],
    [r"how (.*) weather (.*)", [
        "I'm not sure, but you can check a weather app for accurate updates.",
        "Weather depends on your location. Is it sunny where you are?"
    ]],
    [r"tell me a joke", [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]],
    [r"how are you?", ["I'm just a program, but I'm here to assist you!", "I'm functioning as expected!"]],
    [r"what can you do?", ["I can have basic conversations and assist you with simple queries."]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm not sure I understand, but I'm here to help!"]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
