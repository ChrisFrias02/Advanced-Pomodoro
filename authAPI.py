from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from db_helper import create_user, get_user_by_username

class UserRegistration(Resource):
    def post(self):
        data = request.get_json(force=True, silent=True)

        if not data or not data.get('username') or not data.get('email') or not data.get('password'):
            return {"error": "Missing username, email, or password"}, 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if get_user_by_username(username):
            return {"error": "Username already in use"}, 409
        


        new_user_id = create_user(username, email, password)

        if new_user_id:
            return {
                "message": "User created successfully",
                "user_id": new_user_id
            }, 201
        else:
            return {"error": "Failed to create user"}, 500
    pass

class UserLogin(Resource):
    def post(self):
        data = request.get_json(force=True, silent=True)

        if not data or not data.get('username') or not data.get('password'):
            return {"error": "Missing email or password"}, 400
        
        username = data.get('username')
        password = data.get('password')

        user = get_user_by_username(username)

        print(f"Password attempt: '{password}'")
        if user:
            print(f"DB hash: {user.password_hash}")
            print(f"Check result: {check_password_hash(user.password_hash, password)}")
        
        if not user or not check_password_hash(user.password_hash, password):
            return {"error": "Invalid password"}, 401
        
        #create access token
        access_token = create_access_token(identity=user.username)
        
        return jsonify(access_token=access_token)
    pass






