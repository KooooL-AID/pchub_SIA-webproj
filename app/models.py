# from app import db
# from datetime import datetime

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     price = db.Column(db.Float, nullable=False)
#     image_url = db.Column(db.String(255), nullable=False)
#     category = db.Column(db.String(50))
#     stock = db.Column(db.Integer, default=0)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))
#     orders = db.relationship('Order', backref='customer', lazy=True)

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     status = db.Column(db.String(20), default='pending')
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     items = db.relationship('OrderItem', backref='order', lazy=True)

# class OrderItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Float, nullable=False)