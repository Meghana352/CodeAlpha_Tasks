# Function to generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot."
    else:
        return "Sorry, I don't understand that."

# Main chatbot loop
print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("🤖 Chatbot:", response)

    if user_input.lower() == "bye":
        break