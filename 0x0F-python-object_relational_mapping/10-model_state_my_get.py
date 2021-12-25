#!/usr/bin/python3
""" Write a script that prints the State object with,
the name passed as argument from the database hbtn_0e_6_usa
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
    state = session().query(State).filter(State.name == argv[4]).all()
    if state:
        for states in state:
            print(states.id)
        else:
        print("Not found")
    session().close()
