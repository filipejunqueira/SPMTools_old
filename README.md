# **SPMTools** - Welcome to some random stuff I made to help me analise my LT AFM/STM data!

All this stuff was made to be used with **The All Mighty Omicron's** systems folders and files.
We use python here. So before you begin I suggest you create a conda env with python 3.7+. 
Good luck going thorough my terrible writen code. 
 
# **The scripts**

There are at the moment a few scripts and 1 module (a bunch of functions in the same file).

## *spmFunctions.py*

This is module that contains a few functions that are useful in most scripts.
The most important functions are:
### import_matrix_file()
```python
import_matrix_file(series_number, file_path)
return image im
```
image and im are objects which contains all the information that is spit out by matrix, if it exists iit is there.

### load_spec():
This function receives a .txt exported from vernisage and spits out information about the spectroscopy curve. 
```python
load_spec(file_path)
return data_forward, data_retrace, data_size, spec_position, data, spec_object
```
There is a lot of redundancy here. spec_object contains all the info you need.\
This needs to be changed later so it only returns one thing.  

#### plot_spec(file_path)
```python
plot_spec(file_path)
return True
```
This plots and saves a graph of a spec file (.txt).

#### loadspecscript.py

This script loads a .txt spectroscopy curve generated from a export using vernisage.
It assumes you went fowards and backwards with your spectroscopy (which you should always do btw!).

#### gwideontracesimport.py

Imports a gwideon profile trace and creates a nice neat little graphic. 

## *Df_averaging.py*

So this one grabs a file (any Z, DF, I .matrix file) and avarages each row. 
Useful when you want to know how the Df has been varing on your constant Df image. 
Can be done the same for I (for STM images).

## *SpecPositionOnImage.py*

I really need to name my scripts better. This grabs the position of a bunch specs
and the correspondent image in which it has been taken and plots the positions of each spec on top of it. 
Sort of how vernisage does it. 

Still a work in progress...
