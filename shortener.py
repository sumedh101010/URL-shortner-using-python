import tkinter
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.delete(0, tkinter.END)  
    shorturl_entry.insert(tkinter.END, short_url)

root = tkinter.Tk()
root.title("URL Shortener")
font=("Arial", 50, "bold")
root.config(bg="Light blue")

# Calculate center position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 400) // 2  
y = (screen_height - 300) // 2  
root.geometry("400x300+{}+{}".format(x, y))

longurl_label = tkinter.Label(root, text="Enter Long URL")
longurl_label.place(x=50, y=50)

longurl_entry = tkinter.Entry(root)
longurl_entry.place(x=200, y=50)

shorturl_label = tkinter.Label(root, text="Output shortened URL")
shorturl_label.place(x=50, y=100)

shorturl_entry = tkinter.Entry(root, justify='center')
shorturl_entry.place(x=200, y=100)

shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten)
shorten_button.place(x=150, y=150)

root.mainloop()