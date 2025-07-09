
# 🖥️ PC Parts Hub (PCHub) – Flask Web App

**PC Parts Hub (PCHub)** is a simple modern e-commerce platform built with Flask. It allows users to browse PC hardware products, search/filter by category, add items to a shopping cart, and a demo login and registration for presentation . Includes a blog section and static JSON-powered product management.

---

## 📦 Features

- 🛍️ Product catalog with categories and search
- 🛒 Cart with localStorage support
- 👤 Register/Login system (session-based)
- 🧾 Testimonials with product links
- 📄 Pages: About, Mission, Vision, FAQ, Return Policy, Tutorials, Blog, Contact
- 📊 API: Get product data via `/api/product/<id>`
- 🌐 Integrated with Tawk.to and Messenger chat widgets
- 🔧 Designed with Bootstrap 5

---

## 🚀 Live Demo

🌐 [Visit the Deployed Site](https://pchub-sia-webproj.onrender.com/)

---

## 🧰 Tech Stack

- **Backend**: Python, Flask, Jinja2
- **Frontend**: HTML5, CSS3, Bootstrap 5, JS
- **Database**: JSON-based product store (static)
- **Deployment**: Gunicorn + Render / (or use `wsgi.py`)

---

## 🔧 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/pchub-flask-app.git
cd pchub-flask-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python wsgi.py
```

App will be available at `http://localhost:5000`

---

## 📁 Project Structure

```
/pchub-flask-app
│
├── app/
│   ├── static/
│   │   └── data/sample_products.json
│   │   └── assets/...
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── product_detail.html
│   ├── routes.py
│   └── ...
├── wsgi.py
├── requirements.txt
└── README.md
```

---

## 📦 JSON API

- `GET /api/product/<id>` — Get product data as JSON

---

## 🧪 Example Test Accounts (for demo only)

| Email                | Password  |
|---------------------|-----------|
| test@pchub.com      | 1234      |
| demo@pchub.com      | password  |

---

## 📬 Contact

Created by 
📧 Email: eleakim177@gmail.com  
🔗 [Facebook Page](https://www.facebook.com/profile.php?id=61575747562680)
