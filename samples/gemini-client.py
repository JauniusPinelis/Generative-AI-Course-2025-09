import google.generativeai as genai

api_key = ''

def main():
    # Configure the API key
    genai.configure(api_key=api_key)
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print("Google AI Studio (Gemini) Chat Client")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        try:
            # Generate response
            response = model.generate_content(user_input)
            
            # Print the AI response
            print(f"\nAI: {response.text}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
