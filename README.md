# WhatsApp Chat Analyzer

A comprehensive web application built with Streamlit to analyze exported WhatsApp chat data. This tool provides deep insights into messaging patterns, user activity, and temporal trends.

## 🚀 Features

* **Top Statistics**: Instant overview of total messages, words, media shared, and links shared.
* **Timeline Analysis**: Visual trends of chat activity across monthly and daily timelines.
* **Activity Maps**: 
* **Weekly Activity Bar Chart**: Identify the busiest days of the week.
* **Weekly Activity Heatmap**: A detailed grid showing the busiest hours for every day of the week (powered by Seaborn).
* **User Analysis**: Statistical breakdown of the most active participants and their percentage contribution.
* **WordCloud**: Beautiful visual representation of the most frequently used words.
* **Most Common Words**: Data-driven bar chart showing the most used words, filtered using a custom Hinglish stop-words list.

## 🛠️ Technologies Used

* **Python 3.12**
* **Streamlit**: For the interactive web interface.
* **Pandas**: For advanced data manipulation and pivot tables.
* **Matplotlib**: For core data visualizations and plots.
* **Seaborn**: For generating the Weekly Activity Heatmap and styled bar plots.
* **WordCloud**: For generating word clouds.
* **Urlextract**: To identify and count links in messages.
