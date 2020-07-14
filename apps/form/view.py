# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

form_blueprint = Blueprint('form', __name__)


@form_blueprint.route('/form/component', methods=['GET', 'POST'])
def form_component():
    return render_template('form_component.html', )


@form_blueprint.route('/form/validation', methods=['GET', 'POST'])
def form_validation():
    return render_template('form_validation.html', )

