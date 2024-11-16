from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load recipes from JSON file
with open('recipes.json') as f:
    RECIPES = json.load(f)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify([{"name": recipe["name"]} for recipe in RECIPES])

@app.route('/get_recipe', methods=['POST'])
def get_recipe():
    dish = request.form.get('dish').strip().lower()
    for recipe in RECIPES:
        if recipe['name'].lower() == dish:
            return jsonify(recipe)
    return jsonify({"error": "Recipe not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
