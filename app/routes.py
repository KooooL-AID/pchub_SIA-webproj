from flask import Blueprint, render_template, jsonify, request, url_for
import json
import os

main = Blueprint('main', __name__)
DATA_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'static', 'data', 'sample_products.json')

# Categories dictionary for filtering
CATEGORIES = {
    'processors': 'Processors',
    'graphics-card': 'Graphics Cards',
    'ram': 'RAM',
    'storage': 'Storage',
    'psu': 'Power Supplies',
    'cases': 'Cases',
    'cooling': 'Cooling',
    'peripherals': 'Peripherals',
    'accessories': 'Accessories'
}

# Inject categories into templates globally
@main.context_processor
def inject_categories():
    return dict(categories=CATEGORIES)

# Function to load products from sample_products.json
def load_products():
    """ Load products from JSON file. """
    if not os.path.exists(DATA_FILE):
        print(f"⚠️ Warning: sample_products.json not found at {DATA_FILE}")
        return []

    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data.get('products', [])
        except json.JSONDecodeError:
            print("❌ Error: Failed to parse sample_products.json")
            return []

# Home page route
@main.route('/')
def index():
    """ Render homepage with featured products. """
    featured_products = load_products()[:3]  # Show first 3 products as featured
    return render_template('index.html', featured_products=featured_products)

# Products page route
@main.route('/products')
def products():
    """ Render products page, filtering by category or search query. """
    query = request.args.get('q')
    category = request.args.get('category')
    
    all_products = load_products()

    # Filter by category
    if category and category in CATEGORIES:
        filtered_products = [p for p in all_products if p["category"].lower() == category.lower()]
    # Filter by search query
    elif query:
        filtered_products = [p for p in all_products if query.lower() in p["name"].lower()]
    else:
        filtered_products = all_products

    return render_template('products.html', products=filtered_products, search_query=query, selected_category=category)

# API endpoint to return all products as JSON
@main.route('/api/products')
def get_products():
    return jsonify(load_products())

# Currency formatting filter
def currency_filter(value):
    return f"₱{value:,.2f}"

# Additional pages
@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/mission')
def mission():
    return render_template('mission.html')

@main.route('/vision')
def vision():
    return render_template('vision.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

@main.route('/return-policy')
def return_policy():
    return render_template('return_policy.html')

@main.route('/how-to')
def how_to():
    return render_template('how_to.html')

@main.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')
