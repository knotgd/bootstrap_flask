# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

fitures_blueprint = Blueprint('fitures', __name__)


@fitures_blueprint.route('/fitures/components', methods=['GET', 'POST'])
def fitures_components():
    return render_template('general.html', )


@fitures_blueprint.route('/fitures/button', methods=['GET', 'POST'])
def fitures_button():
    return render_template('buttons.html', )


@fitures_blueprint.route('/fitures/grids', methods=['GET', 'POST'])
def fitures_grids():
    return render_template('grids.html', )
