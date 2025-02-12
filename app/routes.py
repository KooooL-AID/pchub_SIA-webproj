from flask import Blueprint, render_template, jsonify, request, url_for
from app.models import Product
from app import db
import json
import os

main = Blueprint('main', __name__)

CATEGORIES = {
    'processors': 'Processors',
    'graphics-card': 'Graphics Cards',  # Changed from graphics-cards to match your data
    'ram': 'RAM',
    'storage': 'Storage',
    'psu': 'Power Supplies',           # Changed from power-supplies to match your data
    'cases': 'Cases',
    'cooling': 'Cooling',
    'peripherals': 'Peripherals',
    'accessories': 'Accessories'
}

@main.context_processor
def inject_categories():
    return dict(categories=CATEGORIES)

@main.route('/')
def index():
    featured_products = [
        {"name": "NVIDIA RTX 4090", "price": 90399.44, "image_url": "assets/graphics-card/rtx_4090.jpg"},
        {"name": "AMD Radeon RX 7900 XTX", "price": 56499.44, "image_url": "assets/graphics-card/rx_7900.jpg"},
        {"name": "AMD Ryzen 9 7950X", "price": 39549.44, "image_url": "assets/processors/ryzen_9.jpg"},
        # ... other products
    ]
    return render_template('index.html', featured_products=featured_products)


@main.route('/api/products')
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'image': url_for('static', filename=p.image_url),
        'category': p.category,
        'stock': p.stock
    } for p in products])

# Database initialization function
@main.route('/products')
def products():
    query = request.args.get('q')
    category = request.args.get('category')

    if query:
        products = Product.query.filter(
            (Product.name.ilike(f"%{query}%")) | (Product.description.ilike(f"%{query}%"))
        ).all()
    elif category:
        # Convert display name to storage format (e.g., "Graphics Cards" -> "graphics-cards")
        category_key = category.lower().replace(' ', '-')
        products = Product.query.filter(Product.category == category_key).all()
    else:
        products = Product.query.all()

    return render_template('products.html', 
                         products=products, 
                         search_query=query, 
                         selected_category=category,
                         categories=CATEGORIES)

def init_db():
    json_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'static', 'data', 'sample_products.json')

    if not os.path.exists(json_path):
        print(f"⚠️ Warning: sample_products.json not found at {json_path}")
        return

    with open(json_path, 'r') as file:
        data = json.load(file)
        product_data = data.get('products', [])

    if Product.query.first() is None:
        products = [
            Product(
                name=item["name"],
                price=item["price"],
                description=item["description"],
                image_url=item["image_url"],
                # Ensure category is stored in standardized format
                category=item["category"].lower().replace(' ', '-'),
                stock=item["stock"]
            ) for item in product_data
        ]

        db.session.add_all(products)
        db.session.commit()
        print(f"✅ Added {len(products)} sample products to the database!")

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
