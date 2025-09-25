from database import session

def get_db():
    db = session()
    try:
        yield db # waiting for others to use
    finally:
        db.close()