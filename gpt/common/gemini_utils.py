import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDm2TkaK1lDlnD_2Qi8J5L23K0k4Ht7lrM")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    print(question)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.replace("sql", "")
    sql_query = sql_query.replace("oracle", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip().rstrip(';')
    return sql_query

def convert_rows_to_sentences(rows, question):
    if rows == "DB_ERROR":
        return ["Please try again."]
    elif not rows:
        return ["No Record Found"]
    
    model = genai.GenerativeModel('gemini-pro')
    sentences = []
    if len(rows) == 1:
        for row in rows:
            row_text = ' '.join(map(str, row))
            prompt = f"{question} The data retrieved from the database is: {row_text}. Please generate a complete sentence."
            response = model.generate_content([prompt])
            if response:
                sentence = response.text.strip()
                sentences.append(sentence)
    else:
        sentences = rows
    return sentences
