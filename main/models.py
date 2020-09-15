import uuid
from main import db

class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(100), nullable=False)
    shortened_url = db.Column(db.String(5), unique = True)
    visits = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortened_url = self.generate_short_link()

    def generate_short_link(self):
        rhash = uuid.uuid4().hex
        shortened_url = rhash[:5]
        already = self.query.filter_by(shortened_url=shortened_url).first()
        if already:
            return self.generate_short_link()
        return shortened_url