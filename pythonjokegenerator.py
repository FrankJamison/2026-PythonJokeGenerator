import pyjokes
import tkinter as tk

root = tk.Tk()
root.title("Python Joke Generator")
root.geometry("400x200")


def generate_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)


joke_label = tk.Label(root, text="Click the button to generate a joke!", wraplength=380, justify="center")
joke_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Joke", command=generate_joke)
generate_button.pack(pady=10)

root.mainloop()