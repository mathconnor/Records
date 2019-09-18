# updates the database by fetching a record from its file, changing it in memory, and the writing it
# back to its pickle file. This time, we have to fetch and rewrite only a single record file,
# not the full database, to upodate

import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.1
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()