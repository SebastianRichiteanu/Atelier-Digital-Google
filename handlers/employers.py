from .database import DatabaseHandler
from models.employers import Employer


def delete_employer(employer):
    session = DatabaseHandler.session
    db_employer = session.query(Employer).filter(Employer.name == employer.name)
    db_employer.delete()
    session.commit()


def add_employer(employer_name):
    session = DatabaseHandler.session
    sql_query = "INSERT INTO employers (name) values ('" + employer_name + "')"
    session.execute(sql_query)
    session.commit()


def edit_employer(old_employer, new_employer):
    session = DatabaseHandler.session
    sql_query = "UPDATE employers set name = ('" + new_employer + "') where name = '" + old_employer + "'"
    session.execute(sql_query)
    session.commit()
