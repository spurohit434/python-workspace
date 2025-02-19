from http.cookiejar import debug

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

posts = {
    0: {
        'name' : 'Jos',
        'section': 4
    },
    1: {
            'name' : 'Sam',
            'section': 4
        }
        ,
    2: {
            'name' : 'Daniles',
            'section': 4
        }
}

@app.route('/posts/<int:post_id>')
def posts(post_id):
    # post = post_id
    post = posts.get(post_id)
    return f"content with {post['name']} and {post['section']}"

if __name__ == '__main__':
    app.run(debug=True)
