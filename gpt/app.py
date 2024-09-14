from flask import Flask, render_template, request
import subprocess
import os
from handlers.dashboard_handler import handle_template1_query
from handlers.prop_res_handler import handle_template2_query

app = Flask(__name__)

# List of general or vague keywords
general_keywords = ["hai", "hello", "hey", "how are you", "good morning", "good evening","good"]

# Predefined list of default suggested questions
suggested_questions = [
    "All Units Sold on Today?",
    "All Units Sold for Tower A?",
    "All units Sold by PHIRDOS STAR PROPERTY?",
    "Today's pre-reserved",
    "Last month's total sale value?",
]

@app.route('/dashboard_gpt', methods=['GET', 'POST'])
def template1():
    # if request.method == 'POST':
    #      question = request.form['question']
    #      sentences = handle_template1_query(question)
    #      return render_template('dashboard_gpt.html', sentences=sentences[0],columns=sentences[1])
    # return render_template('dashboard_gpt.html', sentences=[])

    sentences = []
    suggestions = []
    
    # Get the question from the form or query parameters
    question = request.args.get('question') or (request.form.get('question') if request.method == 'POST' else None)
    
    if question:
        # Detect if the question is general or vague
        if is_general_question(question):
            # Suggest default questions if the input is general
            suggestions = suggested_questions
        else:
            # Call the function to handle the query (your implementation)
            sentences = handle_template1_query(question)
    
    # Render the dashboard template, showing either sentences or suggestions
    if len(sentences) > 1 and isinstance(sentences[0], list) and isinstance(sentences[1], list):
        # If sentences[0] and sentences[1] are valid (assuming [0] is the result and [1] is the columns)
        return render_template('dashboard_gpt.html', sentences=sentences[0], columns=sentences[1], suggestions=suggestions)
    else:
        # If not valid, pass the entire sentences list and an empty column list
        return render_template('dashboard_gpt.html', sentences=sentences, columns=[], suggestions=suggestions)



def is_general_question(question):
    """Check if the question contains general keywords or is vague."""
    for keyword in general_keywords:
        if keyword.lower() in question.lower():
            return True
    return False

@app.route('/prop_res_gpt', methods=['GET', 'POST'])
def template2():
    if request.method == 'POST':
        question = request.form['question']
        sentences = handle_template1_query(question)
        return render_template('prop_res_gpt.html', sentences=sentences)
    return render_template('prop_res_gpt.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default port is 5000
    app.run(host='0.0.0.0', port=port, debug=True)  # Set debug to False for production
    # app.run(debug=True)
