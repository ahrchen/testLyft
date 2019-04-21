from flask import Flask, abort, request, jsonify
import json

app = Flask(__name__)

@app.route("/test", methods=['POST'])
def test():
  if not request.json:
    abort(400)
    print(request.json)
    return json.dumps(request.json)
  else:
    try:
        data = request.json
        string_to_cut = data["string_to_cut"]
        return_string = string_to_cut[2:-1:3]
        return_object ={"return_string":return_string}
        return jsonify(return_object)
    except KeyError:
        return_object = {"return_string": ""}
        return jsonify(return_object)
if __name__ == "__main__":
  app.run()
