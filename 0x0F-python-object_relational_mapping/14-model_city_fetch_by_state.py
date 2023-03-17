#!/usr/bin/python3

'''
A script that prints all the City objects from the
database hbtn_0e_14_usa
'''


if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
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

    objs = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id).all()
    # print(objs)
    for city, state in objs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
