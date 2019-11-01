# Random-groups
Create random group for any database ( the same as fold in crossvalidation)


The function will randomly divide database per dimension and assign an Id Group per group .
I developed it during a machine learning project to create a new feature for my data set. 

HOW IT WORKS ? 
  1. it defines the list of item that we will use to divide database
  2. Calculate the number of item per group 
  3. It randomly select the number of item , assign them a group number and store it in file. 
  4. It does it again for the remaining item until it left no more item. 
  5. It merge the file with the database 

PARAMETERS 
  df = panda database 
  dimension = dimension used  to split accordingly 
  nb_fold = number of group to create 
  random_state = random spliting 


LIBRAIRIES 
  import numpy as np
  import pandas as pd
  
