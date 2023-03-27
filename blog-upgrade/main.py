import datetime
from flask import Flask, render_template, request
import requests
from post import Post
from notification_manager import NotificationManager
import random
import time


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date():
    return str_time_prop("January 01, 2023", datetime.datetime.now().strftime('%B %d, %Y'), '%B %d, %Y', random.random())


posts = requests.get(url="https://api.npoint.io/56e6f9a1df499c2a2546").json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"], "Viktor Tran", random_date()) for post in posts]

notification_manager = NotificationManager()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        notification_manager.send_email(name, email, phone, message)
        return render_template("contact.html", message="Successfully sent your message")

    return render_template("contact.html")


@app.route("/post/<post_id>")
def get_post(post_id):
    requested_post = None
    for post in post_objects:
        if post.id == int(post_id):
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run()

