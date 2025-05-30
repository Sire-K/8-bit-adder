import openai
import os
from flask import Flask, render_template, request
from grammar import highlight_differences  # <-- Add this import

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def paraphrase_gpt(text: str) -> str:
    if not text.strip():
        return "[No input provided]"
    
    prompt = (
        f"Paraphrase the following text in a rich, novelistic style, preserving meaning:\n\n\"{text}\""
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant skilled in literary paraphrasing."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error during paraphrasing: {e}]"

def grammar_correct_gpt(text: str) -> str:
    if not text.strip():
        return "[No input provided]"
    
    prompt = (
        f"Correct the grammar, spelling, and punctuation of the following text. "
        f"Return only the corrected version:\n\n\"{text}\""
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant skilled in grammar correction."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error during grammar correction: {e}]"

@app.route('/', methods=['GET', 'POST'])
def index():
    original = ''
    output = ''
    mode = 'grammar'

    if request.method == 'POST':
        original = request.form.get('text_input', '')
        mode = request.form.get('mode', 'grammar')

        if mode == 'novelistic':
            output = paraphrase_gpt(original)
        else:
            output = grammar_correct_gpt(original)

    return render_template(
        'index.html', 
        original_text=original, 
        output_text=output, 
        highlighted_text=highlight_differences(original, output) if original and output else '',  # <-- Use highlighting
        mode=mode
    )

if __name__ == '__main__':
    app.run(debug=True)
