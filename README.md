# TestCopilot

## User Interface Implementation

The Point of Sale (POS) system for the restaurant has a user-friendly interface using HTML, CSS, and JavaScript. The frontend is built with Bootstrap for styling and responsiveness.

### Frontend Structure

- `templates/`: Contains HTML files for different pages of the POS system.
  - `layout.html`: Basic HTML layout with Bootstrap.
  - `login.html`: Login form for user authentication.
  - `menu.html`: Form for CRUD operations on menu items.
  - `order.html`: Form for adding/removing items from orders.
  - `payment.html`: Form for processing payments.
  - `receipt.html`: Template for generating printable receipts.
  - `table.html`: Form for assigning orders to tables and tracking occupancy.
  - `reports.html`: Template for viewing daily sales, total revenue, and order history.

- `static/css/`: Contains CSS files for styling.
  - `styles.css`: Custom CSS styles for the POS system.

- `static/js/`: Contains JavaScript files for interactivity.
  - `scripts.js`: Custom JavaScript for the POS system.

## Setting Up the Frontend

To set up the frontend, follow these steps:

1. Ensure you have Python and Flask installed. If not, install them using the following commands:
   ```bash
   pip install Flask
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Hayato360/TestCopilot.git
   cd TestCopilot
   ```

3. Run the Flask application:
   ```bash
   flask run
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the POS system.

## How to Run the Program

To run the program, follow these steps:

1. Ensure you have Python and Flask installed. If not, install them using the following commands:
   ```bash
   pip install Flask
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Hayato360/TestCopilot.git
   cd TestCopilot
   ```

3. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000` to access the POS system.
