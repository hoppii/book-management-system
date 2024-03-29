import bottle
import lmdb
import json
#import tkinter
import time
import datetime


env = lmdb.Environment("./dblibrary")

def get_id(txn):
    cur = txn.cursor()
    ite = cur.iterprev()
    try:
        k, v = next(ite)
        last_id = int(k.decode("utf8"))
    except StopIteration:
        last_id = 0
    id = last_id + 1
    return "{:08d}".format(id)

@bottle.route("/")
def root():
    return bottle.static_file("registration.html", root="./static")


@bottle.post("/submit")
@bottle.view("submit")
def submit():
    title = bottle.request.params.title
    author = bottle.request.params.author
    publisher = bottle.request.params.publisher
    acquisitionDate = bottle.request.params.acquisitionDate
    status = "返却済"
    data = {"title": title, "author": author,
            "publisher": publisher, "acquisitionDate": acquisitionDate,
            "status": status}
    with env.begin(write=True) as txn:
        id = get_id(txn)
        txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
    return data    



@bottle.route("/list")
@bottle.view("list")
def list():
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            d["id"] = k
            data.append(d)
    for d in data:
        print(d)
    return {"data": data}


@bottle.get("/delete")
@bottle.view("delete")
def delete():
    id = bottle.request.params.id
    with env.begin(write=True) as txn:
        txn.delete(id.encode("utf8"))


@bottle.get("/checkout")
def checkout(): 
    d = datetime.datetime.now()
    rd = d + datetime.timedelta(days=30) 
    return bottle.template("list.tpl")
    
    #id = bottle.request.params.id  

    #with env.begin(write=True) as txn:
        #try:
            #b = txn.get(id.encode("utf8"))
            #s = b.decode("utf8")
            #s["status"] = "貸出中"
            #txn.put(id.encode("utf8"), s.encode("utf8"))
        #except Exception:
            #pass
    
        


"""
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            d["id"] = k
            data.append(d)
    for d in data:
        print(d)
    return {"data": data}
"""
    
        


bottle.run()
