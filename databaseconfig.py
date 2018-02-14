from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


Base = automap_base()
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/mydb')
session = Session(engine)
Base.prepare(engine,reflect=True)

Users = Base.classes.users
Courses = Base.classes.courses

