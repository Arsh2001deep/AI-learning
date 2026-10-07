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
prompt="give me a cool food app name "

# system
message_system={
    "role": "system",
    "content":"You are a creative brand designer give me one brand name only"
}



# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]


# temperature

response=client.chat.completions.create(model=model, messages=messages, temperature=2)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)