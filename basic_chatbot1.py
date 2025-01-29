import nltk
from nltk.chat.util import Chat, reflections
from googlesearch import search

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
    [r"what can you do?", ["I can have basic conversations, assist you with simple queries, or even search Google for you!"]],
    [r"search (.*)", ["Let me look that up for you..."]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm not sure I understand, but I'm here to help!"]],
]

# Function to perform a Google search
def google_search(query):
    try:
        # Perform a Google search and return the top 3 results
        results = []
        for url in search(query, num_results=3):
            results.append(url)
        return "\n".join(results)
    except Exception as e:
        return f"Sorry, I couldn't complete the search. Error: {str(e)}"

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

        # Check if the input matches a "search" query
        if user_input.startswith("search"):
            query = user_input.replace("search", "").strip()
            print("ChatBot: Let me search that for you...")
            search_results = google_search(query)
            print(f"ChatBot: Here are some links:\n{search_results}")
        else:
            response = chatbot.respond(user_input)
            print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
