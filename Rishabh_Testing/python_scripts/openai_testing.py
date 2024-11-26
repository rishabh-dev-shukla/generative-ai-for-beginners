import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API key
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_key = os.getenv("OPENAI_API_KEY")

# Your prompt
prompt = "Complete the following: Once upon a time there was a girl who was brought up in a jungle"

# Create a chat completion
completion = openai.chat.completions.create(
    model="gpt-4o-mini",  # Replace with "gpt-4" if you have access
    messages=[{"role": "user", "content": prompt}]
)

# Print the response
print(completion.choices[0].message.content.strip())
