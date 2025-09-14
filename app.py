from flask import Flask, render_template, request
import csv

# ✅ yaha __name__ likhna hai
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        full_name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        issue = request.form["issue"]

        with open("leads.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([full_name, email, phone, issue])

        return "Leads Submitted Successfully!"

    return render_template("index.html")

# ✅ yaha bhi __main__ likhna hai
if __name__ == "__main__":
    app.run(debug=True)
