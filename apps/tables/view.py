# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

table_blueprint = Blueprint('table', __name__)


@table_blueprint.route('/table', methods=['GET', 'POST'])
def tables_components():
    return render_template('basic_table.html', )

