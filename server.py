from flask import Flask, url_for, request, render_template, send_file, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def result():
    name = request.form['choice']
    brutto = request.form['brutto']
    netto = request.form['netto']

    print(str(name) + str(brutto) + str(netto))

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=1337, debug=True, threaded=True)
    app.run(host='localhost', port=1337, debug=True, threaded=True)
