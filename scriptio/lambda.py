import json
import requests

# Define the OpenAI API key
OPENAI_API_KEY = "openai-key"


def lambda_handler(event, context):
    if event['httpMethod'] == 'OPTIONS':
        # For the preflight: OPTIONS request, return CORS headers
        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                'Access-Control-Allow-Headers': '*',
            },
        }
        return response
    else:
        try:
            action = event.get("action").lower()
            content = ""
            # Call the OpenAI API with the provided event
            if action == "generatecode":
                content = f"Generate {event['language']} code: " \
                          f"{event['request']['messages'][0]['content']}"
            elif action == "analysecode":
                content = f"Analyse {event['language']} code: " \
                          f"{event['request']['messages'][0]['content']}"
            elif action == "generatetest":
                content = f"Generate {event['language']} " \
                          f"tests with {event['package']}: " \
                          f"{event['request']['messages'][0]['content']}"
            print("Content: ", content)
            # Modify the request to include the updated content string
            event['request']['messages'][0]['content'] = content
            generated_code = call_openai_api(event['request'], OPENAI_API_KEY)

            # Return the generated code in the response
            return {
                'statusCode': 200,
                'body': generated_code
            }
        except Exception as e:
            print("Error: ", str(e))
            # Handle the error and return an appropriate response
            return {
                'statusCode': 500,
                'headers': {
                    "Content-Type": "application/json"
                },
                'body': json.dumps({'error': str(e)})
            }


def call_openai_api(request_body, api_key):
    try:
        # Set the headers for the API call
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        # Make the API call to OpenAI
        response = requests.post('https://api.openai.com/v1/chat/completions',
                                 headers=headers, json=request_body)
        response.raise_for_status()  # Raise an exception if the API call fails

        response_data = response.json()

        # Extract the generated message from the model response
        generated_code = response_data['choices'][0]['message']['content']
        return generated_code
    except Exception as e:
        print("Error calling OpenAI API: ", str(e))
        raise e
