import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-2"
)

def generate_ai_proposal(org_name, mission):

    prompt = f"""
You are an expert nonprofit grant writer.

Organization:
{org_name}

Mission:
{mission}

Write a professional grant proposal including:

1. Executive Summary
2. Organization Overview
3. Problem Statement
4. Project Goals
5. Expected Outcomes
6. Funding Request
7. Conclusion
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = client.invoke_model(
        modelId="anthropic.claude-sonnet-4-20250514-v1:0",
        body=json.dumps(body)
    )

    result = json.loads(
        response["body"].read()
    )

    return result["content"][0]["text"]