from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL


if __name__ == '__main__':
    from app import app
    app.run(debug=True)

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'restoran'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from restoran")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', restorans=data)


@app.route('/simpan', method=["POST"])
def simpan():
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("insert * from restoran (data) values (%s)", (nama))
    mysql.connection.commit()
    return redirect(url_for('home'))


@app.route('/update', method=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("update restoran set data=%s where id=%s", (nama, id_data))
    mysql.connection.commit()
    return redirect(url_for('home'))


@app.route('/hapus', method=["POST"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("delete from restoran where id=%s", (id_data))
    mysql.connection.commit()
    return redirect(url_for('home'))


# class Resep(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String(50), nullable=False)
#     katgeori = db.Column(db.String(20), nullable=False)


# class Bahan(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String(50), nullable=False)
#     jumlah = db.Column(db.String(20), nullable=False)


# class BahanMakanan(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     resep_id = db.Column(db.Integer, db.ForeignKey('resep_id'))
#     bahan_id = db.Column(db.Integer, db.ForeignKey('bahan_id'))


# if __name__ == '__main__':
#     db.create_all()
#     db.run(debug=True)


# @app.route("/resep")
# def resep():
#     cursor = MySQL.connection.cursor()
#     cursor.execute('select * from resep')
#     resep = cursor.fetchall()
#     cursor.close()

#     return render_template('index.html', resep=Resep)


# class Resep(db.Model):
#     id_resep = db.Column(db.Integer(), primary_key=True)
#     nama = db.Column(db.String(255), nullable=False)
#     instruksi = db.Column(db.Text(), nullable=False)

#     def __repr__(self):
#         return self.nama

#     @classmethod
#     def get__all(cls):
#         return cls.query.all()

#     @classmethod
#     def get__by__id(cls, id):
#         return cls.query.get__or__404(id)

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# class ResepSchema(Schema):
#     id_resep = fields.Integer()
#     nama = fields.String()
#     instruksi = fields.String()
