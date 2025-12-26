from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    num_messages= df.shape[0]
    words=[]
    for message in df['message']:
            words.extend(message.split())

    num_media_msg = df[df['message'] == '<Media omitted>\n'].shape[0]

    Links=[]
    for message in df['message']:
         Links.extend(extract.find_urls(message))



    return num_messages, len(words), num_media_msg, len(Links)

def most_busy_users(df):
    to_remove = ['group_notification', 'ERROR', 'Meta AI']
    
    for item in to_remove:
        df = df[df['user'] != item]
    x = df['user'].value_counts().head()
    new_df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index()
    new_df.columns = ['Name', 'Percent']
    
    new_df.index = new_df.index + 1
    return x, new_df

def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]
    temp = df[df['user']!= 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']


    wc = WordCloud(width=500, height=500, min_font_size=10,background_color='white')
    df_wc= wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()
    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]
    temp = df[df['user']!= 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words=[]
    for message in temp['message']:
         for word in message.lower().split():
              if word not in stop_words:
                   words.append(word)
    
    mostcommon_df = pd.DataFrame(Counter(words).most_common(20))
    
    mostcommon_df.index = mostcommon_df.index + 1
    return mostcommon_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]
    
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap