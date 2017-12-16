import sys,getopt
opts,args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])

print ("opts",opts)
print ("args",args)
