#!/usr/bin/python3

'''
A script that lists all the state objects
that contains the letter a from the database hbtn_0e_6_usa
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

    objs = session.query(State)\
        .filter(State.name.like("%a%"))\
        .order_by(State.id).all()

    for obj in objs:
        print("{}: {}".format(obj.id, obj.name))
