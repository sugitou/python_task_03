import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, csv_file):
    search.kimetsu_search(word, csv_file)

eel.init("web")
eel.view_log_js('test')
eel.start("index.html")
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)