#coding=utf-8
import tkinter.filedialog as flog
from flask import render_template
from flask import Flask
import json


app = Flask(__name__)

"""
class Info:
    def __init__(self, infoList):
        self.title = "ServerInfo"

        self.lis = infoList
        self.infoList = infoList
        self.cpu1 = self.infoList[0]["cpu"]
        self.cpu2 = self.infoList[1]["cpu"]
        self.cpu3 = self.infoList[2]["cpu"]
        self.cpu4 = self.infoList[3]["cpu"]

        self.memory1 = self.infoList[0]["memory"]
        self.memory2 = self.infoList[1]["memory"]
        self.memory3 = self.infoList[2]["memory"]
        self.memory4 = self.infoList[3]["memory"]

        self.disk1 = self.infoList[0]["disk"]
        self.disk2 = self.infoList[1]["disk"]
        self.disk3 = self.infoList[2]["disk"]
        self.disk4 = self.infoList[3]["disk"]
"""
jsonfile = flog.askopenfilename(title = '选择json文件')
with open(jsonfile, "r" ,encoding="utf-8") as rf:
    
    dic = json.load(rf)


@app.route('/')
def index():
    """传入的dic为各个服务器的最新数据，日数据，周数据和月数据
    """
    lis = dic["now"]
    # info = Info(lis)
    return render_template("show.html", info = lis)


@app.route('/now')
def now():
    lis = dic["now"]
    return render_template("show.html", info = lis)

@app.route('/hour')
def hour():
    lis = dic["hours"]
    return render_template("show.html", info = lis)

@app.route('/day')
def day():
    lis = dic["days"]
    return render_template("show.html", info = lis)

@app.route('/week')
def week():
    lis = dic["weeks"]
    return render_template("show.html", info = lis)

@app.route('/CPU-PID')
def cpupid():
    lis = dic["hours_list"]
    return render_template("CPU_PID.html", info = lis)


@app.route('/Memory-PID')
def memorypid():
    lis = dic["hours_list"]
    return render_template("Memory_PID.html", info = lis)


@app.route('/calendar-pie')
def calendarPie():
    lis = dic["day_list"]
    return render_template("calendar-pie.html", info = lis)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9971)
