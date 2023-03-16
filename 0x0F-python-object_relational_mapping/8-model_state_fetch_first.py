#!/usr/bin/python3

'''
A script that prints the first state Object
from the database hbtn_0e_6_usa
'''


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db_url = "mysql://{}:{}@localhost:3306/{}".\
             format(username, password, database)
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(State).order_by(State.id).first()

    if obj is not None:
        print("{}: {}".format(obj.id, obj.name))
    else:
        print("Nothing")
