from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from db_helper import create_task, get_task_by_user_id, get_task_by_id, update_task, delete_task


class TaskList(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json(force=True, silent= True)

        if not data or not data.get('title') or not data.get('description'):
            return {"error": "Missing title or description"}, 400
        
        user_id = get_jwt_identity()
        title = data.get('title')
        description = data.get('description')

        task = create_task(user_id, title, description)
        if task:
            return {
                "message": "Task created successfully",
                "task_id": task.id,
                "title": task.title,
                "description": task.description
            }, 201
        else:
            return {"error": "Failed to create task"}, 500
        

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        task = get_task_by_user_id(user_id)

        if task:
            return jsonify([{
                "task_id": t.id,
                "title": t.title,
                "description": t.description
            } for t in task])
        else:
            return {"message": "No tasks found"}, 404
        
        

    @jwt_required()
    def delete(self):
        data = request.get_json(force=True, silent=True)

        if not data or not data.get('task_id'):
            return {"error": "Missing task_id"}, 400
        
        user_id = get_jwt_identity()
        task_id = data.get('task_id')

        task = get_task_by_id(task_id, user_id)
        if not task:
            return {"error": "Task not found"}, 404
        
        if delete_task(task_id):
            return {"message": "Task deleted successfully"}, 200
        else:
            return {"error": "Failed to delete task"}, 500

    @jwt_required()
    def put(self):
        data = request.get_json(force=True, silent=True)
        if not data or not data.get('task_id') or not data.get('title') or not data.get('description'):
            return {"error": "Missing task_id, title, or description"}, 400
        task_id = data.get('task_id')
        title = data.get('title')
        description = data.get('description')

        new_task = update_task(task_id, title, description)
        if new_task:
            return {
                "message": "Task updated successfully",
                "task_id": new_task.id,
                "title": new_task.title,
                "description": new_task.description
            }, 200
        else:
            return {"error": "Failed to update task"}, 500
