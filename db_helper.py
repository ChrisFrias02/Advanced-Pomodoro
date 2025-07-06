from models import db,User,Task,FocusSession
from werkzeug.security import generate_password_hash, check_password_hash




def create_user(username,email,password):
    """Create a new user in the database."""
    password_hash = generate_password_hash(password)
    user = User(username=username,email = email, password_hash = password_hash)
    db.session.add(user)
    db.session.commit()
    return user.id

def get_user_by_username(username):
    """Retrieve a user by username."""
    print(f"Looking for username: {username}")
    user = User.query.filter_by(username=username).first()
    print(f"Found user: {user}")
    return user

def create_task(user_id,title,description):
    """Create a new task for a user."""
    task = Task(user_id=user_id, title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return task

def get_task_by_user_id(user_id):
    """get tasks for a specific user"""
    tasks = Task.query.filter_by(user_id=user_id).all()
    return tasks

def get_task_by_id(task_id,user_id):
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    return task
 

def update_task(task_id,title,description):
    task = Task.query.get(task_id)
    if task:
        task.title = title
        task.description = description
        db.session.commit()
        return task
    return None
    

def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False


def create_focus_session(user_id, planned_minutes, task_id=None):
    session = FocusSession(
        user_id=user_id,
        task_id=task_id,
        task_name=Task.query.get(task_id).title if task_id else "General Focus",
        planned_minutes=planned_minutes,
        completed=False
    )
    db.session.add(session)
    db.session.commit()
    return session


def get_focus_sessions_by_user(user_id,task_id ):
    if task_id:
        return FocusSession.query.filter_by(user_id=user_id, task_id=task_id).all()
    else:
        return FocusSession.query.filter_by(user_id=user_id).all()
    
    

def delete_focus_session(session_id):
    session = FocusSession.query.get(session_id)
    if session:
        db.session.delete(session)
        db.session.commit()
        return True
    return False
    

#return how many hours the user has spent in focus sessions
def get_total_focus_time(user_id):
    sessions = FocusSession.query.filter_by(user_id=user_id).all()
    total_minutes = sum(session.actual_minutes for session in sessions if session.actual_minutes)
    return total_minutes // 60, total_minutes % 60  # Return hours and minutes

def get_total_focus_time_by_task(user_id,task_id):
    sessions = FocusSession.query.filter_by(user_id=user_id, task_id=task_id).all()
    total_minutes = sum(session.actual_minutes for session in sessions if session.actual_minutes)
    return total_minutes // 60, total_minutes % 60  # Return hours and minutes


def get_focus_session_by_id(session_id,user_id=None):
    sessions = FocusSession.query.filter_by(id=session_id, user_id=user_id).first()
    if sessions:
        return sessions

    
    