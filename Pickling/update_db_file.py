# makes changes by loading, updating, and storing again

from FormattedFiles.make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tommy Boy'
storeDbase(db)