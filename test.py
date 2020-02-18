from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *

import pandas as pd
import csv
import os
import sys

text = u'すもももももももものうち'
path = "./data.csv"

def create_first_dataframe():
	with open(path, mode = "w") as f:
		#csvにデータを追加
		
		
		
def exec_analyser(text):
	
	#解析　名詞だけ取り出す
	token_filters = [POSKeepFilter(['名詞']), TokenCountFilter(sorted=True)]
	a = Analyzer(token_filters=token_filters)
	col_list = []
	value_list = []
	for k, v in a.analyze(text):
		col_list.append(k)
		value_list.append(v)
	return (col_list,value_list)	

def file_io():
	if os.path.exists(path):
		with open(path, "r") as f:
			#データフレームの作成
			df = pd.read_csv(f, sep = ",")
			s = pd.Series(value, index=collist, name=len(df))
			df_append = df.append(s)
	with open(path, mode = "w") as f:
		df_append.to_csv(f, mode="w")
		

def main():
	
	
		
			
if __name__ == "__main__":
    main()
