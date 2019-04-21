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
    if request.is_json:
      data = request.json
      string_to_cut = data["string_to_cut"]
      data["string_to_cut"] = string_to_cut[2:-1:3]
    return jsonify(data)
  
if __name__ == "__main__":
  app.run()
