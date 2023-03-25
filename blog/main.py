import requests
from flask import Flask, render_template
from post import Post


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for post in post_objects:
        if post.id == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
