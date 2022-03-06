from flask import Flask, request, make_response, redirect
import correct_functions
import json


def check_word(word):
    return correct_functions.check_word(word)


app = Flask(__name__,
            static_url_path='',
            static_folder='web')


@app.route('/')
def home():
    return redirect('/spellchecker.html')


@app.route('/api/check', methods=['GET'])
def api_check():
    print("input = ", str(request.args))
    w = request.args['word']
    print("Input word = ", w)

    result = check_word(w)

    print("check_word rsp = ", result)

    if result is True:
        rsp = json.dumps({"status": "CORRECT"})
        response = make_response(rsp)
    else:
        rsp = json.dumps({"status": "INCORRECT", "original": w, "suggestions": result})
        print("rsp = ", rsp)
        response = make_response(rsp)

    response.headers['Content-Type'] = 'application/json'

    return response


@app.route('/api/correct', methods=['POST'])
def api_correct():

    rsp = {"msg": ""}
    bar = json.dumps(rsp)
    response = make_response(bar)
    response.headers['Content-Type'] = 'application/json'
    print("returning")
    return response


if __name__ == '__main__':
    app.run(debug=True)
