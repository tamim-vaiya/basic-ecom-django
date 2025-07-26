# 🛒 JavaScript Cart System Explanation

```js
// Check if 'cart' data exists in localStorage.
// If not, initialize an empty cart object.
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    // If it exists, parse it from JSON string to JavaScript object.
    cart = JSON.parse(localStorage.getItem('cart'));
}
```

```js
// jQuery event handler for all buttons with class "atc" (Add To Cart).
$(document).on('click', '.atc', function () {
    var item_id = this.id.toString();

    if (cart[item_id] != undefined) {
        cart[item_id] = cart[item_id] + 1;
    } else {
        cart[item_id] = 1;
    }

    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById("nav-cart").innerHTML = "Cart(" + Object.keys(cart).length + ")";
});
```

```js
// On page load, update cart count in the navbar if data exists
document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem('cart')) {
        const cart = JSON.parse(localStorage.getItem('cart'));
        document.getElementById("nav-cart").innerHTML = "Cart(" + Object.keys(cart).length + ")";
    }
});
```

```js
// Clear cart manually (for testing)
localStorage.removeItem('cart');
```

### ✅ Summary
- Uses localStorage to store cart items.
- Adds/removes items via JS + jQuery.
- Updates cart count in navbar.
- Data survives page reload.
