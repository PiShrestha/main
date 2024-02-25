from flask import Flask, request, render_template
import requests
import barcode_video
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vidscanner', methods=['POST'])
def result():
    return barcode_video.getBarcode()

if __name__ == "__main__":
    app.run(debug=True)