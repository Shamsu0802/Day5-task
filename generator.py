import os
from openai import OpenAI
from dotenv import load_dotenv

from prompts import get_rag_prompt

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_answer(question, retrieved_docs):

    context = "\n\n".join(
        [doc["content"] for doc in retrieved_docs]
    )

    prompt = get_rag_prompt(question, context)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content