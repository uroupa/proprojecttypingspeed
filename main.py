from tkinter import *
from tkinter.messagebox import showinfo
import math
import random


random_words = []
time = 1
word_list = ['cook', 'circulate', 'district', 'wreck', 'execute', 'proposal', 'goalkeeper', 'charismatic', 'disagreement', 'dilute', 'football', 'pool', 'pen', 'pupil', 'channel', 'drown', 'stretch', 'repetition', 'ivory', 'abundant', 'pace', 'crowd', 'format', 'cupboard', 'wave', 'praise', 'entertainment', 'affair', 'stadium', 'lawyer', 'squash', 'sustain', 'throat', 'ballet', 'budge', 'courtship', 'color', 'competition', 'organisation', 'city', 'easy', 'ally', 'performer', 'play', 'expect', 'treasurer', 'discipline', 'buy', 'rumor', 'precedent', 'character', 'proper', 'battle', 'restless', 'store', 'tooth', 'impulse', 'viable', 'transport', 'ward', 'south', 'courtship', 'broken', 'overwhelm' 'command', 'countryside', 'compound', 'creep', 'talented', 'claim', 'disclose', 'wall', 'baby', 'minor', 'admiration', 'chew', 'toast', 'feminist', 'feast', 'origin', 'seal', 'state', 'palm', 'obstacle', 'doll', 'headquarters', 'slot', 'compromise', 'excuse', 'heat', 'dash', 'express', 'seek', 'rabbit', 'break', 'impound', 'recognize', 'relative', 'realism', 'storage', 'excavation', 'chief', 'treat', 'practical', 'dive', 'tip', 'asset', 'distort', 'slice', 'prayer', 'doctor', 'budget', 'differ', 'comprehensive', 'stereotype', 'tin', 'assertive', 'cheese', 'pen', 'modernize', 'effort', 'strong', 'painter', 'rally', 'dynamic', ]


# create the root window
root = Tk()
root.title('Typing Speed App')
root.config(padx=50, pady=50)


# ---------------------------- TIMER ------------------------------- #

def start():
    timer_time = time * 12
    get_words()
    t.config(state='normal')
    t.delete("1.0", END)
    count_down(timer_time)

# ---------------------------- FUNCTIONALITY ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = (f"0{count_sec}")
    timer_text.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count-1)
    else:
        timer_text.config(text="00:00")
        t.config(state='disabled')
        get_text()

def get_words():
    global random_words
    word_label.config(state='normal')
    random_words = random.sample(word_list, k=100)
    word_text = ' '.join(random_words)
    word_label.delete("1.0", END)
    word_label.insert("1.0", word_text)
    word_label.config(state='disabled', font=("Roboto", 15, "normal"))

def get_text():
    text = t.get("1.0", 'end-1c')
    typed_list = text.split(' ')
    # print(text)
    print(typed_list)
    # print(random_words)
    calculate_speed(typed_list)

def calculate_speed(list):
    correct_words = []
    for word in list:
        if word.lower() in random_words:
            correct_words.append(word)
    # print(correct_words)
    char_count = ''.join(correct_words)
    # print(list)
    showinfo("Information", f"Time is Up. You typed {len(correct_words)} words correctly in 1 minute. You typed {len(char_count)} characters per minute. Keep going!!")


timer_text = Label(text="00:00", font=('Segoe UI', 20, "bold"))
timer_text.grid(row=0, column=2, pady=10)

start_button = Button(text="Start Typing", command=start, padx=5, pady=5,  border=0, highlightthickness=0)
start_button.grid(row=1, column=2, pady=10)

word_label = Text(root, height = 15, width = 60, wrap = "word")
word_label.grid(row=1, column=1, pady=10, padx=10)
x = 'start to get words'
word_label.delete("1.0", END)
word_label.insert("1.0", x)
word_label.config(state='disabled', font=("Roboto", 15, "normal"))

# Text label
type_label = Label(root, text="Type Here :",font=("Segoe UI", 15), fg="black", bg="#fff")
type_label.grid(column=0, row=3, padx=10, pady=25)

# Text Widget
t = Text(root, width=60, height=15)
t.grid(column=1, row=3)
t.config(font=("Roboto", 15, "normal"))
# print(t.get("1.0", 'end-1c'))



# run the application
root.mainloop()
