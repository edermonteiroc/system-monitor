System Information Collector

This project collects system information such as CPU, RAM, disk usage, motherboard details, and OS version, and stores the data in a MySQL database. It also provides a Flask-based API to retrieve and display this information.

Features

Collects system details including CPU, RAM, disk, OS, and IP address.

Stores data in a MySQL database.

Flask API for querying stored system data.

Supports table creation and validation.

Includes basic unit tests for system data retrieval.

Prerequisites

Before running the application, ensure you have the following installed:

Python 3.x

MySQL database

Required Python libraries (see below)

Installation

Clone the repository:

git clone <repository_url>
cd <project_directory>

Install dependencies:

pip install -r requirements.txt

Set up environment variables (create a .env file in the project root and define your MySQL credentials):

DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=your_database

Usage

1. Collect and Store System Data

Run the main script to gather system information and store it in the database:

python main.py <your_identifier>

This will create a table <your_identifier>_devices (if it doesn't exist) and insert system data.

2. Run the API Server

To start the Flask-based API:

python server.py

The API provides the following endpoints:

GET /tables - List all available tables.

GET /systems?table=<tablename> - Fetch system data from a specific table.

3. Run Tests

To run the unit tests:

pytest test_system.py

This ensures that system data retrieval functions work correctly.

Project Structure

|-- main.py              # Entry point for collecting and storing system data
|-- server.py            # Flask API for querying system data
|-- mysqlcon.py          # MySQL connection handling
|-- mysql_crud.py        # CRUD operations for MySQL
|-- mysqloperations.py   # Database table management
|-- getsystem.py         # System information retrieval
|-- getoperationsystem.py # OS details retrieval
|-- getmotherboard.py    # Motherboard details retrieval
|-- test_system.py       # Unit tests for system information functions
|-- requirements.txt     # Dependencies

Contributing

Feel free to fork this repository and submit pull requests with improvements or fixes.

License

This project is open-source and available under the MIT License.