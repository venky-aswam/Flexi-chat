import os
import sys

# Ensure the `common` directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from gemini_utils import get_gemini_response, convert_rows_to_sentences
from db_utils import read_sql_query

template_2 = """         
           table = FND_COUNTRY, fields = (COUNTRY_ID, COUNTRY_NAME, COUNTRY_TEL_CODE, COUNTRY_CODE, NATIONALITY)
           """

def handle_template2_query(question):
    response = get_gemini_response(question, template_2)
    rows = read_sql_query(response)
    sentences = convert_rows_to_sentences(rows, question)
    return sentences

