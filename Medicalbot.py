from openai import OpenAI

# Initialize client with Groq's API
client = OpenAI(
    api_key="Your_api_key", 
    base_url="https://api.groq.com/openai/v1"
)

print("Medical Bot: Hello! Ask me any medical-related question. Type 'quit' to exit.")

# Start chat loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Medical Bot: Goodbye! Stay healthy.")
        break

    # Generate response from LLaMA 3 model via Groq
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and accurate medical assistant. Only provide factual and medically-relevant responses."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        # Print the bot's response
        print("Medical Bot:", response.choices[0].message.content.strip())
    
    except Exception as e:
        print("Medical Bot: Sorry, something went wrong.", str(e))
