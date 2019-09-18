# Updating with a pickle file is similar to a manually formatted file, except that Python
# is doing all of the formatting weork for us

import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tommy Boy'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()