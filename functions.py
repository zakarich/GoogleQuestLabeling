import numpy as np
import pandas as pd
import re
import os

def readCSV_DATA(PathData):

	df_dict = {}

	for file in os.listdir(PathData):
	    if file.endswith(".csv"):
	    	pathFinal = PathData+os.sep+file
	    	df_dict[file] = pd.read_csv(pathFinal)

	return df_dict

def visualizeSampleText(df):
    
    #Visualizing texts samples
    for i in np.random.randint(df.shape[0], size=(5)).tolist():
        print('\n----> Question title: <----\n')
        print(df.question_title[i])
        print('\n----> Question body: <----\n')
        print(df.question_body[i])
        print('\n----> Answer: <----\n')
        print(df.answer[i])


def prepareData(df):
    # Concat three main text columns
    df['text_all_concat'] = ['\n\n'.join([i,j,k]) for i,j,k in zip(df.question_title, df.question_body, df.answer)]
    # Clean numbers
    df['text_concat_filter'] = [re.sub('[0-9]+[^ ,.]*[0-9]*', '_num_', i) for i in df.text_all_concat]

    return df
