from textblob import TextBlob
from fuzzywuzzy import process

print("Hi! I am chatbot. How can I assit you today?")

predefined_phrase= {
    "hello": "Hi there! How can I assist you today",
    "how are you": "I'm just a Program , But I functioning great!. How about you ?",
    "bye": "Goodbye! Take care!",
    "help": "Sure, I'm here to help. Ask me anything!"
}


while True:
    user_input = input("You: ").lower()
    
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a Great Day!")
        break

    closest_match, similarity = process.extractOne(user_input,predefined_phrase.keys())

    if similarity>70:
        print(f"Chatbot: {predefined_phrase[closest_match]}")
    else:
    
        blob= TextBlob(user_input)

        if blob.sentiment.polarity > 0 :
            print("Chatbot: You seem happy!")
        elif blob.sentiment.polarity < 0 :
            print("Chatbot: Oh! Why so sad")
        else :
            print("I'm here to listen. Tell me more!")
    