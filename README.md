# SPMTools - Welcome to random stuff I made to help me analise my LT AFM/STM data!

All this stuff was made to be used with **The All Mighty Omicron's** systems folders and files.
We use python here. So before you begin I suggest you create a conda env with python 3.7+. 
Good luck going thorough my terrible writen code. 
 
# The scripts

There are at the moment 4 scripts and 1 module (a bunch of functions in the same file).

## loadspecscript.py

This script loads a .txt spectroscopy curve generated from a export using vernisage.
It assumes you went fowards and backwards with your spectroscopy (which you should always do btw!).

## gwideontracesimport.py

imports a gwideon profile trace and creates a nice neat little graphic. 

## Df_averaging.py

So this one grabs a file (any Z, DF, I .matrix file really) and avarages each row. 
Useful when you want to know how the Df has been varing on your constant Df image. 
Can be done the same for I (for STM images).

## SpecPositionOnImage.py

I really need to name my scripts better. This grabs the position of a bunch specs
and the correspondent image in which it has been taken and plots the positions of each spec on top of it. 
Sort of how vernisage does it. 

Still a work in progress...
