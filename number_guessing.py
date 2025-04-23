from flask import Flask, render_template, request
import random

app = Flask(__name__)

final_number = random.randint(1,15)


@app.route("/", methods=['GET', 'POST'])
def home():
    number_guess = 0
    if request.method == "POST":
        print(final_number)
        guess = request.form["guess"]
        number_guess = int(guess)
    return render_template('number_guessing/index.html', guess = number_guess, final_number = final_number)


if __name__ == "__main__":
    app.run(debug=True, port=2500)