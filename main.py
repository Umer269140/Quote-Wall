from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_cors import CORS


client = OpenAI()
app = Flask(__name__)
CORS(app)


@app.route('/api/generate_quote', methods=['POST'])
def generate_quote():
    data = request.get_json()
    feeling = data.get('feeling')



 
    Instruction = """
       You are AI assistant for QuoteWall and your job is to generate quotes.
       You need to follow the following rules strictly:
       1. The quote must be unique every time, quote must not be repeated.
       2. The quote must be based on the feeling provided by the user.
       3. After generating the quote, you must provide the name of the author.
       4. After the author's name, add a short description of the author in 1-2 lines.
       5. The quote must be in the following format:
         "Quote" - Author Name, Short description of the author
       6. Make sure that you follow all the rules and specially rule number 1.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": Instruction},
            {"role": "user", "content": f"Generate a quote with the name of the author based on the feeling: {feeling}"}
        ]
    )
    print(response.choices[0].message.content.strip())
    return jsonify({"quote": response.choices[0].message.content.strip()})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001)
