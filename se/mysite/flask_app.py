from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # static/images klasöründeki resimlerin isimleri
    images = [
        'images/resim1.jpg',
        'images/resim2.jpg',
        'images/resim3.jpg'
    ]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
