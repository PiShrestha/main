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
        nutriments = product.get('nutriments', {})
        product_info = {
           'name': product.get('product_name', 'N/A'),
           'allergens': product.get('allergens_from_ingredients', 'N/A'),
           'serving_size': product.get('serving_size', 'N/A'),
           'ingredients': product.get('ingredients_text', 'N/A'),
      
           'fat': nutriments.get('fat', 'N/A'),
           'fat_unit': nutriments.get('fat_unit', ''),
           'cholesterol': nutriments.get('cholesterol', 'N/A'),
           'cholesterol_unit': nutriments.get('cholesterol_unit', ''),
           'sodium': nutriments.get('sodium', 'N/A'),
           'sodium_unit': nutriments.get('sodium_unit', ''),
           'carbohydrates': nutriments.get('carbohydrates', 'N/A'),
           'carbohydrates_unit': nutriments.get('carbohydrates_unit', ''),
           'sugars': nutriments.get('sugars', 'N/A'),
           'sugars_unit': nutriments.get('sugars_unit', ''),
           'proteins': nutriments.get('proteins', 'N/A'),
           'proteins_unit': nutriments.get('proteins_unit', '')
       }
        return product_info
    else:
        return "Product not found or doesn't exist."
    
if __name__ == "__main__":
    app2.run(port=8080, debug=True)