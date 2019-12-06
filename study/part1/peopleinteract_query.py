import shelve

db = shelve.open('class-shelve')
fieldname = ('name', 'age', 'pay', 'job')
maxfield = max(len(n) for n in fieldname)
while True:
    key = input('\nKey =>')

    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldname:
            print(field.ljust(maxfield), '=>', getattr(record, field))

db.close()
