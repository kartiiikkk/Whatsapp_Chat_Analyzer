import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from matplotlib import rcParams
from helper import most_common_words

st.sidebar.title("Whatsapp chat Analyzer📊")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    #fetch unique user
    user_list=df['user'].unique().tolist()

    user_list.remove("group_notification")
    user_list.sort()

    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("Show analysis wrt", user_list)

    # Stats
    if st.sidebar.button("Show Analysis"):

        num_message,words,num_media,num_link = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages️")
            st.title(num_message)
        with col2:
            st.header("Total Words 🔠")
            st.title(words)
        with col3:
            st.header("Media 📽️")
            st.title(num_media)
        with col4:
            st.header("Link 🔗")
            st.title(num_link)

        #monthly timeline
        st.title("Monthly Message Timeline⌛")
        timeline=helper.monthly_timeline(selected_user, df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color='#000C66')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #daily timeline
        st.title("Daily Message Timeline⏳")
        d_timeline=helper.daily_timeline(selected_user, df)
        fig,ax=plt.subplots()
        ax.plot(d_timeline['only_date'], d_timeline['message'],color='#145DA0')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # activity map
        st.title("Activity Map🗺️")
        col1,col2=st.columns(2)
        with col1:
            st.header("Most busy day")
            day = helper.week_activity(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(day['day_name'],day['count'], color='#0C2D48')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy Month")
            month_a = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(month_a['month'], month_a['count'], color='#2E8BC0')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # activity_heatmap
        st.title("Weekly Activity Map🔥")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig,ax = plt.subplots(figsize=(17, 10))
        ax = sns.heatmap(user_heatmap, cmap='GnBu', annot=True, fmt=".1f")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # busiest users in whatsapp

        if selected_user=="Overall":
            st.title("Most Busy User")
            x,new_df=helper.most_busy_user(df)
            fig,ax=plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='#FF8300')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.title("Active Percentage")
                st.dataframe(new_df)

        # WordCloud
        st.title("Wordcloud☁️")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most_common_words
        most_common_df=helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1],color='#90ADC6')
        plt.xticks(rotation='vertical')
        st.title("Most Common Words")
        st.pyplot(fig)

        #Emoji Count

        emoji_counts=helper.emoji_count(selected_user,df)
        st.title("Emoji Count😇")

        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_counts)
        with col2:
            st.title("Top Emojis🔝")
            fig = px.pie(
                emoji_counts.head(10),
                values=1,
                names=0
            )
            st.plotly_chart(fig)