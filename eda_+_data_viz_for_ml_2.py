import pandas as pd

def eda(df):
  print(f'*** SHAPE ***\n {df.shape}\n\n')
  print(f'*** INFO ***')
  print(f'{df.info()}\n\n')
  print(f'*** SAMPLE ***\n{df.sample(10)}\n\n')
  print(f'*** MISSING VALUES ***\n {df.isnull().sum()}\n\n')
  print(f'*** DESCRIBE *** \n {df.describe()}\n\n')
  print(f'*** COLUMN HEADINGS ***\n {df.columns}\n\n')
  print(f'*** COLUMN FEATURES ***')
  for i in df.columns:
    print(i,len(df[i].unique()))
  print(f'\n\n*** FEATURES WITH <20 UNIQUE VALUES***')
  for i in df.columns:
      if len(df[i].unique())<20:
          print(f'{i} has {len(df[i].unique())} unique values: {df[i].unique()}')
