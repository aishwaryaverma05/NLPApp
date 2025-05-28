# from tkinter import *
# from mydb import Database
# from tkinter import messagebox
#
#
# # from myapi import API
# # from textblob import TextBlob
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# nltk.download('vader_lexicon')
# from transformers import pipeline
#
# class NLPApp:
#     def __init__(self):
#
#         #create database object
#         self.dbo=Database()
#         self.ner_pipeline = pipeline("ner", grouped_entities=True)
#         self.emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
#         # self.apio=API()
#         #login ka gui load krna h
#         # self.root ek variable h jism hum Tk() object ko store kr rahe h
#         self.root=Tk()  #gui banaya h
#         self.root.title("NLPApp")
#         self.root.iconbitmap('resources/favicon.ico')
#         self.root.geometry("600x600") #size kitna hona cahiye jab run kre screen pr
#         self.root.config(bg="#708090") #gui ka background colour
#         self.login_gui()
#         self.root.mainloop() #gui ko screen pr hold rakha
#
#     def login_gui(self):
#
#         self.clear()
#         heading=Label(self.root,text="Natural Language Processing",bg='#708090',fg='black')
#         heading.pack(pady=(30,80))
#         heading.configure(font=("calibri", 35,'bold'))
#
#         label1=Label(self.root,text="Enter emailID",bg='#708090',fg='black')
#         label1.pack(pady=(30,10)) # pack dalna zaruri h vrna show nhi krega
#         label1.configure(font=("calibri", 18))
#
#         #entry box
#         self.emailID=Entry(self.root,width=50)
#         self.emailID.configure(font=("calibri", 14,'bold'))
#         self.emailID.pack(pady=(5),ipady=10) #ipady is to increase height, we cant directly inc. height **in entry box**
#
#
#         label2=Label(self.root,text="Enter password",bg='#708090',fg='black')
#         label2.pack(pady=(10,10)) # pack dalna zaruri h vrna show nhi krega
#         label2.configure(font=("calibri", 18))
#
#
#         self.pw=Entry(self.root,width=50,show='*')
#         self.pw.configure(font=("calibri", 14,'bold'))
#         self.pw.pack(pady=(5),ipady=10) #ipady is to increase height, we cant directly inc. height
#
#         login_btn=Button(self.root, text="Login", width=10, command=self.perform_login)
#         login_btn.configure(font=("calibri", 14))
#         login_btn.pack(pady=(30,10))
#
#         label3 = Label(self.root, text="Not a member?", bg='#708090', fg='black')
#         label3.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         label3.configure(font=("calibri", 18,'italic'))
#
#         redirect_btn = Button(self.root, text="Register Now!", width=15,command=self.register_gui)
#         redirect_btn.configure(font=("calibri", 14))
#         redirect_btn.pack(pady=(30, 10))
#
#     def register_gui(self):
#         self.clear()
#
#         heading = Label(self.root, text="Natural Language Processing", bg='#708090', fg='black')
#         heading.pack(pady=(30, 80))
#         heading.configure(font=("calibri", 35, 'bold'))
#
#         label0 = Label(self.root, text="Enter Name:", bg='#708090', fg='black')
#         label0.pack(pady=(30, 10))  # pack dalna zaruri h vrna show nhi krega
#         label0.configure(font=("calibri", 18))
#
#         self.name = Entry(self.root, width=50)
#         self.name.configure(font=("calibri", 14, 'bold'))
#         self.name.pack(pady=(5), ipady=10)
#
#         label1 = Label(self.root, text="Enter emailID", bg='#708090', fg='black')
#         label1.pack(pady=(30, 10))  # pack dalna zaruri h vrna show nhi krega
#         label1.configure(font=("calibri", 18))
#
#         self.emailID = Entry(self.root, width=50)
#         self.emailID.configure(font=("calibri", 14, 'bold'))
#         self.emailID.pack(pady=(5),ipady=10)  # ipady is to increase height, we cant directly inc. height **in entry box**
#
#         label2 = Label(self.root, text="Create a password", bg='#708090', fg='black')
#         label2.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         label2.configure(font=("calibri", 18))
#
#         self.pw = Entry(self.root, width=50, show='*')
#         self.pw.configure(font=("calibri", 14, 'bold'))
#         self.pw.pack(pady=(5), ipady=10)  # ipady is to increase height, we cant directly inc. height
#
#         register_btn = Button(self.root, text="Register Now", width=10,command=self.perform_registration)
#         register_btn.configure(font=("calibri", 14))
#         register_btn.pack(pady=(30, 10))
#
#         label3 = Label(self.root, text="Already a member", bg='#708090', fg='black')
#         label3.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         label3.configure(font=("calibri", 18, 'italic'))
#
#         redirect_btn = Button(self.root, text="Login Now!", width=15, command=self.login_gui)
#         redirect_btn.configure(font=("calibri", 14))
#         redirect_btn.pack(pady=(30, 10))
#     def clear(self):
#          # clear the existing gui
#         for i in self.root.pack_slaves():
#             i.destroy()
#
#
#     def perform_registration(self):
#         #fetch data from gui
#         get_name=self.name.get()
#         get_mail = self.emailID.get()
#         get_pw = self.pw.get()
#
#         response=self.dbo.add_data(get_name, get_mail, get_pw)
#         if response:
#             messagebox.showinfo('Success', 'Successfully registered! You can now login')
#         else:
#             messagebox.showinfo('error', 'Email exists')
#
#
#     def perform_login(self):
#         # Fetch email and password from GUI
#         get_mail = self.emailID.get()
#         get_pw = self.pw.get()
#
#
#         response = self.dbo.search_user(get_mail, get_pw)
#         if response:
#             messagebox.showinfo('Success', 'Login Successful!')
#             self.home_gui()
#         else:
#             messagebox.showerror('Error', 'Incorrect Email/password.')
#
#
#     def home_gui(self):
#         self.clear()
#
#         heading = Label(self.root, text="Natural Language Processing", bg='#708090', fg='black')
#         heading.pack(pady=(30, 80))
#         heading.configure(font=("calibri", 35, 'bold'))
#
#         sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=4,command=self.sentiment_analysis)
#         sentiment_btn.configure(font=("calibri", 14))
#         sentiment_btn.pack(pady=(30, 10))
#
#         ner_btn = Button(self.root, text="Named Entity Recognisation", width=30, height=4,command=self.ner_gui)
#         ner_btn.configure(font=("calibri", 14))
#         ner_btn.pack(pady=(30, 10))
#
#
#         emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=4,command=self.emotion_gui)
#         emotion_btn.configure(font=("calibri", 14))
#         emotion_btn.pack(pady=(30, 10))
#
#         logout_btn = Button(self.root, text="Logout", width=15, command=self.login_gui)
#         logout_btn.configure(font=("calibri", 14))
#         logout_btn.pack(pady=(30, 10))
#
#     def sentiment_analysis(self):
#         self.clear()
#
#         heading1= Label(self.root, text="Natural Language Processing", bg='#708090', fg='black')
#         heading1.pack(pady=(30, 80))
#         heading1.configure(font=("calibri", 35, 'bold'))
#
#         heading2 = Label(self.root, text="Sentimental Analysis", bg='#708090', fg='black')
#         heading2.pack(pady=(10, 20))
#         heading2.configure(font=("calibri", 25, 'bold'))
#
#         label1 = Label(self.root, text="Enter the Text", bg='#708090', fg='black')
#         label1.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         label1.configure(font=("calibri", 18))
#
#         self.sentiment_input = Entry(self.root, width=50)
#         self.sentiment_input.configure(font=("calibri", 14, 'bold'))
#         self.sentiment_input.pack(pady=(5), ipady=10)
#
#         sentiment_btn = Button(self.root, text="Analyse Sentiment", width=15, command=self.do_sentiment_analysis)
#         sentiment_btn.configure(font=("calibri", 14))
#         sentiment_btn.pack(pady=(30, 10))
#
#         self.sentiment_result = Label(self.root, text="", bg='#708090', fg='black')
#         self.sentiment_result.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         self.sentiment_result.configure(font=("calibri", 18))
#
#         goback_btn = Button(self.root, text="Back", width=15, command=self.home_gui)
#         goback_btn.configure(font=("calibri", 14))
#         goback_btn.pack(pady=(30, 10))
#
#         #text display ke liye label ka use krna padhta haiiii
#
#     def do_sentiment_analysis(self):
#         text = self.sentiment_input.get()
#         sid = SentimentIntensityAnalyzer()
#         scores = sid.polarity_scores(text)
#         # Extract scores
#         pos = scores['pos']
#         neu = scores['neu']
#         neg = scores['neg']
#         compound = scores['compound']
#         if compound >= 0.05:
#             overall = "Positive 😊"
#         elif compound <= -0.05:
#             overall = "Negative 😠"
#         else:
#             overall = "Neutral 😐"
#         result = (
#             f"Overall Sentiment: {overall}\n\n"
#             f"Detailed Scores:\n"
#             f"Positive: {pos:.2f}\n"
#             f"Neutral: {neu:.2f}\n"
#             f"Negative: {neg:.2f}\n"
#             f"Compound: {compound:.2f}"
#         )
#         self.sentiment_result.config(text=result)
#
#
#     def ner_gui(self):
#         self.clear()
#
#         heading1 = Label(self.root, text="Natural Language Processing", bg='#708090', fg='black')
#         heading1.pack(pady=(30, 80))
#         heading1.configure(font=("calibri", 35, 'bold'))
#
#         heading2 = Label(self.root, text="Named Entity Recognition(NER)", bg='#708090', fg='black')
#         heading2.pack(pady=(10, 20))
#         heading2.configure(font=("calibri", 25, 'bold'))
#
#         label1 = Label(self.root, text="Enter the Text", bg='#708090', fg='black')
#         label1.pack(pady=(10, 10))  # pack dalna zaruri h vrna show nhi krega
#         label1.configure(font=("calibri", 18))
#
#         self.ner_input = Entry(self.root, width=50)
#         self.ner_input.configure(font=("calibri", 14, 'bold'))
#         self.ner_input.pack(pady=(5), ipady=10)
#
#         ner_btn = Button(self.root, text="Perform NER", width=15, command=self.do_ner)
#         ner_btn.configure(font=("calibri", 14))
#         ner_btn.pack(pady=(30, 10))
#
#         self.ner_result = Label(self.root, text="", bg='#708090', fg='black', wraplength=550, justify="left")
#         self.ner_result.pack(pady=(10, 10))
#         self.ner_result.configure(font=("calibri", 14))
#
#         goback_btn = Button(self.root, text="Back", width=15, command=self.home_gui)
#         goback_btn.configure(font=("calibri", 14))
#         goback_btn.pack(pady=(30, 10))
#
#     def do_ner(self):
#         text = self.ner_input.get()
#         results = self.ner_pipeline(text)
#
#         if not results:
#             self.ner_result.config(text="No named entities found.")
#             return
#
#         result_str = "Named Entities:\n\n"
#         for entity in results:
#             word = entity['word'].replace("##", "")  # BERT sometimes adds '##' in subwords
#             label = entity['entity_group']
#             score = entity['score']
#             result_str += f"• {word} → {label} ({score:.2f})\n"
#
#         self.ner_result.config(text=result_str)
#
#
#     def emotion_gui(self):
#         self.clear()
#
#         heading1 = Label(self.root, text="Natural Language Processing", bg='#708090', fg='black')
#         heading1.pack(pady=(30, 80))
#         heading1.configure(font=("calibri", 35, 'bold'))
#
#         heading2 = Label(self.root, text="Emotion Prediction", bg='#708090', fg='black')
#         heading2.pack(pady=(10, 20))
#         heading2.configure(font=("calibri", 25, 'bold'))
#
#         label1 = Label(self.root, text="Enter the Text", bg='#708090', fg='black')
#         label1.pack(pady=(10, 10))
#         label1.configure(font=("calibri", 18))
#
#         self.emotion_input = tk.Text(self.root, height=4, width=50)
#         self.emotion_input.configure(font=("calibri", 14, 'bold'))
#         self.emotion_input.pack(pady=(5), ipady=10)
#
#         emotion_btn = Button(self.root, text="Detect Emotion", width=15, command=self.do_emotion_prediction)
#         emotion_btn.configure(font=("calibri", 14))
#         emotion_btn.pack(pady=(30, 10))
#
#         self.emotion_result = Label(self.root, text="", bg='#708090', fg='black', wraplength=550, justify="left")
#         self.emotion_result.pack(pady=(10, 10))
#         self.emotion_result.configure(font=("calibri", 14))
#
#         goback_btn = Button(self.root, text="Back", width=15, command=self.home_gui)
#         goback_btn.configure(font=("calibri", 14))
#         goback_btn.pack(pady=(30, 10))
#
#
#
#     def do_emotion_prediction(self):
#         text = self.emotion_input.get()
#         results = sorted(self.emotion_pipeline(text), key=lambda x: x['score'], reverse=True)
#
#         if not results:
#             self.emotion_result.config(text="No emotion detected.")
#             return
#
#         result_str = "Detected Emotions:\n\n"
#         for res in results:
#             result_str += f"{res['label']} ({res['score']:.2f})\n"
#
#         self.emotion_result.config(text=result_str)
#
#
# nlp=NLPApp()


