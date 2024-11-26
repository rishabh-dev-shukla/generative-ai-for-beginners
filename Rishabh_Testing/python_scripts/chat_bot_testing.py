import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Set up the OpenAI API key
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_key = os.getenv("OPENAI_API_KEY")

# configure Azure OpenAI service client
# client = AzureOpenAI(
#   azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
#   api_key=os.environ['AZURE_OPENAI_API_KEY'],
#   api_version = "2023-10-01-preview"
#   )

#deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']



# Function to load the sales assistant prompt from a text file
def load_sales_prompt(file_path):
    with open(file_path, "r") as file:
        return file.read()


# Function to generate the chatbot's response using OpenAI
def generate_sales_assistant_response_azure(user_input, conversation, sales_prompt):
    prompt = f"""
    {sales_prompt}
    {conversation}
    Customer: {user_input}
    AI Sales Assistant:     
    """
    messages = [{"role": "user", "content": prompt}]
    #completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.7)

    return ""
    #return completion.choices[0].message.content.strip()


# Function to generate the chatbot's response using OpenAI
def generate_sales_assistant_response_open_ai(user_input, conversation, sales_prompt):
    messages = [
        {"role": "system", "content": sales_prompt},
        {"role": "user", "content": conversation + user_input}
    ]

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-4" if you're using GPT-4
        messages=messages,
    )

    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    # Load the Sales Assistant prompt from the text file
    sales_prompt = load_sales_prompt("C:\\Users\\shash\PycharmProjects\\generative-ai-for-beginners\\Rishabh_Testing\\text_files\\yoga_offline_prompt.txt")

    conversation = ""
    while True:
        user_input = input("Customer: ")
        conversation += f"Customer: {user_input}\n"
        bot_response = generate_sales_assistant_response_open_ai(user_input, conversation, sales_prompt)
        print(f"AI Sales Assistant: {bot_response}")
        conversation += f"AI Sales Assistant: {bot_response}\n"
