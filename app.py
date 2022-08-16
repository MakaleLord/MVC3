#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, abort

from .posts import blog_posts
from .decorators import welcome_screen

app = Flask(__name__)

app.secret_key = 'DHDF4t44yyhj'

@app.route('/')
@welcome_screen
def home_page():
    return render_template('page.html', posts=blog_posts)

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/<post_link>')
@welcome_screen
def post_page(post_link):
    for post in blog_posts:
        if post['permalink'] == post_link:
            return render_template('post.html', post=post)
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
