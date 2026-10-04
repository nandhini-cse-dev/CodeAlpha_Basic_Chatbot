# Basic Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hello! 👋 How can I help you?"

    elif user_input == "how are you":
        return "I'm doing great! 😊 Thanks for asking."

    elif user_input == "what can you do":
        return "I can respond to simple questions and have a basic conversation."
    elif user_input == "what is your name":
        return "I'm CodeBot, a simple Python-based chatbot! 🤖"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I don't understand that. 🤔"


# Start the chatbot
print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to exit the chatbot.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye" or user_input.lower() == "goodbye":
        break

print("👋 Chatbot ended. Thank you!")
