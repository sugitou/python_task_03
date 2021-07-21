import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

text = ''

@ eel.expose
def kimetsu_search(word, csv_file):
    search_result = search.kimetsu_search(word, csv_file)
    text = search_result
    print('text', text)

eel.init("web")
eel.view_log_js(text)
eel.start("index.html")
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)