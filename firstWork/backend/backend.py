#мне нужен веб сервис с веб галереей моих любимых людей - дедушки и конечно же володи! мои кумиры ! для них точно необходимо создать личный веб-сайт 

#хочу чтоб фронтенд выглядел так как я нарисовал щас окей теперь решаем бек энд - смотри будет бд бд хранит дату, кому принадлежит да получается фото может загрузить любой человек, что странно конечно, но предположу что у дедушки и володи много кумиров. хорошо что бы реализовать это потребуется ознакомится с документацией я выбираю стек - python, flask, html, postgress sql, sqlalchemy


#поля для бд нам точно нужны

#id

#name

#photoPath
from flask import Flask, render_template, request, send_from_directory,redirect, url_for

from BdConnect import GetObjectInBd
from BdConnect import SetObjectInBd
import os
#class CentralObj:
#    def My():
#

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
MyFolderForVolodia = os.path.join(basedir, '..', 'uploads')
app.config['UPLOAD_FOLDER'] = os.path.normpath(MyFolderForVolodia)




@app.route("/")
def home():
    return render_template("MyFronthend.html")

#Block Volodya only
@app.route('/clickVolodya', methods=['POST'])
def handle_click():
    print("Кнопка нажата! Данные получены.")
    return  render_template("Volodya.html")


@app.route('/PhotoFetchV', methods=['POST'])
def upload_file():
    file = request.files['avatar']
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    print(full_path)
    SetObjectInBd.SetUser("Volodya", full_path)
    

    return "this stub"


#Block dedushka only

@app.route('/clickDedushka', methods=['POST'])
def handle_click1():
    print("Кнопка нажата! Данные получены.")
    return render_template("Dedushka.html")

@app.route('/PhotoFetchD', methods=['POST'])
def upload_file1():
    file = request.files['avatar']
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    print(full_path)
    SetObjectInBd.SetUser("Dedushka", full_path)
    return "this stub"


@app.route('/show_user')
def show_user():
    obj = GetObjectInBd()
    full_patch  = obj.GetPhoto(14)
    print(full_patch)
    only_name = os.path.basename(full_patch) 
    return redirect(url_for('serve_photo', filename=only_name))

@app.route('/uploads/<filename>')
def serve_photo(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/clickGallory', methods=['POST'])
def gallory():
    db = GetObjectInBd()
    clean_friends = []
    frends = db.GetAllFriends()
    for name, full_path in frends:
        filename = os.path.basename(full_path)
        clean_friends.append({'name': name, 'photo': filename})
    return render_template('gallery.html', friends=clean_friends)


if __name__ == "__main__":
    app.run(debug=True)


#--create table animators(
#--id serial primary key,
#--nickname varchar(100) not null
#--);

#--create table toys(
#--id serial primary key,
#--price numeric(10,2),
#--form varchar(255),
#--animator_id int not null,
#--foreign key (animator_id) references animators(id)
#--)

#--create table buyers(
#--id serial primary key,
#--email varchar(100) not null,
#--password varchar(100) not null
#--)