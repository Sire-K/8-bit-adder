# Grammar Correction Tool

This project is a simple web application built using Flask that provides grammar correction functionality. It utilizes the `language_tool_python` library to analyze and correct text input by users.

## Project Structure

```
grammar-correction-tool
├── src
│   ├── app.py          # Main application logic
│   └── grammar.py      # Additional grammar-related functions
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd grammar-correction-tool
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```
   python src/app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

3. **Input your text:**
   Enter the text you want to check for grammar corrections and submit the form.

4. **View corrections:**
   The application will display the corrected text along with highlighted differences.

## Future Enhancements

- Implement user authentication for saving corrections.
- Add support for multiple languages.
- Enhance the UI for better user experience.

## License

This project is licensed under the MIT License.