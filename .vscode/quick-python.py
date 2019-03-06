#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass

#%%
'''define function and call function'''
def square_sum(a,b):
	a = a**2
	b = b**2
	c = a + b
	return c
	print ("I am here.")
x = square_sum(3,4)
print (x)
