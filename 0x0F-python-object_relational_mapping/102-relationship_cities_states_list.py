#!/usr/bin/python3

'''
A script that lists all the City from the
database [hbtn_0e_101_usa]
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

    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
