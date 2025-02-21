
document.addEventListener("DOMContentLoaded", () => {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];

    // Function to update cart icon badge
    function updateCartBadge() {
        const cartCount = document.getElementById("cart-count");
        if (cart.length > 0) {
            cartCount.textContent = cart.length;
            cartCount.style.display = "inline-block";
        } else {
            cartCount.style.display = "none";
        }
    }

    // Function to add a product to the cart
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
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", async (event) => {
            const productId = event.target.dataset.productId;
    
            try {
                const response = await fetch(`/api/product/${productId}`);
    
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
    
                const product = await response.json();
    
                if (!product || product.error) {
                    throw new Error("Invalid product data received.");
                }
    
                addToCart(product);
                alert(`${product.name} added to cart!`);
    
            } catch (error) {
                console.error("Error fetching product:", error);
                alert("Error adding product. Please try again.");
            }
        });
    });

    
    

    // Update cart count on page load
    updateCartBadge();
    
    document.getElementById('chat-widget').addEventListener('click', function() {
        document.getElementById('chat-box').style.display = 'flex';
    });
    
    document.getElementById('close-chat').addEventListener('click', function() {
        document.getElementById('chat-box').style.display = 'none';
    });
    
    document.getElementById('send-message').addEventListener('click', function() {
        const inputField = document.getElementById('chat-input');
        const message = inputField.value.trim();
        
        if (message !== "") {
            const chatBody = document.getElementById('chat-body');
            
            // Append user message
            const userMessage = document.createElement('p');
            userMessage.textContent = "You: " + message;
            userMessage.style.background = "#eee";
            userMessage.style.padding = "8px";
            userMessage.style.borderRadius = "10px";
            chatBody.appendChild(userMessage);
    
            // Clear input field
            inputField.value = "";
    
            // Auto-reply
            setTimeout(() => {
                const botReply = document.createElement('p');
                botReply.textContent = "🤖 Bot: Thank you for reaching out!";
                botReply.classList.add('bot-message');
                chatBody.appendChild(botReply);
    
                // Scroll to bottom
                chatBody.scrollTop = chatBody.scrollHeight;
            }, 1000);
        }
    });
    
    
    
});
