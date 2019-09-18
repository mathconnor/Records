# dumps the entire database by using the standard library's glob module to do a filname expansion
# and thus collect all the fields in this directory with a .pkl extension. To load a single record,
# we open its file and deserialize with pickle; we must load only one record file, though, not the
# entire database, to fetch one record.

import pickle
import glob

for filename in glob.glob('*pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, ' => ', record)


suefile = open('sue.pkl', 'rb')
print(f"sue's name: {pickle.load(suefile)['name']}")