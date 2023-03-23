#!/usr/bin/python3

'''
A script that creates the State 'California' with the city
'San Francisco' from the database [hbtn_0e_100_usa]
'''

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    username = argv[1]
    password = argv[2]
    db = argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
             format(username, password, db)

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add state and city to session
    ca_state = State(name='California', cities=[City(name='San Francisco')])
    session.add(ca_state)

    # Commit changes to database
    session.commit()

    # Close session
    session.close()