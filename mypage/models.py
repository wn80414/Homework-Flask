from mypage import db

class City(db.Model):
    city_name = db.Column(db.String(80), unique=True, nullable=False)
    city_rank = db.Column(db.Integer, primary_key=True)
    def __repr__(self):
        return f'{self.city_name}'
