from flask import render_template, redirect, url_for, abort, flash, request
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
