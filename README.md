# 📱 WhatsApp Chat Analyzer  

🛠 **WhatsApp Chat Analyzer** is a powerful web-based tool that helps you explore and visualize WhatsApp conversations.  
It parses raw `.txt` chat exports, cleans the data, and generates **insights, statistics, and visualizations** such as timelines, busiest users, word clouds, emoji analysis, and heatmaps.  

The app is deployed with **Streamlit**, enabling real-time interactive exploration of chat datasets.  

---

## 🔍 Problem Statement  

Analyzing WhatsApp conversations can provide valuable insights into communication patterns, activity trends, and group dynamics. However, challenges exist:  

- **Raw Data Format** – WhatsApp exports chats as unstructured `.txt` files  
- **Preprocessing** – Regex parsing, cleaning, and structuring data  
- **Scalability** – Handling large group chats with thousands of messages  
- **Feature Extraction** – Deriving meaningful statistics (users, words, emojis, links)  
- **Visualization** – Converting raw numbers into intuitive charts & graphics  

---

## 🚀 Proposed Work  

This project addresses the above challenges through a streamlined **chat analysis pipeline**.  

### ✅ Project Workflow  
1. **Data Import**: Export WhatsApp chat (`.txt`) without media and upload to the app.  
2. **Preprocessing**: Regex-based parsing → Usernames, timestamps, messages.  
3. **Feature Engineering**: Extract word counts, emoji usage, URLs, media.  
4. **Visualization**: Generate word clouds, activity heatmaps, bar/pie charts.  
5. **Exploration**: Filter insights by overall chat or individual participants.  
6. **Frontend**: Deployed with **Streamlit** for user-friendly interaction.  

---

## 🧠 Features & Analysis  

| Feature | Description |  
|---------|-------------|  
| ✅ Real-Time Analysis | Upload `.txt` file & instantly get insights |  
| 📊 General Statistics | Total messages, words, media, links shared |  
| 📅 Activity Timeline | Daily, monthly, and yearly activity trends |  
| ⏰ Weekly & Hourly Heatmap | Identify busiest days and hours |  
| 👥 Most Active Users | Ranking by message count & contribution |  
| ☁ Word Cloud | Visual representation of frequently used words |  
| 😂 Emoji Analysis | Breakdown of emoji frequency per user |  
| 🔗 Link Sharing | Count of shared URLs |  
| 📉 Message Trends | Line plots and bar charts for activity insights |  
| 🌙 Dark Mode (Planned) | Theme toggle support |  
| 📤 Export (Planned) | Download chat reports as PDF/Excel |  

---

## 📊 Visualizations  

- **Timeline Analysis** – Daily/Monthly activity  
- **Heatmap** – Active hours & days of the week  
- **WordCloud** – Most common words in chat  
- **Emoji Usage** – Frequency distribution  
- **User Contribution** – Pie chart of messages by user  
- **Top Messages/Links** – Insights into shared content  

---

## 🗂 Dataset  

- 📁 **Source**: Exported WhatsApp Chat (`.txt` format)  
- 🔢 **Features Extracted**:  
  - User  
  - Date & Time  
  - Message  
  - Media (e.g., images, videos, audio)  
  - Emojis & Links  

---

## 🔬 Evaluation Metrics  

Since this project is **exploratory** (not predictive), evaluation is based on:  

- **Accuracy of Parsing** – Correctly extracting users, timestamps, messages  
- **Scalability** – Handling large chat histories efficiently  
- **Clarity of Visualizations** – Easy interpretation of insights  
- **User Experience** – Smooth interaction with Streamlit UI  

---

## 💻 How to Run  

### Clone the repository  
- git clone https://github.com/your-username/whatsapp-chat-analyzer.git
- cd whatsapp-chat-analyzer

##Install dependencies
pip install -r requirements.txt

##Run the Streamlit App
streamlit run app.py


Then open http://localhost:8501 in your browser.

##🌐 Deployment

You can deploy this Streamlit app on:

✅ Streamlit Cloud – Free and easy deployment
🔁 HuggingFace Spaces – Streamlit/Gradio hosting
☁ Heroku / AWS / GCP – For production-level hosting

Steps for Streamlit Cloud:

- Push your project to GitHub
- Go to Streamlit Cloud
- Click New App → Select repo → Choose app.py
- Click Deploy

##👩‍💻 Developers & Acknowledgements

👨‍💻 Developed by Kartik Soni
🎓 Student Developer | 💡 Data Science Enthusiast

##🙏 Acknowledgements

-WhatsApp for data exports
-Streamlit for interactive UI
-pandas, matplotlib, seaborn, wordcloud for analysis & visualization
