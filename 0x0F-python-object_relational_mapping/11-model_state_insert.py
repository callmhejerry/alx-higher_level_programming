#!/usr/bin/python3

'''
A script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
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

    newObj = State()
    newObj.name = "Louisiana"
    session.add(newObj)
    session.commit()
    print(newObj.id)
