import mtranslate as mt
import pandas as pd
import time

def Translate():
	df = pd.read_csv("datasettotranslate.csv")
	for i in range(len(df)):
		df["Text"][i] = mt.translate(df["Text"][i],"en","tr") # translate(text to string,desired language,base language)
		print(i)
	df.to_csv("translated.csv")
