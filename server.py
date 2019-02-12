from flask import Flask, render_template, request, redirect, url_for
import connection
# todo: lets seegvcxcbncbn,vc vvb


app = Flask(__name__)


@app.route('/')
@app.route("/list")
def home_page():
    kurvaanyad = connection.get_data_from_file()
    print(kurvaanyad[0])
    return render_template("list.html")


# Todo : route - /question/<question_id>


# Todo : route - /add-question


# Todo : route - /question/<question_id>


# Todo : route - /list?order_by=title &order_direction=desc


# Todo : route - /question/<question_id>/edit


# Todo : route - /question/<question_id>/delete


if __name__ == '__main__':
    app.run()
