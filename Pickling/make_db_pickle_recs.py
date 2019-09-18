# Stores each record in its own flat file, usingg each record's original key as its filename
# with a .pkl appended

from initdata import bob, sue, tom
import pickle
for(key, record) in [('bob', bob), ('tom', tom), ('sue', sue),]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()