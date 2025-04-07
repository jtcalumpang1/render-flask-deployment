from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        last_name = request.form.get("last_name")


        if first_name and middle_name and last_name:
            full_name = f"{first_name} {middle_name} {last_name}"
            return render_template("submitted.html", full_name=full_name)
        else:

            return "Please fill out all fields.", 400

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
