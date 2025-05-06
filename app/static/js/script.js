document.addEventListener("DOMContentLoaded", () => {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];

    function updateCartBadge() {
        const cartCount = document.getElementById("cart-count");
        if (cart.length > 0) {
            cartCount.textContent = cart.length;
            cartCount.style.display = "inline-block";
        } else {
            cartCount.style.display = "none";
        }
    }

    function addToCart(product) {
        const existingProduct = cart.find(item => item.id === product.id);
        if (existingProduct) {
            existingProduct.quantity += 1;
        } else {
            product.quantity = 1;
            cart.push(product);
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCartBadge();
    }

    document.body.addEventListener("click", async (event) => {
        if (event.target.classList.contains("add-to-cart")) {
            const productId = event.target.dataset.productId;

            try {
                const response = await fetch(`/api/product/${productId}`);
                if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

                const product = await response.json();
                if (!product || product.error) throw new Error("Invalid product data received.");

                addToCart(product);
                alert(`${product.name} added to cart!`);
            } catch (error) {
                console.error("Error fetching product:", error);
                alert("Error adding product. Please try again.");
            }
        }
    });

    updateCartBadge();
});
console.log("Add-to-cart script loaded");
