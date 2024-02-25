from flask import Flask, request, render_template, Response
import requests
import barcode_video

app2 = Flask(__name__)

@app2.route('/')
def index():
    return render_template('index.html')

@app2.route('/result', methods=['POST'])
def result():
    barcode = barcode_video.getBarcode()
    product_info = fetch_product_info(barcode)
    return render_template('result.html', barcode=barcode, product=product_info)

def fetch_product_info(barcode):
    endpoint = 'https://world.openfoodfacts.org/api/v0/product/'
    url = f'{endpoint}{barcode}.json'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 1:
        product = data['product']
        product_info = {
            'name': product.get('product_name', 'No product name available'),
            'allergens': product.get('allergens_from_ingredients', 'No allergens information available'),
            'serving_size': product.get('serving_size', 'No serving size available'),
            'ingredients': product.get('ingredients_text', 'No ingredients text available'),
            'nutriments': product.get('nutriments', {})
        }
        return product_info
    else:
        return "Product not found or doesn't exist."

if __name__ == "__main__":
    app2.run(port=6969, debug=True)