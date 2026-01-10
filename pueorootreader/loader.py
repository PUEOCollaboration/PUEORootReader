'''This module handles functions related to file fetching'''

# Don't have the root file locally? No problem! All you need is this function, and... patience :)
def seekRootFile(run, chunk, user='', password=''):
    '''Seek the data ROOT file path from online. These files come from "/data/pueo/starlink-offline/rootified/". 
    The run and chunk refer to the subdirectory and saved data chunk (100, 200, ...).'''
    return f'https://{user}:{password}@pueo.uchicago.edu/data/pueo/starlink-offline/rootified/run{run:04d}/{chunk:06d}.root'