# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Flask
from apps.index.view import index_blueprint
from apps.form.view import form_blueprint
from apps.ui_fitures.view import fitures_blueprint
from apps.widgets.view import widgets_blueprint
from apps.charts.view import chart_blueprint
from apps.tables.view import table_blueprint
from apps.pages.view import pages_blueprint


app = Flask(__name__, template_folder="..\\ui\\templates", static_folder="..\\ui\\static")
app.register_blueprint(index_blueprint)
app.register_blueprint(form_blueprint)
app.register_blueprint(fitures_blueprint)
app.register_blueprint(widgets_blueprint)
app.register_blueprint(chart_blueprint)
app.register_blueprint(table_blueprint)
app.register_blueprint(pages_blueprint)

