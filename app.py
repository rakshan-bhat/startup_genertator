from flask import Flask, render_template, request
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
groq_api_key = os.getenv("GROQ_API_KEY")

def generate_idea(prompt):
    llm = ChatGroq(
        temperature=0.7,
        model_name="qwen2-72b-instruct",
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['prompt']
        idea = generate_idea(user_input)
        return render_template('result.html', idea=idea)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
