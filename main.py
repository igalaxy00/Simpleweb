from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    args = request.args

    name = args.get('name')
    message = args.get('message')

    if not name and not message:
        return "Rekruto! Давай дружить!"

    return f"Hello {args['name']} ! {args['message'] } "