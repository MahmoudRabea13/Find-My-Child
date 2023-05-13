from flask import Flask, render_template,request , jsonify , json

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/input' , methods = ['POST', 'GET'] )
def filter():
    if request.method == 'POST':
        img = request.files.get('input_img')
        name = './static/Imgs/' + img.filename + '.jpg'
        img.save(name)
        print(img)
        return render_template('main.html')
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)