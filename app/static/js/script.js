document.addEventListener("DOMContentLoaded", function () {
    updateCartCount();

    // Handle Add to Cart Buttons
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", function () {
            const productId = this.getAttribute("data-product-id");
            addToCart(productId);
        });
    });

    // Navbar toggle fix (Bootstrap issue workaround)
    const navbarToggler = document.querySelector(".navbar-toggler");
    if (navbarToggler) {
        navbarToggler.addEventListener("click", function () {
            document.querySelector("#navbarNav").classList.toggle("show");
        });
    }


// Function to add product to cart
function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem("cart")) || {};
    
    cart[productId] = (cart[productId] || 0) + 1;

    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

// Function to update cart count badge
function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem("cart")) || {};
    let itemCount = Object.values(cart).reduce((acc, curr) => acc + curr, 0);
    
    const cartBadge = document.querySelector(".cart-count");
    if (cartBadge) {
        cartBadge.textContent = itemCount;
    }
}

// Function to clear cart (for checkout simulation)
function clearCart() {
    localStorage.removeItem("cart");
    updateCartCount();
}

// Expose function to clear cart globally (for checkout button)
window.clearCart = clearCart;
