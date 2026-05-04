from flask import Flask, render_template, request

web = Flask(__name__)
@web.route('/')
def home():
    return render_template("home.html")


@web.route("/confirmation", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("phone_number")
        return render_template("confirm.html", name=n, city=c, phone_number=p)
    return render_template("register.html")



if __name__ == "__main__":
    web.run(debug=True)


