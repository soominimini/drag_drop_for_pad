from flask import Flask, render_template,request

app = Flask(__name__)

f = open("log.txt", 'w')


@app.route('/', methods=['GET', 'POST'])
def taking_instruction():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        result = request.data.decode('utf-8')
        f.write(result)
        f.close()
        return render_template('home.html', val = result)


@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
