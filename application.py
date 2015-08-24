from flask import Flask, jsonify, render_template, request

from reddit_doc_model import RedditModel

app = Flask(__name__)

model = RedditModel()
model.load_model()
def upit(word):
	return str(model.most_sim_subs(word))

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a', 0, type=unicode)

    return jsonify(result=upit(a))


if __name__ == '__main__':

    app.run(debug=True)
