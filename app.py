from flask import Flask, render_template, request
import boto3
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# Connect to DynamoDB in the London region
dynamodb = boto3.resource("dynamodb", region_name="eu-west-2")

# Connect to our table
table = dynamodb.Table("WebAppRegistrations")


@app.route("/", methods=["GET", "POST"])
def home():

    message = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        registration_id = str(uuid.uuid4())

        table.put_item(
            Item={
                "registrationId": registration_id,
                "name": name,
                "email": email,
                "phone": phone,
                "createdAt": datetime.now(timezone.utc).isoformat()
            }
        )

        message = f"Thank you {name}. Your registration was successful!"

    return render_template("index.html", message=message)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)