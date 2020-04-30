
class todo:

    def __init__(self):
        self.todos = []

    def addTodo(self,newTodo):
        self.todos.append(newTodo)

    def removeTodo(self, id: int):
        for i in self.todos:
            if i["id"] == id:
                self.todos.remove(i)
                return True
        else:
            return False

    def modifyTodo(self, id: int, new_note: str, new_description: str):
        for i in self.todos:
            if i["id"] == id:
                i["note"] = new_note
                i["description"] = new_description
                return True
        else:
            return False

    def getTodo(self, id: int):
        for i in self.todos:
            if i["id"] == id:
                return i
        else:
            return False

    def getTodos(self):
        return self.todos



