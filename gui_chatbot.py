import tkinter as tk
import speech_recognition as sr
from school_bot import get_school_response

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_log.config(state="normal")
    chat_log.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

    response = get_school_response(user_input)
    chat_log.insert(tk.END, f"SchoolBot: {response}\n\n")
    chat_log.config(state="disabled")
    chat_log.see(tk.END)

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat_log.config(state="normal")
        chat_log.insert(tk.END, "🎤 Listening...\n")
        chat_log.config(state="disabled")
        root.update()

        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, user_input)
            send_message()
        except sr.UnknownValueError:
            chat_log.config(state="normal")
            chat_log.insert(tk.END, "⚠️ Sorry, I didn't understand that.\n\n")
            chat_log.config(state="disabled")
        except sr.RequestError:
            chat_log.config(state="normal")
            chat_log.insert(tk.END, "⚠️ Could not reach the speech service.\n\n")
            chat_log.config(state="disabled")
        except sr.WaitTimeoutError:
            chat_log.config(state="normal")
            chat_log.insert(tk.END, "⚠️ Listening timed out.\n\n")
            chat_log.config(state="disabled")

# Main window setup
root = tk.Tk()
root.title("SchoolBot")
root.geometry("650x500")

# Chat display
chat_log = tk.Text(root, bg="white", fg="black", font=("Arial", 12), state="disabled")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_log.config(state="normal")
chat_log.insert(tk.END, "SchoolBot: Hello! How can I assist you today?\n\n")
chat_log.config(state="disabled")

# Input frame with entry and buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", send_message)

send_btn = tk.Button(frame, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, padx=(10, 5))

voice_btn = tk.Button(frame, text="🎤 Voice", command=voice_input)
voice_btn.pack(side=tk.LEFT)

entry.focus()
root.mainloop()
