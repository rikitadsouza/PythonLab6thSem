import random

def simple_chatbot(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "what's your name": "I don't have a name, but you can call me Chatbot.",
        "bye": "Goodbye! If you have more questions, feel free to ask.",
        "tell me a joke": "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
        "favorite color": "I don't have a favorite color, but I like the sound of hexadecimal #00FF00.",
        "who created you": "I was created by a team of developers using Python and the GPT-3.5 model.",
        "how old are you": "I don't have an age, as I am just a program running on a computer.",
        "what is the meaning of life": "The meaning of life is a philosophical question. I'm just a chatbot!",
        "what can you do": "I can answer questions, tell jokes, and engage in simple conversations. Ask me anything!",
    }
    user_input_lower = user_input.lower()
    if user_input_lower in responses:
        return responses[user_input_lower]
    else:
        return "I'm not sure how to respond to that. Feel free to ask me something else!"

def main():
    print("Hello! I'm a simple chatbot. You can start a conversation with me or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            response = simple_chatbot(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()