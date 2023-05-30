import tkinter as tk
import pyshorteners
import tkinter.messagebox as messagebox
import pyperclip

def shorten_url():
    original_url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url)
    result_label.config(text=shortened_url)
    copy_button.config(state=tk.NORMAL)

def copy_url():
    shortened_url = result_label.cget("text")
    pyperclip.copy(shortened_url)
    messagebox.showinfo("Success", "Shortened URL copied to clipboard!")

root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Enter URL", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=40)
entry.pack(pady=10)

shorten_button = tk.Button(root, text="Shorten", command=shorten_url, font=("Helvetica", 14),
                            bg="#333333", fg="#ffffff")
shorten_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="#333333")
result_label.pack()

copy_button = tk.Button(root, text="Copy", command=copy_url, font=("Helvetica", 14),bg="#fc3503",
                        border=12, fg="#ffffff", state=tk.DISABLED)
copy_button.pack(pady=10)

root.mainloop()
