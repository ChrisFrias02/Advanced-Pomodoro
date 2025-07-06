from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from db_helper import create_focus_session, get_total_focus_time, get_total_focus_time_by_task, get_focus_session_by_id, delete_focus_session,get_focus_sessions_by_user


class FocusSessionList(Resource):
    #creates new focuus session(timer)
    @jwt_required()
    def post(self):
        data = request.get_json(force=True, silent=True)
        if not data or not data.get('planned_minutes'):
            return {"error": "Missing planned_minutes"}, 400
        
        user_id = get_jwt_identity()
        planned_minutes = data.get('planned_minutes')
        task_id = data.get('task_id')

        session = create_focus_session(user_id, planned_minutes, task_id)
        if session:
            return {
                "message": "Focus session created successfully",
                "session_id": session.id,
                "task_name": session.task_name,
                "planned_minutes": session.planned_minutes
            }, 201
        else:
            return {"error": "Failed to create focus session"}, 500
    @jwt_required()
    #gets all focus sessions for a user
    def get(self):
        user_id = get_jwt_identity()  
        task_id = request.args.get('task_id', type=int)

        sessions = get_focus_sessions_by_user(user_id, task_id)
        if sessions:
            return jsonify([{
                "session_id": s.id,
                "task_name": s.task_name,
                "planned_minutes": s.planned_minutes,
                "actual_minutes": s.actual_minutes,
                "completed": s.completed,
                "timestamp": s.timestamp.isoformat()
            } for s in sessions])
        else:
            return {"message": "No focus sessions found"}, 404

    #delete focus session
    @jwt_required()    
    def delete(self):
        user_id = get_jwt_identity()
        data = request.get_json(force=True, silent=True)
        if not data or not data.get('session_id'):
            return {"error": "Missing session_id"}, 400
        
        session_id = data.get('session_id')
        session = get_focus_session_by_id(session_id,user_id)

        if not session:
            return {"error": "Focus session not found"}, 404

        delete_focus_session(session_id)
        return {"message": "Focus session deleted successfully"}, 200

    #update session(not implemented yet)
    @jwt_required()
    def put(self):
        pass

class FocusSessionStats(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        task_id = request.args.get('task_id', type=int)

        if task_id:
            total_hours, total_minutes = get_total_focus_time_by_task(user_id, task_id)
        else:
            total_hours, total_minutes = get_total_focus_time(user_id)

        return {
            "total_focus_time": {
                "hours": total_hours,
                "minutes": total_minutes
            }
        }, 200

class FocusSessionById(Resource):
    @jwt_required()
    def get(self, session_id):
        user_id = get_jwt_identity()
        session = get_focus_session_by_id(session_id,user_id)
        if session:
            return {
                "session_id": session.id,
                "task_name": session.task_name,
                "planned_minutes": session.planned_minutes,
                "actual_minutes": session.actual_minutes,
                "completed": session.completed,
                "timestamp": session.timestamp.isoformat()
            }, 200
        else:
            return {"error": "Focus session not found"}, 404