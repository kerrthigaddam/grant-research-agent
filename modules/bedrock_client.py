import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-2"
)

def generate_ai_proposal(org_name, mission):

    prompt = f"""
You are a nonprofit grant writing expert.

Organization:
{org_name}

Mission:
{mission}

Write a professional grant proposal including:

1. Executive Summary
2. Organization Overview
3. Need Statement
4. Project Goals
5. Expected Impact
"""

    response = client.invoke_model(
        modelId="anthropic.claude-sonnet-4-20250514-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    )

    result = json.loads(
        response["body"].read()
    )

    return result["content"][0]["text"]