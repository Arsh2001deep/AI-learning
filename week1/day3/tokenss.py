import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"

# prompts
prompt1="HI"
prompt2="Explain ai and ml"
prompt3="tell differences between ai and ml within 5000 words"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
    "role": role,
    "content": prompt
    }

    messages=[message]

    response=client.chat.completions.create(model=model, messages=messages,max_tokens=50)
    usage=response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")






# print(response)

# print("#######################################")

# answer=response.choices[0].message.content
# print(answer)



# there are 3 types of token porompt token written by us , Response/completion token  written by llm, total token the addition of both