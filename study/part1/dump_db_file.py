from make_db_file import loadDbase, storeDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
db['sue']['pay'] *=1.1
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
