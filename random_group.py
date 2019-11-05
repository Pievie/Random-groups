def fold (df,dimension,nb_fold = 100,random_state = 42 ):
    """
    Define randomly different group id per item ( as fold )
    Parameters : df = panda database , dimension = dimension used  to split accordingly ,
    nb_fold = number of group to create , random_state = random spliting 
    """
    if nb_fold > df[dimension].nunique() :
       return print(' Number of group is higher than the nb of entity.\n It is impossible to assign a group per entity.\n\n >>> Review parameter nb_fold' )
        
    else :
        print(df[dimension].nunique(),'Items to split in ',nb_fold,'groups' )
        df_item= df[dimension].drop_duplicates(keep = 'first', inplace = False).to_frame().copy()
        
        nb_item = len(df_item)
        fold_size = int(np.trunc(nb_item/nb_fold)) #define the number of item per folds
        df_fold = pd.DataFrame()
        
        for j in range(nb_fold) :
            fold_number = j
            id_fold = df[dimension].sample(n=fold_size, random_state=42).to_frame() # define random item  (random_state to get all the time the same randomisation )
            id_fold  = id_fold .assign(fold_number=fold_number) # assign the id number to the fold 
            
            for i in id_fold[dimension]: 
                df_item = df_item[df_item.ItemKey !=i] # remove the item from the list to avoid the same random sampling in the next iteration
            #df_item = pd.merge(df_item, id_fold, how = 'left', on = 'ItemKey' ).fillna(-1)# merge fold_id with dataframe  
            #df_item = df_item[df_item['fold_number']<0]
            df_fold =     df_fold.append(id_fold) # append the created id to the existing id_fold 
        
            print(str(int((len(df_fold) / nb_item )* 10 ** (1 + 2)) / (10 ** (1))) + '%')# print percentage 
        
        
        # do the last iteration outside the loop to include the reamining items 
        id_fold =  df_item.copy()
        del df_item
        fold_number = nb_fold+1    
        id_fold  = id_fold .assign(fold_number=fold_number) # assign the id number to the fold 
        df_fold =     df_fold.append(id_fold) # append the created id to the existing id_fold 
        
        # Merge the group id with the original dataframe 
        df = pd.merge(df, df_fold, how = 'left', on = dimension )# merge fold_id with dataframe
    print( 'Group index created')
    return df
   
