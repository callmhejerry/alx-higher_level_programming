#!/usr/bin/python3

'''
A script that lists all state objects, and
corresponding City object, contained in the database
[hbtn_0e_101_usa]
'''


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from relationship_city import City
    from relationship_state import State, Base
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    db_url = "mysql://{}:{}@localhost:3306/{}".\
             format(username, password, db)
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    states = session.query(State, State.cities).filter(State.id == City.id)\
        .order_by(State.id, City.id).all()
    for obj in states:
        (state, bools) = obj
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
