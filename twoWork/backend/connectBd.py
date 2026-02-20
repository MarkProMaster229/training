from sqlalchemy import create_engine
from sqlalchemy import text


engine = create_engine('postgresql://postgres:1@localhost/MyData')

#getters
class GetAnimators():
    def GetID(number):
        conn = engine.connect()
        
        result = conn.execute(text(f"SELECT ID FROM animators LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetNickname(name):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT nickname FROM animators LIMIT 1 OFFSET{name}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    

class GetToys():
    def Getid(number):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT ID FROM toys LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetPrice(number):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT price FROM toys LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
class GetBuyers():
    def Getid(number):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT ID FROM buyers LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetEmail(Email):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT Email FROM buyers LIMIT 1 OFFSET {Email}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetPassword(Password):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT password FROM buyers LIMIT 1 OFFSET {Password}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
#setters

class SetMethod():
    def SetAnimator(name):
        conn = engine.connect()
        query = text("INSERT INTO animator (name) VALUES (:name)")
        conn.execute(query,{"name":name})
        conn.commit()
        conn.close()

    def SetToys(price):
        conn = engine.connect()
        query = text("INSERT INTO toys (price) VALUES (:price)")
        conn.execute(query,{"price":price})
        conn.commit()
        conn.close()

    def Buyers(email, password):
        conn = engine.connect()
        query = text("INSERT INTO buyers (email, password) VALUES (:email, :password)")
        conn.execute(query,{"email": email, "password": password})
        conn.commit()
        conn.close()

        

#--create table animators(
#--id serial primary key,
#--nickname varchar(100) not null
#--);
#--SELECT ID
#--FROM animators
#--LIMIT 1 OFFSET 0

#--SELECT nickname 
#--FROM animators 
#--LIMIT 1 OFFSET 0


#--create table toys(
#--id serial primary key,
#--price numeric(10,2),
#--form varchar(255),
#--animator_id int not null,
#--foreign key (animator_id) references animators(id)
#--)
#--SELECT ID FROM toys
#--LIMIT 1 OFFSET 0

#--SELECT price FROM toys LIMIT 1 OFFSET 0


#--create table buyers(
#--id serial primary key,
#--email varchar(100) not null,
#--password varchar(100) not null
#--)

#--SELECT ID FROM buyers LIMIT 1 OFFSET 
#--SELECT Email FROM buyers LIMIT 1 OFFSET 0
#--SELECT password FROM buyers LIMIT 1 OFFSET 0


#--INSERT INTO animator nickname VALUES (:name, :path)

