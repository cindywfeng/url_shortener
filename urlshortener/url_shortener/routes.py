from flask import Blueprint, render_template, request, redirect

server = Blueprint('server', __name__)

from .extensions import db
from .models import URL

@server.route('/<short_url>')
def redirect_to_url(short_url):
    link = URL.query.filter_by(short_url = short_url).first_or_404()
    return redirect(link.long_url)

@server.route('/')
def index():
    return render_template('index.html')

@server.route('/add_url', methods=['POST'])
def add_url():
    long_url = request.form['long_url']
    link = URL(long_url=long_url)
    db.session.add(link)
    db.session.commit()

    return render_template('url_generated.html', 
        new_link = link.short_url, long_url=link.long_url)
    

@server.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404