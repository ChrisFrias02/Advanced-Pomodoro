from models import db,User,Task,FocusSession
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(username,password):
    """Create a new user in the database."""
    password_hash = generate_password_hash(password)
    user = User(username=username, password_hash = password_hash)
    db.session.add(user)
    db.session.commit()
    return user


def create_task(user_id,title,description):
    """Create a new task for a user."""
    task = Task(user_id=user_id, title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return task


    
    