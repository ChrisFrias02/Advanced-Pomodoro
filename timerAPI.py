from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from db_helper import create_task, get_task_by_user_id, get_task_by_id, update_task, delete_task


class FocusSessionList(Resource):
    #creates new focuus session(timer)
    @jwt_required()
    def post(self):
        pass
        #gets all focus sessions for a user
    @jwt_required()
    def get(self):
        pass

    #delete focus session
    @jwt_required()    
    def delete(self):
        pass

    #update session(not implemented yet)
    @jwt_required()
    def put(self):
        pass