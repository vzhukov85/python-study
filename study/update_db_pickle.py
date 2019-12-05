if __name__ == '__main__':
    import pickle

    db_file = open('people-pickle', 'rb')
    db = pickle.load(db_file)
    db_file.close()

    db['sue']['pay'] = 30000
    db['tom']['name'] = 'Tom Tom'

    db_file = open('people-pickle', 'wb')
    pickle.dump(db, db_file)
    db_file.close()
