import pandas as pd
def hashtags(df_tweets):
  lista_hash = []
  lista_indices = df_tweets.index 
  for i in range(len(df_tweets)):
    if i in lista_indices:
      tweet = df_tweets['renderedContent'][i]
      tweet = tweet.replace("\n", "")
      tweet = tweet.split(" ") 
      for j in tweet:
        if "#" in j:
          d = j.find("#")
          hash = j[d+1::]
          hashtags = hash.split("#")
          for k in hashtags:
            lista_hash.append(k)
  
  df_hasthtags = pd.DataFrame({'hashtag': lista_hash})
  freq = df_hasthtags['hashtag'].value_counts() 
  freq = freq.head(10)
  df_hash_freq = pd.DataFrame({'hashtag': freq.index, 'frecuencia': freq})
  df_hash_freq.index = [0, 1,2,3,4,5,6,7,8,9]
  
  return df_hash_freq