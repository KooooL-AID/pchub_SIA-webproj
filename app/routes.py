from flask import Blueprint, render_template, jsonify, request, url_for, flash, redirect,abort, session
import json
import os
from datetime import datetime

main = Blueprint('main', __name__)
DATA_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'static', 'data', 'sample_products.json')
TESTIMONIALS_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'static', 'data', 'testimonials.json')
users_db = []


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

#Product Details routes
@main.route('/product/<int:product_id>')
def product_detail(product_id):
    """ Render detailed product page. """
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return abort(404)
    
    return render_template('product_detail.html', product=product)

# Currency formatting filter
def currency_filter(value):
    return f"₱{value:,.2f}"

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

#JSON API endpoints
@main.route('/api/product/<int:product_id>')
def get_product(product_id):
    """Return product details as JSON."""
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


#Login and Register routes

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password') # In a real app, HASH THIS PASSWORD!

        if not name or not email or not password:
            flash('Please fill out all fields.', 'danger')
            return render_template('register.html')

        existing_user = next((user for user in users_db if user['email'] == email), None)
        if existing_user:
            flash('Email already registered.', 'warning')
            return render_template('register.html')

        users_db.append({'name': name, 'email': email, 'password': password})
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html') # Rendered from uploaded:register.html

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = next((user for user in users_db if user['email'] == email and user['password'] == password), None)

        if user:
            session['user_email'] = user['email'] # Basic session management
            flash('Login successful!', 'success')
            return redirect(url_for('main.index')) # Or a dashboard page
        else:
            flash('Invalid email or password.', 'danger')
            return render_template('login.html') # Rendered from uploaded:login.html
    return render_template('login.html') # Rendered from uploaded:login.html

@main.route('/logout')
def logout():
    session.pop('user_email', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

# Additional pages routes

@main.route('/cart')
def cart():
    return render_template('cart.html')


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

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/newsletter')
def newsletter_signup():
    return render_template('newsletter.html')

@main.route('/downloads')
def downloads():
    return render_template('downloads.html')

@main.route('/support')
def support():
    return render_template('support.html')


# Testimonials Page

# Load testimonials from JSON
def load_testimonials():
    if not os.path.exists(TESTIMONIALS_FILE):
        return {"testimonials": []}
    with open(TESTIMONIALS_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"testimonials": []}
        
def save_testimonial(new_testimonial):
    data = load_testimonials()
    data["testimonials"].append(new_testimonial)
    with open(TESTIMONIALS_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

@main.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        rating = int(request.form.get('rating'))
        comment = request.form.get('comment')
        product_id = request.form.get('product_id')
        if not product_id:
            flash("Please select a product.", "error")
            return redirect(url_for('main.testimonials'))
        product_id = int(product_id)


        if not customer_name or not comment:
            flash("Please fill in all fields.", "error")
            return redirect(url_for('main.testimonials'))

        new_testimonial = {
            "id": len(load_testimonials()["testimonials"]) + 1,
            "customer_name": customer_name,
            "rating": rating,
            "comment": comment,
            "product_id": product_id,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        save_testimonial(new_testimonial)
        flash("Your testimonial has been submitted successfully!", "success")
        return redirect(url_for('main.testimonials'))

    all_testimonials = load_testimonials()["testimonials"]
    products = load_products()  # Load products for selection in the form
    return render_template('testimonials.html', testimonials=all_testimonials, products=products)

