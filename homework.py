from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie is set!")
    response.set_cookie('visit_count', '1')
    return response

@app.route('/get_cookie')
def get_cookie():
    visit_count = request.cookies.get('visit_count')
    return f"Visit count: {visit_count}"

@app.route('/language', methods=['GET', 'POST'])
def set_language():
    if request.method == 'POST':
        language = request.form.get('language')
        response = make_response(redirect('/'))
        response.set_cookie('language', language)
        return response
    return render_template('language.html')

@app.route('/redirect_example')
def redirect_example():
    return render_template('redirect_example.html')


if __name__ == "__main__":
    app.run(debug=True)