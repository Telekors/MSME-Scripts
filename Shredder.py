###SHREDDER Created by: Mason Helphrey
import sys, time
from mfe_saw.esm import ESM
from mfe_saw.datasource import DataSource, DevTree
print ("###########")
print ("# WARNING #")
print ("###########")
print("")
print ("############")
print ("# SHREDDER #")
print ("############")
####FAIL SAFE
sys.stdout.write("Enter 'yes' to continue: ")
# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input().lower()
if choice in yes:
   x = ''
elif choice in no:
   print('QUITTING')
   time.sleep(.5)
   quit()
else:
   print('QUITTING')
   time.sleep(.5)
   quit()




header = "Objects to delete"

#Login to ESM print time and mount the tree
esm = ESM()
esm.login('10.10.10.10', 'NGCP', 'Password(TOBECHANGED)')
print(esm.time())
tree = DevTree()
print(len(tree))
beforedelete = len(tree)

#open files
o = open("output.csv", "w")
o.write(header)  
with open("input.csv") as f:
	content = f.readlines()
content = [x.strip('\n') for x in content]
##DEBUG     print(content)
##DEBUG     yammer = tree.search('pbisfxprd299')
##DEBUG     print(yammer.name)

#Iterate through input and print
for x in content:
	#print(x)
	if not x == '': #THIS LINE EXISTS TO PREVENT DELETING ESM!!!!
		y = tree.search(x)
		#print (y.name)
		try:
			y.delete(),
			time.sleep(1)
			print (x)
			print (y.name+" deleted."),
		except AttributeError:
			print("NoneError: "+x)


tree.refresh()

sys.stdout.write("Before Delete: ")
print(beforedelete)
sys.stdout.write("After Delete: ")
print(len(tree))
o.close()