import tkinter as tk
from tkinter import messagebox
from mydb import Database

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from transformers import pipeline

class NLPApp:
    def __init__(self):
        self.dbo = Database()

        # Load models
        self.ner_pipeline = pipeline("ner", grouped_entities=True)
        self.emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

        self.root = tk.Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry("600x600")
        self.root.config(bg="#708090")

        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear()
        heading = tk.Label(self.root, text="Natural Language Processing", bg='#708090', fg='black', font=("calibri", 35, 'bold'))
        heading.pack(pady=(30, 80))

        tk.Label(self.root, text="Enter emailID", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.emailID = tk.Entry(self.root, width=50, font=("calibri", 14, 'bold'))
        self.emailID.pack(pady=(5), ipady=10)

        tk.Label(self.root, text="Enter password", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.pw = tk.Entry(self.root, width=50, show='*', font=("calibri", 14, 'bold'))
        self.pw.pack(pady=(5), ipady=10)

        tk.Button(self.root, text="Login", width=10, font=("calibri", 14), command=self.perform_login).pack(pady=(30, 10))

        tk.Label(self.root, text="Not a member?", bg='#708090', fg='black', font=("calibri", 18, 'italic')).pack(pady=(10, 10))
        tk.Button(self.root, text="Register Now!", width=15, font=("calibri", 14), command=self.register_gui).pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        tk.Label(self.root, text="Natural Language Processing", bg='#708090', fg='black', font=("calibri", 35, 'bold')).pack(pady=(30, 80))

        tk.Label(self.root, text="Enter Name:", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.name = tk.Entry(self.root, width=50, font=("calibri", 14, 'bold'))
        self.name.pack(pady=(5), ipady=10)

        tk.Label(self.root, text="Enter emailID", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.emailID = tk.Entry(self.root, width=50, font=("calibri", 14, 'bold'))
        self.emailID.pack(pady=(5), ipady=10)

        tk.Label(self.root, text="Create a password", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.pw = tk.Entry(self.root, width=50, show='*', font=("calibri", 14, 'bold'))
        self.pw.pack(pady=(5), ipady=10)

        tk.Button(self.root, text="Register Now", width=10, font=("calibri", 14), command=self.perform_registration).pack(pady=(30, 10))
        tk.Label(self.root, text="Already a member", bg='#708090', fg='black', font=("calibri", 18, 'italic')).pack(pady=(10, 10))
        tk.Button(self.root, text="Login Now!", width=15, font=("calibri", 14), command=self.login_gui).pack(pady=(10, 10))

    def perform_registration(self):
        get_name = self.name.get()
        get_mail = self.emailID.get()
        get_pw = self.pw.get()

        response = self.dbo.add_data(get_name, get_mail, get_pw)
        if response:
            messagebox.showinfo('Success', 'Successfully registered! You can now login')
        else:
            messagebox.showinfo('Error', 'Email already exists')

    def perform_login(self):
        get_mail = self.emailID.get()
        get_pw = self.pw.get()

        response = self.dbo.search_user(get_mail, get_pw)
        if response:
            messagebox.showinfo('Success', 'Login Successful!')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect Email/password.')

    def home_gui(self):
        self.clear()
        tk.Label(self.root, text="Natural Language Processing", bg='#708090', fg='black', font=("calibri", 35, 'bold')).pack(pady=(30, 80))

        tk.Button(self.root, text="Sentiment Analysis", width=30, height=4, font=("calibri", 14), command=self.sentiment_analysis).pack(pady=(10))
        tk.Button(self.root, text="Named Entity Recognition", width=30, height=4, font=("calibri", 14), command=self.ner_gui).pack(pady=(10))
        tk.Button(self.root, text="Emotion Prediction", width=30, height=4, font=("calibri", 14), command=self.emotion_gui).pack(pady=(10))
        tk.Button(self.root, text="Logout", width=15, font=("calibri", 14), command=self.login_gui).pack(pady=(30, 10))

    def sentiment_analysis(self):
        self.clear()
        tk.Label(self.root, text="Sentimental Analysis", bg='#708090', fg='black', font=("calibri", 25, 'bold')).pack(pady=(30, 20))

        tk.Label(self.root, text="Enter the Text", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))
        self.sentiment_input = tk.Entry(self.root, width=50, font=("calibri", 14, 'bold'))
        self.sentiment_input.pack(pady=(5), ipady=10)

        tk.Button(self.root, text="Analyse Sentiment", width=15, font=("calibri", 14), command=self.do_sentiment_analysis).pack(pady=(30, 10))

        self.sentiment_result = tk.Label(self.root, text="", bg='#708090', fg='black', font=("calibri", 18))
        self.sentiment_result.pack(pady=(10, 10))

        tk.Button(self.root, text="Back", width=15, font=("calibri", 14), command=self.home_gui).pack(pady=(30, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            overall = "Positive 😊"
        elif compound <= -0.05:
            overall = "Negative 😠"
        else:
            overall = "Neutral 😐"

        result = (
            f"Overall Sentiment: {overall}\n\n"
            f"Detailed Scores:\n"
            f"Positive: {scores['pos']:.2f}\n"
            f"Neutral: {scores['neu']:.2f}\n"
            f"Negative: {scores['neg']:.2f}\n"
            f"Compound: {compound:.2f}"
        )
        self.sentiment_result.config(text=result)

    def ner_gui(self):
        self.clear()
        tk.Label(self.root, text="Named Entity Recognition", bg='#708090', fg='black', font=("calibri", 25, 'bold')).pack(pady=(30, 20))
        tk.Label(self.root, text="Enter the Text", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))

        self.ner_input = tk.Entry(self.root, width=50, font=("calibri", 14, 'bold'))
        self.ner_input.pack(pady=(5), ipady=10)

        tk.Button(self.root, text="Perform NER", width=15, font=("calibri", 14), command=self.do_ner).pack(pady=(30, 10))

        self.ner_result = tk.Label(self.root, text="", bg='#708090', fg='black', wraplength=550, justify="left", font=("calibri", 14))
        self.ner_result.pack(pady=(10, 10))

        tk.Button(self.root, text="Back", width=15, font=("calibri", 14), command=self.home_gui).pack(pady=(30, 10))

    def do_ner(self):
        text = self.ner_input.get()
        results = self.ner_pipeline(text)
        if not results:
            self.ner_result.config(text="No named entities found.")
            return

        result_str = "Named Entities:\n\n"
        for entity in results:
            word = entity['word'].replace("##", "")
            result_str += f"• {word} → {entity['entity_group']} ({entity['score']:.2f})\n"

        self.ner_result.config(text=result_str)

    def emotion_gui(self):
        self.clear()
        tk.Label(self.root, text="Emotion Prediction", bg='#708090', fg='black', font=("calibri", 25, 'bold')).pack(pady=(30, 20))
        tk.Label(self.root, text="Enter the Text", bg='#708090', fg='black', font=("calibri", 18)).pack(pady=(10, 10))

        self.emotion_input = tk.Text(self.root, height=4, width=50, font=("calibri", 14, 'bold'))
        self.emotion_input.pack(pady=(5), ipady=10)

        tk.Button(self.root, text="Detect Emotion", width=15, font=("calibri", 14), command=self.do_emotion_prediction).pack(pady=(30, 10))

        self.emotion_result = tk.Label(self.root, text="", bg='#708090', fg='black', wraplength=550, justify="left", font=("calibri", 14))
        self.emotion_result.pack(pady=(10, 10))

        tk.Button(self.root, text="Back", width=15, font=("calibri", 14), command=self.home_gui).pack(pady=(30, 10))

    def do_emotion_prediction(self):
        text = self.emotion_input.get("1.0", "end").strip()
        results = sorted(self.emotion_pipeline(text), key=lambda x: x['score'], reverse=True)
        if not results:
            self.emotion_result.config(text="No emotion detected.")
            return

        result_str = "Detected Emotions:\n\n"
        for res in results:
            result_str += f"{res['label']} ({res['score']:.2f})\n"

        self.emotion_result.config(text=result_str)


if __name__ == "__main__":
    nlp = NLPApp()
