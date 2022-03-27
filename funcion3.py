import pandas as pd
def dias(df_tweets):
  df_tweets2 = df_tweets
  fechas = []
  for i in df_tweets2['date']:
    fechas.append(f"{i.year}-{i.month}-{i.day}")
  df_tweets2['fecha'] = fechas
  
  freq = df_tweets2['fecha'].value_counts() 
  freq = freq.head(10)
  df_date_freq = pd.DataFrame({'date': freq.index, 'frecuencia': freq})
  df_date_freq.index = [0, 1,2,3,4,5,6,7,8,9]
  return df_date_freq