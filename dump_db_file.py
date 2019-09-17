# reloads the database from a file each time it is run.

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, ' => ', db[key])
print(db['sue']['name'])