from openai import OpenAI

api_key = ''

def main():
    # Initialize client (API key must be set as environment variable: OPENAI_API_KEY)
    client = OpenAI(api_key=api_key)

    while True:
        user_input = input("Ask a question (or type 'exit' to quit): ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # or another available model
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        print(f"\nAI: {answer}\n")

if __name__ == "__main__":
    main()
