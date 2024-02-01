from flask import Flask, render_template, request
from processing import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    message = " "

    if request.method == "POST":
        param1 = request.form.get("param1")
        param1 = float(param1)

        param2 = request.form.get("param2")
        param2 = float(param2)

        param3 = request.form.get("param3")
        param3 = float(param3)

        param4 = request.form.get("param4")
        param4 = float(param4)

        param5 = request.form.get("param5")
        param5 = float(param5)

        param6 = request.form.get("param6")
        param6 = float(param6)

        param7 = request.form.get("param7")
        param7 = float(param7)

        param8 = request.form.get("param8")
        param8 = float(param8)

        param9 = request.form.get("param9")
        param9 = float(param9)

        param10 = request.form.get("param10")
        param10 = float(param10)

        result = predict([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10])

        message = f"Значение параметра шероховатости поверхности равно {result}"

        print(param1)
    return render_template("index.html", message=message)




