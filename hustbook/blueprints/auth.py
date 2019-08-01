'''
@Description: 
@Author: Wu Xie
@Github: https://github.com/shiehng
@Date: 2019-07-23 23:23:57
'''
from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('')

@auth_bp.route('/logout')
def logout():
    pass

