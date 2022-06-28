#%%
import pandas as pd
import os 
from tqdm import tqdm
#%%
def read_dat_file(filename):
    """
    Read .dat file, discards some row headers and returns appropriate values.
    Parameters
    ----------
    filename : string with path and filename do .dat file
    Returns
    -------
    df : pandas.DataFrame
        A pandas dataframe contatining the data.
    """
    df = pd.read_csv(filename, skiprows=3)
    df_aux = pd.read_csv(filename, header=1)
    df.columns = df_aux.columns

    cols_to_drop = ['RECORD', 'Excedente_Avg', 'Compra_Avg']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop([col], axis=1)

    for column in df.columns:
        if column != "TIMESTAMP":
            df[column] = df[column].astype('float')
    # Drop column 'RECORD' (if present) because from june 2019 is is no longer used
    return df

def get_list_of_files(folder):
    """
    Return a list of *.dat files inside the subfolders of folder 'folder'.
    Parameters
    ----------
    folder : string with path to root folder
    Returns
    -------
    lst : list
        A list containing all *.dat file strings
    """
    lst = []
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            complete_filename = os.path.join(root, name)
            # print(complete_filename)
            lst.append(complete_filename)
        for name in dirs:
            complete_filename = os.path.join(root, name)
            # print(complete_filename)
            lst.append(complete_filename)

    lst.sort()
    return [x for x in lst if '.dat' in x]