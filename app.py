from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    message = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        print("New Registration:")
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)

        message = f"Thank you {name}. Your registration was successful!"

    return render_template("index.html", message=message)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
