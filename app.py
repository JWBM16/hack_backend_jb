from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# hack_1
@app.route("/users", methods=["GET"])
def fn_get():
    return jsonify({"payload": "success"})

# hack_2
@app.route("/user", methods=["POST"])
def fn_post():
    return jsonify({"payload": "success"})

# hack_3
@app.route("/user", methods=["DELETE"])
def fn_delete():
    return jsonify({"payload": "success"})

# hack_4
@app.route("/user", methods=["PUT"])
def fn_put():
    return jsonify({"payload": "success",
                    "error":False})

# hack_5
@app.route("/api/v1/users", methods=["GET"])
def fn_get_v1():
    return jsonify({'payload':[]})



# hack_6
@app.route("/api/v1/user", methods=["post"])
def fn_api_post_user():
    email = request.args.get("email")
    name = request.args.get("name")
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
        }
    })

# hack_7
@app.route("/api/v1/user/add", methods=["POST"])
def fn_api_post_add_user():
    email = request.form.get("email")
    name = request.form.get("name")
    id = request.form.get("id")
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    })

# hack_8
@app.route("/api/v1/user/create", methods=["post"])
def fn_api_post_create_user():
    data = request.get_json()
    return jsonify({
        "payload": {
            "email":data["email"],
            "name":data["name"],
            "id":data["id"],
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
