document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for menu item CRUD operations
    const menuForm = document.querySelector('#menu-form');
    if (menuForm) {
        menuForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Handle menu item form submission
            const formData = new FormData(menuForm);
            fetch(menuForm.action, {
                method: 'POST',
                body: formData
            }).then(response => response.json())
              .then(data => {
                  // Update the menu items table with the new data
                  updateMenuItemsTable(data);
              });
        });
    }

    // Add event listeners for order processing
    const orderForm = document.querySelector('#order-form');
    if (orderForm) {
        orderForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Handle order form submission
            const formData = new FormData(orderForm);
            fetch(orderForm.action, {
                method: 'POST',
                body: formData
            }).then(response => response.json())
              .then(data => {
                  // Update the orders table with the new data
                  updateOrdersTable(data);
              });
        });
    }

    // Add event listeners for payment processing
    const paymentForm = document.querySelector('#payment-form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Handle payment form submission
            const formData = new FormData(paymentForm);
            fetch(paymentForm.action, {
                method: 'POST',
                body: formData
            }).then(response => response.json())
              .then(data => {
                  // Update the orders table with the new data
                  updateOrdersTable(data);
              });
        });
    }
});

function updateMenuItemsTable(data) {
    const tableBody = document.querySelector('#menu-items-table tbody');
    tableBody.innerHTML = '';
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.price}</td>
            <td>${item.category}</td>
            <td>${item.availability ? 'Yes' : 'No'}</td>
            <td>
                <a href="/edit_menu_item/${item.id}" class="btn btn-warning btn-sm">Edit</a>
                <a href="/delete_menu_item/${item.id}" class="btn btn-danger btn-sm">Delete</a>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function updateOrdersTable(data) {
    const tableBody = document.querySelector('#orders-table tbody');
    tableBody.innerHTML = '';
    data.forEach(order => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${order.id}</td>
            <td>${order.table_number}</td>
            <td>${order.total}</td>
            <td>${order.timestamp}</td>
            <td>
                <a href="/add_order_item/${order.id}" class="btn btn-success btn-sm">Add Item</a>
                <a href="/remove_order_item/${order.id}" class="btn btn-danger btn-sm">Remove Item</a>
            </td>
        `;
        tableBody.appendChild(row);
    });
}
