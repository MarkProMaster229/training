from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('postgresql://postgres:1@localhost/MyData')

class GetObjectInBd():

    
    def GetName(self, number):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT name FROM MyFrend LIMIT 1 OFFSET {number}")).fetchall()

        conn.close()
        return result[0][0] if result else "Никого не нашли"

    def Getid(self, number):
        conn = engine.connect()

        result = conn.execute(text(f"SELECT id FROM MyFrend LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"

    def GetPhoto(self,number):
        conn = engine.connect()
        
        result = conn.execute(text(f"SELECT photopatch FROM MyFrend LIMIT 1 OFFSET {number}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetAllFriends(self):
        conn = engine.connect()
        result = conn.execute(text("SELECT name, photopatch FROM MyFrend")).fetchall()
        conn.close()
        return result

        
class SetObjectInBd():
    def SetUser(name, photo_path):
        conn = engine.connect()
        query = text("INSERT INTO MyFrend (name, photopatch) VALUES (:name, :path)")
        conn.execute(query, {"name": name, "path": photo_path})
        conn.commit()
        conn.close()

        
#мне нужен веб сервис с веб галереей моих любимых людей - дедушки и конечно же володи! мои кумиры ! для них точно необходимо создать личный веб-сайт 

#хочу чтоб фронтенд выглядел так как я нарисовал щас окей теперь решаем бек энд - смотри будет бд бд хранит дату, кому принадлежит да получается фото может загрузить любой человек, что странно конечно, но предположу что у дедушки и володи много кумиров. хорошо что бы реализовать это потребуется ознакомится с документацией я выбираю стек - python, react, fastAPI, postgress sql, sqlalchemy


#поля для бд нам точно нужны

#id

#name

#photoPath

#нейросетями пользоваться - ЗАПРЕЩАЮ СУКА СКОЛЬКОБЫ У ТЕБЯ НЕ УШЛО ВРЕМЕНИ ХОТЬ ОБОСРИСЬ НО ПОЛЬЗОВАТЬСЯ НЕРОСЕТЯМИ ЗАПРЕЩЕНО - ЭТО БОЛЕЗНЬ ЭТО РАК!!! (можно но немного если только иначе я просто сейчас не справлюсь) 




