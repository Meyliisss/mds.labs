from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="tinyllama",
    messages=[
        {
            "role": "user",
            "content": "What is heavier between a kilogram of lead and a kilogram of feathers?"
        }
    ]
)

print(response.choices[0].message.content)

