#  Date & Time 03/06/2024, 19:20.
#  @author Mesfin Haftu

from flask import Flask, request, jsonify
import mysql.connector

# Database connection details
db_config = {
    "host":     "localhost",
    "user":     "root",
    "password": "@Fmhtrtsaqyl24",
    "database": "Citizen_Data"
}

app = Flask(__name__)

# Connect to MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


@app.route("/citizen", methods = ["GET", "POST"])
def citizens():
    if request.method == "GET":

        # Get all citizens
        cursor.execute("SELECT * FROM citizen")
        data = cursor.fetchall()
        citizens = []
        for row in data:
            citizen = {"citizen_id":        row[0], "first_name": row[1], "father_name": row[2],
                       "grand_father_name": row[3], "mother_name": row[4], "date_of_birth": row[5],
                       "place_of_birth":    row[6], "gender": row[7], "nationality": row[8]}
            citizens.append(citizen)
        return jsonify(citizens)
    elif request.method == "POST":

        # Add a new citizen
        data = request.get_json()
        sql = ("INSERT INTO citizen (first_name, father_name, grand_father_name, mother_name, date_of_birth, place_of_birth, gender, nationality, date_registered) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")  # Add all fields
        values = (data["first_name"], data["father_name"], data["grand_father_name"],
                  data["mother_name"], data["date_of_birth"], data["place_of_birth"],
                  data["gender"], data["nationality"], data["date_registered"])  # Extract values from JSON
        cursor.execute(sql, values)
        connection.commit()
        return jsonify({"message": "Citizen added successfully!"})

# Similar routes can be created for address, contact_information, employment, and education


if __name__ == "__main__":
    app.run(debug = True)
