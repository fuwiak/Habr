import cyrtranslit
import pandas as pd 



df = pd.read_csv('songs.csv')
df = df[['name','text']]

df.text = df.text.apply(lambda x: cyrtranslit.to_latin(x, 'ru'))

df.text.to_csv('trans.csv')


from textgenrnn import textgenrnn
textgen = textgenrnn()
textgen.train_from_file('trans.csv', num_epochs=1)