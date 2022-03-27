import pandas as pd
def usuarios(df_tweets, df_users):
  freq = df_tweets['userId'].value_counts() 
  freq = freq.head(10)
  df_user_freq = pd.DataFrame({'userId': freq.index, 'frecuencia': freq})
  df_user_freq.index = [0, 1,2,3,4,5,6,7,8,9]
  left_join = pd.merge(df_user_freq, df_users, how='left', on='userId')
  return left_join[['userId', 'frecuencia', 'username', 'displayname']].head(10)