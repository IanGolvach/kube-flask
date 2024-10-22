from flask import Flask, request, jsonify, url_for
from service import ToDoService, MembershipService, UserService

from models import Schema
from markupsafe import escape

import json


app = Flask(__name__)




@app.after_request
def add_headers(response):
   response.headers['Access-Control-Allow-Origin'] = "*"
   response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
   response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
   return response


@app.route("/")
def hello():
   return "Hello World!"




@app.route("/<name>")
def hello_name(name):
   # Check if <name> is a member.
   return "<b>Hello " + escape(name) + "</b>"

@app.route("/terry")
def terry_crews():
   return """
   <p>Here's Terry Crews</p>
   <img src=\""""+url_for('static',filename='TerryCrews.jpg')+"""\" alt="Terry Crews">
   """


@app.route("/todo", methods=["GET"])
def list_todo():
   return jsonify(ToDoService().list())




@app.route("/todo", methods=["POST"])
def create_todo():
   return jsonify(ToDoService().create(request.get_json()))




@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
   return jsonify(ToDoService().update(item_id, request.get_json()))


@app.route("/todo/<item_id>", methods=["GET"])
def get_item(item_id):
   return jsonify(ToDoService().get_by_id(item_id))


@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
   return jsonify(ToDoService().delete(item_id))

@app.route("/members", methods=["GET"])
def show_members():
    return jsonify(MembershipService().list())

@app.route("/members",methods=["POST"])
def add_member():
    return jsonify(MembershipService().create(request.get_json()))

@app.route("/members/<member_id>",methods=["GET"])
def show_single_member(member_id):
   return jsonify(MembershipService().get_by_id(member_id))

@app.route("/users",methods=["GET"])
def show_users():
   return jsonify(UserService().list())

@app.route("/users",methods=["POST"])
def create_user():
   return jsonify(UserService.create(request.get_json()))

@app.route("/users/<userid>")
def show_user_specific(userid):
   return jsonify(UserService().get_by_id(userid))




if __name__ == "__main__":
   Schema()
   app.run(debug=True, host='127.0.0.1', port=5000)
