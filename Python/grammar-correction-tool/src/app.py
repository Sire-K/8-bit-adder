import openai
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def paraphrase_gpt(text: str) -> str:
    if not text.strip():
        return "[No input provided]"
    
    prompt = (
        f"Paraphrase the following text in a rich, novelistic style, preserving meaning:\n\n\"{text}\""
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
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
            # Your existing grammar correction code here
            output = original  # placeholder

    # Pass the same output for highlighted_text so template can show it
    return render_template(
        'index.html', 
        original_text=original, 
        output_text=output, 
        highlighted_text=output, 
        mode=mode
    )

if __name__ == '__main__':
    app.run(debug=True)
