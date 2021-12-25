#!/usr/bin/python3
""" Write a script that lists all State objects from the,
database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)
    Session = session().query(State).all()
    for state in Session:
        print("{}: {}".format(state.id, state.name))
    session().close()
