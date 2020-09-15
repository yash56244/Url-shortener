from main import app, db
from flask import render_template, redirect, request
from main.models import URLMapping

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/link_shorterned', methods=['POST'])
def shortern_url():
    original_url = request.form['url']
    url = URLMapping(original_url=original_url)
    db.session.add(url)
    db.session.commit()
    return render_template('final.html', original_url=original_url, shortened_url=url.shortened_url)

@app.route('/<string:shortened_url>')
def redirectu(shortened_url):
    url = URLMapping.query.filter_by(shortened_url=shortened_url).first()
    url.visits += 1
    db.session.commit()
    return redirect(url.original_url)

@app.route('/all_urls')
def all_urls():
    urls = URLMapping.query.all()
    return render_template('all_urls.html', urls=urls)