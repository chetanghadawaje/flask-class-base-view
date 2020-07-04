from flask import Flask
from flask.views import MethodView
from decorators import DemoDecorator


class ClassBaseAPI(MethodView):
    decorators = [DemoDecorator]

    def get(self, id):
        print("GET -->", id)
        return {"GET": id}

    def post(self):
        print("POST")
        return {"POST": "Done"}

    def delete(self, id):
        print("DELETE --->", id)
        return {"DELETE": id}

    def put(self, id):
        print("PUT --->", id)
        return {"PUT": id}


app = Flask(__name__)
# API
user_api_view = ClassBaseAPI.as_view('class_base_api')
app.add_url_rule('/class/', defaults={'id': None}, view_func=user_api_view, methods=["GET"])
app.add_url_rule('/class/', view_func=user_api_view, methods=["POST"])
app.add_url_rule('/class/<int:id>', view_func=user_api_view, methods=["GET", "PUT", "DELETE"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)