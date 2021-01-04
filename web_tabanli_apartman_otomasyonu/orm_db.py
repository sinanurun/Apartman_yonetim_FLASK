from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import label
from datetime import datetime

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Qwev8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///araptman_otomasyon.db'

db = SQLAlchemy(app)
dbsession = db.session()

class Uye(db.Model):

    uye_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    uye_adi_soyadi = db.Column(db.String(50), nullable=False)
    uye_tc = db.Column(db.String(11), unique=True, nullable=False)
    uye_tel = db.Column(db.String(11), nullable=False)
    uye_adres = db.Column(db.String(250))
    uye_sifre = db.Column(db.String(10), nullable=False)
    uye_email = db.Column(db.String(50))
    uye_durum = db.Column(db.Integer, nullable=False)
    uye_yonetim = db.Column(db.Integer)


class Aidat(db.Model):

    aidat_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    aidat_yonetici_id = db.Column(db.Integer, db.ForeignKey('uye.uye_id'), nullable=False)
    aidat_uye_id = db.Column(db.Integer, db.ForeignKey('uye.uye_id'), nullable=False)
    yonetici = db.relationship('Uye', backref=db.backref('aidat_yonetici', lazy=True),
                               foreign_keys=[aidat_yonetici_id])
    aidatuye = db.relationship('Uye', backref=db.backref('aidat_uye', lazy=True),
                               foreign_keys=[aidat_uye_id])
    aidat_tutari = db.Column(db.Float, nullable=False)
    aidat_tarihi = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    aidat_aciklama = db.Column(db.String(500), nullable=False)


class Gider(db.Model):
    gider_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    gider_yonetici_id = db.Column(db.Integer, db.ForeignKey('uye.uye_id'), nullable=False)
    gideryonetici = db.relationship('Uye', backref=db.backref('gideryonetici', lazy=True),
                                    foreign_keys=[gider_yonetici_id])
    gider_tutari = db.Column(db.Float, nullable=False)
    gider_tarihi = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gider_aciklama = db.Column(db.String(500), nullable=False)


class Duyuru(db.Model):
    duyuru_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    duyuru_yonetici_id = db.Column(db.Integer, db.ForeignKey('uye.uye_id'), nullable=False)
    duyuruyonetici = db.relationship('Uye', backref=db.backref('duyuruyonetici', lazy=True),
                                    foreign_keys=[duyuru_yonetici_id])
    duyuru_basligi = db.Column(db.String(500), nullable=False)
    duyuru_tarihi = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duyuru_aciklama = db.Column(db.String(500), nullable=False)


class Sikayet(db.Model):

    sikayet_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    sikayet_uye_id = db.Column(db.Integer, db.ForeignKey('uye.uye_id'), nullable=False)
    sikayetuye = db.relationship('Uye', backref=db.backref('sikayet_uye', lazy=True),
                               foreign_keys=[sikayet_uye_id])
    sikayet_basligi = db.Column(db.String(500), nullable=False)
    sikayet_tarihi = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sikayet_aciklama = db.Column(db.String(500), nullable=False)



# veri tabanını oluşturmak için tabloyu oluşturmak için
db.create_all()