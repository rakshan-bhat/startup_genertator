from flask import Flask, render_template, request
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
groq_api_key = os.getenv("GROQ_API_KEY")

def generate_idea(prompt):
    try:
        llm = ChatGroq(
            temperature=0.7,
            model_name="llama-3.3-70b-versatile",
            api_key=groq_api_key
        )
        
        response = llm.invoke(f"""
        Generate a detailed startup idea based on: {prompt}
        Include:
        - Problem statement
        - Solution description
        - Target market
        - Revenue model
        - Competitive advantage
        """)
        
        return response.content
    except Exception as e:
        return f"Sorry, there was an error generating your idea: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['prompt']
        idea = generate_idea(user_input)
        return render_template('result.html', idea=idea)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
