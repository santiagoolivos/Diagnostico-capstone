def mas_retweeted(df_tweets):
  df_mas_retweet = df_tweets.sort_values('retweetCount', ascending=False)
  return df_mas_retweet.head(10)
