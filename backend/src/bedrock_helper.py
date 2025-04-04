import boto3
import json
import os
from typing import Dict, Any
from dotenv import load_dotenv
from pathlib import Path
from botocore.exceptions import ClientError
from config import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, BEDROCK_CHAT_MODEL_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

class BedrockHelper:
    def __init__(self):
        self.client = boto3.client(
            'bedrock-runtime',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

    def generate_response(self, context: str, question: str) -> str:
        """Generate response using Claude model."""
        prompt = USER_PROMPT_TEMPLATE.format(context=context, question=question)
        
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [
                {
                    "role": "user",
                    "content": f"{SYSTEM_PROMPT}\n\n{prompt}"
                }
            ],
            "temperature": 0.7,
            "top_p": 0.9
        }
        
        try:
            response = self.client.invoke_model(
                modelId=BEDROCK_CHAT_MODEL_ID,
                body=json.dumps(request_body)
            )
            
            response_body = json.loads(response.get('body').read())
            return response_body.get('content')[0].get('text')
        except Exception as e:
            print(f"\nError generating response: {str(e)}")
            print("Please check if you have access to the chat model.")
            return "I apologize, but I'm unable to generate a response at this time. Please check your AWS Bedrock access and permissions." 
