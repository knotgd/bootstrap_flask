# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', )
