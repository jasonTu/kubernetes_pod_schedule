from time import sleep

from flask import  abort, Response
from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from ..extension import db
from ..models import Note
import os


def abort_if_todo_doesnt_exist(todo_id):
    if not Note.query.get(todo_id):
        abort(Response("'code'：403,'message'：'Todo {todo_id} doesn't exist'\n".format(todo_id=todo_id), 403))


parser = reqparse.RequestParser()
parser.add_argument('task')

resource_fields = {
    'id': fields.Integer,
    'task': fields.String
}


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    # 获得资源
    @marshal_with(resource_fields, envelope='resource')
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return Note.query.get(todo_id)

    # 删除
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        task = Note.query.get(todo_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

    # 上传
    @marshal_with(resource_fields, envelope='resource')
    def put(self, todo_id):
        # 从表单获取资源
        args = parser.parse_args()
        abort_if_todo_doesnt_exist(todo_id)
        Task = Note.query.get(todo_id)
        Task.task = args['task']
        db.session.commit()
        # 返回给客户端资源
        return Task, 201


# TodoList
# shows a list of all todos , and lets you POST to add new tasks
class TodoList(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        # Default to 200OK
        return Note.query.all()

    @marshal_with(resource_fields, envelope='resource')
    def post(self):
        args = parser.parse_args()
        if Note.query.all():
            todo_id = max([x.id for x in Note.query.all()]) + 1
        else:
            todo_id = 1
        note = Note(id=todo_id, task=args["task"])
        db.session.add(note)
        db.session.commit()
        return note, 201


class initdb(Resource):
    def get(self):
        db.drop_all()
        db.create_all()
        return {"message":"initdb success"}


class getversion(Resource):
    def get(self):
        envrion = os.environ
        if 'imageVersion' in envrion:
            return {"message": envrion['imageVersion']}
        return {"message": "null"}

class getversion_sleep(Resource):
    def get(self):
        envrion = os.environ
        sleep(1)
        if 'imageVersion' in envrion:
            return {"message": envrion['imageVersion']}
        return {"message": "null"}
