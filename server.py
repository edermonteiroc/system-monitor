from flask import Flask, jsonify, request, render_template
from mysqlcon import connect_db

app = Flask(__name__)

@app.route("/")
def index():
    """Render the HTML page with a dropdown for table selection."""
    return render_template("index.html")

@app.route("/tables", methods=["GET"])
def get_tables():
    """API endpoint to get a list of all tables in the database."""
    dbcon = connect_db()
    if dbcon:
        try:
            mycursor = dbcon.cursor()
            mycursor.execute("SHOW TABLES")  # Get all tables
            tables = [table[0] for table in mycursor.fetchall()]
            return jsonify({"tables": tables})
        except Exception as ex:
            return jsonify({"error": str(ex)})
    return jsonify({"error": "Database connection failed"}), 500

@app.route("/systems", methods=["GET"])
def get_system_data():
    """API endpoint to get data from a selected table."""
    tablename = request.args.get("table")  # Get selected table from request
    if not tablename:
        return jsonify({"error": "Table name is required"}), 400

    dbcon = connect_db()
    if dbcon:
        try:
            mycursor = dbcon.cursor(dictionary=True)
            sql = f"SELECT * FROM `{tablename}`"
            mycursor.execute(sql)
            results = mycursor.fetchall()
            return jsonify(results)
        except Exception as ex:
            return jsonify({"error": str(ex)})
    return jsonify({"error": "Database connection failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)