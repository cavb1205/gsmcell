from flask import render_template, request, redirect
from app import db
from . import inversion


@inversion.route('/')
def inversion_list():
    return ('hola inversiones')