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

3. Create a virtual environment to manage your project's dependencies. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

6. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. Run the Flask application:
   ```bash
   flask run
   ```

8. Open your web browser and navigate to `http://127.0.0.1:5000` to access the POS system.

## Verifying Module Names and Installing Missing Modules

To verify the correct module names and install missing modules, follow these steps:

1. Ensure that the module names in your `app.py` file are correct. The import statement for `flask_sqlalchemy` should be:
   ```python
   from flask_sqlalchemy import SQLAlchemy
   ```

2. Verify that the `flask_sqlalchemy` module is installed by running:
   ```bash
   pip show flask_sqlalchemy
   ```

3. If the module is not installed, install it using:
   ```bash
   pip install flask_sqlalchemy
   ```

4. After verifying the module names and installing the dependencies, try running the Flask application again:
   ```bash
   flask run
   ```
