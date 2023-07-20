from flask import Flask, request
import spacy
import configparser


app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Load the API key from the properties file
config = configparser.ConfigParser()
config.read('config.properties')
OPENAI_API_KEY = config.get('API_KEYS', 'openai_api_key')


@app.route('/generate-code', methods=['POST'])
def generate_code():
    prompt = request.json['user_input']

    # Code generation logic using completions API
    # Replace this with actual code generation implementation
    refined_prompt = refine_prompt(prompt)
    generated_code = get_response_from_client(refined_prompt)

    return {'code': generated_code}


def refine_prompt(user_input):
    doc = nlp(user_input)

    refined_prompt = " ".join([token.text for token in doc])

    return refined_prompt


def get_response_from_client(prompt):
    # make the actual call with http impl
    generated_code = f'Mock generated code for prompt: {prompt}'

    return generated_code


if __name__ == '__main__':
    app.run(debug=True)
