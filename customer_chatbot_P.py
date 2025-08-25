# start the chatbot with GUI, develop a simple GUI using tkinter
# import tkinter as tk
import tkinter as tk
from fuzzywuzzy import process

# --- NLTK for natural language preprocessing ---
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_nltk(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

faq_dict = {
    "what courses are you offering": "We are providing the best training programming language across all programming languages.",
    "i want learn machine learning": "We have a comprehensive course on machine learning that covers everything from basics to advanced topics. Would you like to know more about the course structure?",
    "what about libraries for machine learning": "In the machine learning process, we cover all required libraries.",
    "what is the fee structure for machine learning": "The fee structure is ₹30,000 for the complete course.",
    "where is the institute located": "Our institute is located in Madhapur, Hyderabad.",
    "what kind of projects will we work on": "You will work on predictive modeling, NLP, image recognition, and more.",
    "are you providing certification about this course": "Yes, we provide a certification upon successful completion of the course.",
    "what is the duration of this course": "The duration is 5 months with 2 classes per week.",
    "what is the mode of learning": "The course is conducted online.",
    "should i pay the fee in installments": "Yes, we allow two installments.",
    "fee structure": "javafullstack is 40,000 rupees, data science is 45,000 rupees, html ,css,c++ 20,000 rupees, and SAP is 30,000 rupees.",
    "class timings": "classes are held twice a week, with each classs having 2 hours",
    "what courses are you offering": "We are providing the best training programming language across all programming languages.",
    "i want learn machine learning": "We have a comprehensive course on machine learning that covers everything from basics to advanced topics. Would you like to know more about the course structure?",
    "what about libraries for machine learning": "In the machine learning process, we cover all required libraries.",
    "what is the fee structure for machine learning": "The fee structure is ₹30,000 for the complete course.",
    "where is the institute located": "Our institute is located in Madhapur, Hyderabad.",
    "how can i enroll": "You can enroll by visiting our official website and filling out the registration form.",
    "do you offer online classes": "Yes, we offer online classes through our learning platform.",
    "is there a weekend batch": "Yes, we have weekend batches for working professionals.",
    "what tools will we use": "We use Python, Jupyter Notebook, TensorFlow, Scikit-learn, and cloud platforms like AWS.",
    "do you provide certification": "Yes, a certification is provided upon successful course completion.",
    "who are the trainers": "Our trainers are industry professionals with experience in data science and machine learning.",
    "do you help with placements": "Yes, we offer placement assistance including resume building and mock interviews.",
    "is there any refund policy": "No, we do not have a refund policy.",
    "can i pay the fee in installments": "Yes, the course fee can be paid in two installments.",
    "what is the duration of the course": "The course duration is 5 months with 2 classes per week.",
    "what projects will we do": "You will work on real-time projects including predictive modeling and NLP.",
    "how many hours per week": "Each week includes approximately 4 hours of class time.",
    "is this course suitable for beginners": "Yes, the course is beginner-friendly with step-by-step guidance.",
    "what are the prerequisites": "Basic knowledge of programming and statistics is helpful but not required.",
    "do you provide study material": "Yes, we provide detailed study materials and access to course recordings.",
    "what is the last date for admission": "The last date for admission is the 30th of this month.",
    "can i join without any background in tech": "Yes, the course is designed for students from all backgrounds.",
    "what is the mode of teaching": "The course is taught through live online sessions.",
    "do you offer demo classes": "Yes, we offer free demo classes to help you decide.",
    "can i talk to a counselor": "Yes, you can request a call with our admission counselor.",
    "do you provide job guarantee": "We provide job assistance but not a job guarantee.",
    "what companies are you partnered with": "We are partnered with various tech companies for placements.",
    "what is the schedule for classes": "Classes are scheduled twice a week in the evenings.",
    "what is covered in the python course": "The Python course covers basic syntax, data structures, OOP, and libraries like Pandas and NumPy.",
    "do you teach data visualization": "Yes, data visualization using Matplotlib and Seaborn is included.",
    "is interview preparation included": "Yes, we include mock interviews and interview preparation guidance.",
    "do you provide internships": "Yes, we offer internship opportunities for selected students.",
    "can i access classes on mobile": "Yes, our classes can be accessed via mobile devices.",
    "what is the success rate of placements": "Our placement success rate is over 85%.",
    "do you help build resumes": "Yes, resume building is part of our placement support.",
    "what languages are used in training": "Training is conducted in English.",
    "do you provide lifetime access": "You will have access to course materials for 1 year after completion.",
    "can i switch my batch timing": "Yes, batch changes are allowed with prior notice.",
    "is there support after course ends": "Yes, we offer limited post-course support.",
    "can i contact trainer directly": "Yes, students can contact trainers through the learning platform.",
    "is the certificate downloadable": "Yes, certificates can be downloaded from the student dashboard.",
    "do you provide printed certificates": "No, certificates are only available in digital format.",
    "what is the average salary after course": "Average salary depends on skills and performance, typically 3-6 LPA for freshers.",
    "do you have a referral program": "Yes, we offer referral discounts for new student enrollments.",
    "can i learn at my own pace": "The course has live sessions, but recordings can be accessed anytime.",
    "what happens if i miss a class": "You can watch the recorded session later.",
    "is there any group discount": "Yes, group discounts are available for 3 or more students.",
    "what is your contact number": "You can call us at +91-77414787873 for any queries.",
    "do you offer courses for school students": "Yes, we offer coding courses for school students as well.",
    "what is the difference between basic and advanced courses": "Basic courses focus on foundations, while advanced courses go deeper into practical applications."
}



def chatbot_response(user_input):
    user_input = user_input.lower()

    # --- Chatbot response function ---

    if 'hii' in user_input or 'hello' in user_input:
        return "welcome to VIHA's skill development institute. how can i assist you?"

    best_match = process.extractOne(user_input, faq_dict.keys())
    if best_match[1] > 80:  # If confidence is above 80%
        return faq_dict[best_match[0]]
        return "I'm sorry, I didn't understand that."

    elif 'what courses are you offering'in user_input or "courses offered" in user_input:
        return "we are providing the best training programming language across all programming languages."

    elif 'i want learn machine learning' in user_input or "machine learning course" in user_input:
        return "we have a comprehensive course on machine learning that covers everything from basics to advanced topics. Would you like to know more about the course structure?"

    elif 'what about libraries for machine learning' in user_input or "libraries for machine learning" in user_input:
        return "In the machine learning process, we have to cover what libraries we need to use. Those libraries will be taught in the process of machine learning."

    elif 'what is the fee structure for machine learning' in user_input or "fee structure for machine learning" in user_input:
        return "The fee structure for machine learning is 30,000 rupees. overall things what you need to learn machine learning."

    elif 'what is the duration of this course' in user_input or "duration of machine learning course" in user_input:
        return "The duration of the machine learning course is 5 months, with classes held twice a week. Each class lasts for 2 hours."

    elif 'what is the mode of learning' in user_input or "offline or online mode" in user_input:
        return "The mode of learning for the machine learning course is online, allowing you to attend classes from the comfort of your home."

    elif 'are you providing certification about this course' in user_input or "certificates for courses" in user_input:
        return "yes, we provide a certification upon successful completion of the All courses. This certification can help you in your career advancement."

    elif 'can you tell me about the trainers' in user_input or "who are the trainers" in user_input:
        return "Our trainers are experienced professionals with a strong background in machine learning and data science. They have worked on various projects and are passionate about teaching."

    elif 'should i pay the fee in installments' in user_input or "fee structure" in user_input or "amount" in user_input or "how much fee" in user_input:
        return "javafullstack is 40,000 rupees, data science is 45,000 rupees, html ,css,c++ 20,000 rupees, and SAP is 30,000 rupees.yes, but my institute provides only 2 installments."

    elif 'what is the process of admission' in user_input:
        return "The admission process is totally online. you first register on our website, then you see the admission form."

    elif 'what is the last admission date' in user_input:
        return "the last admission date is 30th of this month for machine learning."

    elif 'is there any refund policy' in user_input:
        return 'no, we do not have a refund policy.'

    elif 'where is the institute located' in user_input:
        return "our institute is located in the madhapur, area silicon valley, hyderabad."

    elif 'what are the prerequisites for this course' in user_input:
        return "The prerequisites for the machine learning course include a basic understanding of programming (preferably in Python), linear algebra, and statistics. Familiarity with data manipulation libraries like Pandas and NumPy is also beneficial."

    elif 'what about projects' in user_input:
        return "yes , we provide projects in the machine learning."

    elif 'what kind of projects will we work on' in user_input or "projects ":
        return "You will work on various projects, including predictive modeling, natural language processing, and image recognition. These projects will help you apply the concepts learned in the course to real-world scenarios."

    elif 'may i know about the placement assistance' in user_input:
        return "yes, we provide placement assistance to our students. We have tie-ups with various companies and help students prepare for interviews."

    elif 'are you providing mock interviews' in user_input:
        return "yes, we conduct mock interviews to help students prepare for real interviews."

    elif 'what is the success rate of placements' in user_input:
        return "Our placement success rate is around 85%. We have a dedicated placement cell that works tirelessly to connect students with potential employers."

    elif 'can you tell me about the course content' in user_input:
        return "The course content includes topics such as supervised and unsupervised learning, regression analysis, classification algorithms, clustering techniques, neural networks, and deep learning. We also cover practical applications and case studies."

    elif 'what tools and technologies will we use' in user_input:
        return "You will use tools and technologies such as Python, Jupyter Notebook, TensorFlow, Keras, Scikit-learn, and various data visualization libraries. We also introduce you to cloud platforms like AWS and Google Cloud for deploying machine learning models."

    elif 'you said this course take 5 months' in user_input or "course duration" in user_input:
        return "yes, the course is designed to be completed in 5 months."

    elif 'you said this course is 5 months, but how much time it will take python.' in user_input:
        return "The Python programming part of the course will take approximately 1 month. This includes learning the basics of Python, data manipulation, and libraries commonly used in machine learning."

    elif 'but i came different background' in user_input:
        return " no problem! We understand that students come from diverse backgrounds. Our course is designed to accommodate beginners as well as those with some programming experience. We will provide you with the necessary resources and support to help you succeed."

    elif 'what kind of companies do you have tie_ups with' in user_input:
        return 'we have tie-ups with various companies in the tech industry.'

    elif 'can you tell me about the course schedule' in user_input:
        return "The course schedule is flexible, with classes held twice a week in the evenings. We also offer weekend batches for working professionals."
    
    elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
        return "Thank you for chatting with us! If you have any more questions in the future, feel free to reach out. Goodbye!"
    
    else:
        return "I'm not sure I understood. Can you please rephrase or ask something else?"


# --- Send function: total function to send the message to the chatbot and display the response in the chat log. It works between the user and chatbot.---
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)  
    chat_log.insert(tk.END, "User: " + user_input + "\n")  
    response = chatbot_response(user_input)
    chat_log.insert(tk.END, "You: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    entry_box.delete(0, tk.END)

def clear_chat():
    """Clear the chat log and input field."""
    chat_log.config(state=tk.NORMAL)
    chat_log.delete(1.0, tk.END)
    entry_box.delete(0, tk.END)
    chat_log.config(state=tk.DISABLED)

# --- Window setup is to create and maintain the GUI with width and length and height --- 
window = tk.Tk()
window.title("VIHA's Skill Development Institute ")
window.geometry("400x500")

# --- Chat display area to shown what the user is typing and what the bot is responsding and chatbot display in the display area.---
chat_log = tk.Text(window, bd=1, bg="lightyellow", font=("Times New Roman", 10), wrap=tk.WORD)
chat_log.config(state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# --- Bottom frame for input and button ---
bottom_frame = tk.Frame(window)
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

# --- Entry box ---
entry_box = tk.Entry(bottom_frame, bd=1, font=("Times New Roman", 10))
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# --- Send button it works to send the message to the chatbot ---
send_button = tk.Button(bottom_frame, text="Send", font=("Times New Roman", 10), command=send_message)
send_button.pack(side=tk.RIGHT)

# --- clear function to clear the chat log ---
clear_button = tk.Button(bottom_frame, text="Clear", font=("Times New Roman", 10), command=clear_chat)
clear_button.pack(side=tk.RIGHT, padx=(5, 0))
clear_button.pack(side=tk.RIGHT, padx=(5, 0))

# --- Run the app ---
window.mainloop()


