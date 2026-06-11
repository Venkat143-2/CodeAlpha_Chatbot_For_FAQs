import tkinter as tk
from tkinter import scrolledtext
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
faq_data = {

    "What is Python?":
        "Python is a high-level programming language.",

    "Who created Python?":
        "Python was created by Guido van Rossum.",

    "What is AI?":
        "AI stands for Artificial Intelligence.",

    "What is Machine Learning?":
        "Machine Learning enables computers to learn from data.",

    "What is Deep Learning?":
        "Deep Learning is a subset of Machine Learning.",

    "What is Data Science?":
        "Data Science is the process of extracting insights from data.",

    "What is NLP?":
        "NLP stands for Natural Language Processing.",

    "What is a chatbot?":
        "A chatbot is software that simulates human conversation.",

    "What is Tkinter?":
        "Tkinter is Python's standard GUI library.",

    "What is an API?":
        "API stands for Application Programming Interface.",

    "What is HTML?":
        "HTML is used to structure web pages.",

    "What is CSS?":
        "CSS is used for styling web pages.",

    "What is JavaScript?":
        "JavaScript adds interactivity to web pages.",

    "What is a variable?":
        "A variable stores data values.",

    "What is a function?":
        "A function is a reusable block of code.",

    "What is OOP?":
        "OOP stands for Object-Oriented Programming.",

    "What is inheritance?":
        "Inheritance allows one class to acquire properties of another class.",

    "What is polymorphism?":
        "Polymorphism allows methods to behave differently based on context.",

    "What is encapsulation?":
        "Encapsulation protects data by wrapping it with methods.",

    "What is abstraction?":
        "Abstraction hides implementation details and shows only functionality.",

    "What is SQL?":
        "SQL is used to manage relational databases.",

    "What is MySQL?":
        "MySQL is a relational database management system.",

    "What is Git?":
        "Git is a version control system.",

    "What is GitHub?":
        "GitHub is a platform for hosting Git repositories.",

    "What is DSA?":
        "DSA stands for Data Structures and Algorithms.",

    "What is an array?":
        "An array stores multiple elements of the same type.",

    "What is a linked list?":
        "A linked list is a linear data structure consisting of nodes.",

    "What is a stack?":
        "A stack follows the LIFO principle.",

    "What is a queue?":
        "A queue follows the FIFO principle.",

    "What is a tree?":
        "A tree is a hierarchical data structure.",

    "What is a graph?":
        "A graph consists of vertices and edges.",

    "What is hashing?":
        "Hashing maps data into fixed-size values.",

    "What is recursion?":
        "Recursion is when a function calls itself.",

    "What is cloud computing?":
        "Cloud computing provides computing services over the internet.",

    "What is cybersecurity?":
        "Cybersecurity protects systems and data from attacks.",

    "What is Linux?":
        "Linux is an open-source operating system.",

    "What is Java?":
        "Java is an object-oriented programming language.",

    "What is C++?":
        "C++ is a powerful programming language supporting OOP.",

    "What is a database?":
        "A database is an organized collection of data.",

    "What is software engineering?":
        "Software engineering is the systematic development of software.",

    "What is debugging?":
        "Debugging is the process of finding and fixing errors.",

    "What is testing?":
        "Testing verifies that software works correctly.",

    "What is frontend development?":
        "Frontend development focuses on the user interface.",

    "What is backend development?":
        "Backend development handles server-side logic.",

    "What is full stack development?":
        "Full stack development includes frontend and backend development.",

    "What is an internship?":
        "An internship provides practical work experience.",

    "What is competitive programming?":
        "Competitive programming focuses on solving coding problems efficiently."
}
def preprocess(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text
questions = list(faq_data.keys())
processed_questions = [
    preprocess(question)
    for question in questions
]
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(
    processed_questions
)
def get_response(user_question):
    processed_input = preprocess(user_question)
    user_vector = vectorizer.transform(
        [processed_input]
    )
    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )
    best_match_index = similarity_scores.argmax()
    score = similarity_scores[0][best_match_index]
    if score > 0.25:
        return faq_data[
            questions[best_match_index]
        ]
    else:
        return (
            "Sorry, I couldn't find a matching answer."
        )
def send_message():
    user_message = user_input.get().strip()
    if not user_message:
        return
    chat_area.insert(
        tk.END,
        "You: " + user_message + "\n"
    )
    response = get_response(user_message)
    chat_area.insert(
        tk.END,
        "Bot: " + response + "\n\n"
    )
    chat_area.see(tk.END)
    user_input.delete(0, tk.END)
def clear_chat():
    chat_area.delete("1.0", tk.END)
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("900x650")
root.state("zoomed")
title = tk.Label(
    root,
    text="🤖 FAQ Chatbot using NLP",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)
chat_area = scrolledtext.ScrolledText(
    root,
    width=100,
    height=25,
    font=("Arial", 11)
)
chat_area.pack(pady=10)
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
user_input = tk.Entry(
    input_frame,
    width=70,
    font=("Arial", 12)
)
user_input.grid(
    row=0,
    column=0,
    padx=10
)
user_input.bind(
    "<Return>",
    lambda event: send_message()
)
send_button = tk.Button(
    input_frame,
    text="Send",
    width=15,
    command=send_message
)
send_button.grid(
    row=0,
    column=1,
    padx=10
)
clear_button = tk.Button(
    input_frame,
    text="Clear Chat",
    width=15,
    command=clear_chat
)
clear_button.grid(
    row=0,
    column=2,
    padx=10
)
footer = tk.Label(
    root,
    text="Uses TF-IDF Vectorization + Cosine Similarity",
    font=("Arial", 10)
)
footer.pack(pady=10)
root.mainloop()
