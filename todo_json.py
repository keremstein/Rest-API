from todo_funcs import todo
from flask import Flask, jsonify, request

todolist = todo()
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"Welcome to ToDo List Page" : "by Keremstein"})

@app.route("/todos", methods = ["GET","POST"])
def displayTodos():

    if request.method == "GET":
        return jsonify(todolist.getTodos())

    elif request.method == "POST":
        todolist.addTodo({"id":len(todolist.todos)+1, "note":input("note ? "), "description":input("description ? ")})
        return jsonify({"Result" : True})

    else:
        return jsonify({"Result" : False})

@app.route("/todos/<int:id>", methods = ["GET","PUT","DELETE"])
def displayTodo(id):
    
    if request.method == "GET":
        return jsonify(todolist.getTodo(id))

    elif request.method == "PUT":
        if len(todolist.todos) == 0:
            return jsonify({'Todo Item': 'List is empty'}), 404
        else:
            todolist.modifyTodo(id, input("new note ? "), input("new description ? "))
            return jsonify({"Data" : "Changed"})

    elif request.method == "DELETE":
        if len(todolist.todos) == 0:
            return jsonify({'Todo Item': 'Not found'}), 404
        else:
            todolist.removeTodo(id)
            return jsonify({"Data" : "Deleted"})

    else:
        return jsonify({"Result" : False})


if __name__ == "__main__":
    app.run(debug=True)