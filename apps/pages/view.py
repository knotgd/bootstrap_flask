# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint, request, jsonify
from flask import render_template

pages_blueprint = Blueprint('pages', __name__)


@pages_blueprint.route('/pages/profile', methods=['GET', 'POST'])
def page_profile():
    return render_template('profile.html', )


@pages_blueprint.route('/pages/test', methods=['GET', 'POST'])
def test_service():
    num = '-----'
    if request.method == 'POST':
        num = request.form['num']
    data = ["从后台传来的数据"+num]
    return render_template('test.html', data=data)


@pages_blueprint.route('/pages/test/ajax', methods=['GET', 'POST'])
def test_ajax_service():
    if request.method == 'POST':
        num = request.form['num']
        return jsonify(["从后台传来的数据"+num])

