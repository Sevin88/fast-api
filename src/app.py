from fastapi_offline import FastAPIOffline

app = FastAPIOffline()
mylist = [5, 10, 15, 20, 25, 30]
new_item = [20]
@app.get('/home/')

def home():
    return {'HELLO':'ME'}

@app.get('/getitems/')
def get_all_item():
    return {'mylist': mylist}

@app.post('/item/{new_item}')
def add_item(new_itme: int):
    mylist.append(new_item)
    return {'mylist': mylist}

@app.get('/get_item/{index}')
def get_item(index: int):
    if index >= len(mylist):
        return 'Index Not Found'
    else:
        return(f'Your item: {mylist:[index]}')
    
@app.get('/lastitem/')
def get_lastitem():
    if len(mylist) > 0:
        return (f'Your item: {mylist:[index[-1]]}')
    else:
        return 'List Is  Empty'
    
@app.put('/update_item/{new_item}')
def update_Byitem(old_item:int, new_item):
    index = 0
    if old_item in mylist:
        index = mylist.index(old_item)
        return {'New My List':mylist}
    else:
        return ('Item Not Found')
    
@app.put('/update_index/')
def update_Byindex(index:int, new_item:int):
    if index < len(mylist):
        mylist[index] = new_item
        return {'New My List':mylist}

@app.delete('/delete_Byitem/')
def delete_index(index:int):
    if index < len(mylist):
        result = mylist.pop(index)
        return (f'{result} Deleted From List')
    else:
        return ('Index Not Found')
    
@app.delete('/delete_item/')
def delete_item(item:int):
    if item in mylist:
        result = mylist.remove(item)
        return (f'{result} Deleted From List')
    else:
        'Item Not Found'

@app.get('/reverse_list/')
def get_reverse_list():
    return (f'Recovered List:{mylist[::-1]}')