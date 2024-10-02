import tkinter as tk
import random
import time

# Sample sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The only thing we have to fear is fear itself.",
]

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.label = tk.Label(master, text="Type the following sentence:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.sentence = random.choice(sentences)
        self.sentence_label = tk.Label(master, text=self.sentence, font=("Helvetica", 12))
        self.sentence_label.pack(pady=10)

        self.text_box = tk.Text(master, height=5, width=50, font=("Helvetica", 12))
        self.text_box.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.start_time = None

    def start_test(self):
        self.text_box.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()
        self.text_box.focus()

        # Bind the key release event to check input
        self.text_box.bind("<KeyRelease>", self.check_input)

    def check_input(self, event):
        typed_text = self.text_box.get(1.0, tk.END).strip()
        if typed_text == self.sentence:
            elapsed_time = time.time() - self.start_time
            wpm = (len(typed_text.split()) / elapsed_time) * 60
            self.result_label.config(text=f"Congratulations! Your typing speed is {wpm:.2f} WPM.")
            self.text_box.unbind("<KeyRelease>")  # Unbind the event

if __name__ == "__main__":
    root = tk.Tk()
    typing_test = TypingSpeedTest(root)
    root.mainloop()
