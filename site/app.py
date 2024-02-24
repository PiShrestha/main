from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        barcode = request.form['barcode']
        product_info = fetch_product_info(barcode)
        return render_template('index.html', product=product_info)
    return render_template('index.html', product=None)

def fetch_product_info(barcode):
    endpoint = 'https://world.openfoodfacts.org/api/v0/product/'
    url = f'{endpoint}{barcode}.json'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 1:
        product = data['product']
        product_info = {
            'name': product.get('product_name', 'No product name available'),
            'serving_size': product.get('serving_size', 'No serving size available'),
            'allergens': product.get('allergens_from_ingredients', 'No allergens information available'),
            'ingredients': product.get('ingredients_text', 'No ingredients text available'),
            'nutriments': product.get('nutriments', {})
        }
        return product_info
    else:
        return "Product not found or doesn't exist."

if __name__ == '__main__':
    app.run(debug=True)
