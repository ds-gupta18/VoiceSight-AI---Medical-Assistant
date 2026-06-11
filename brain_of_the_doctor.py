#Step1 : Setup GROQ API key
from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2 : Concert image to required format
import base64

#image_path="acne.jpg"

def encode_image(image_path):
     image_file=open(image_path, "rb")
     return base64.b64encode(image_file.read()).decode('utf-8')

#Step3 : Setup multimodal  
from groq import Groq

query="Describe what you see in this image"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq(api_key=GROQ_API_KEY) 
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    }
                }
            ]
        }
    ]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content