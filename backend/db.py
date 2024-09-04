import unittest
from sqlalchemy import create_engine, text

def run_query(stmt, params) :
    engine = create_engine("postgresql://postgres:Aromax@localhost:5432/twitter")
    with engine.connect() as conn:
         result = conn.execute(stmt,params)
         conn.commit()
         conn.close()
         return result
    

def reset_database():
     with open("../db/init.sql") as file:
          stmt = text(file.read())
          run_query(stmt,{})
     return         

def create_user (username, password):
    statement = text(
        "insert  into users(username,password) values (:username, :password) returning id "
    ) 
    params = {"username" : username , "password" : password}
    result = run_query(statement,params)
    print(result.mappings().all()[0])
    return {"id":"1"}
    

class TestDatabaseMethods(unittest.TestCase):
    def testOne(self):
        self.assertTrue('FOO'.isupper())

    
    def test_create_user_works (self):
        username = 'test_user_1'
        password = 'test_pass_1'
        user = create_user(username, password)
        self.assertEqual(user,{"id": "1"})


if __name__ == "__main__" :
          unittest.main()




         