from flask import Flask, request
import spacy


app = Flask(__name__)
nlp = spacy.load("raw_prompt")


@app.route('/generate-code', methods=['POST'])
def generate_code():
    prompt = request.json['refined_prompt']

    # Code generation logic using completions API
    # Replace this with actual code generation implementation

    generated_code = f'Generated code for prompt: {prompt}'

    return {'code': generated_code}


if __name__ == '__main__':
    app.run(debug=True)
