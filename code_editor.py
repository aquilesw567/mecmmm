import tkinter as tk
from tkinter import scrolledtext

class CodeEditor:
    def __init__(self, master):
        self.master = master
        self.master.title('Python Code Editor')

        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        self.setup_syntax_highlighting()
        
    def setup_syntax_highlighting(self):
        # configuring tags for syntax highlighting
        self.text_area.tag_configure('keyword', foreground='blue')
        self.text_area.tag_configure('string', foreground='green')
        self.text_area.tag_configure('comment', foreground='grey')
        self.text_area.tag_configure('number', foreground='purple')

        # example code snippet to be highlighted
        self.text_area.insert(tk.END, """
# Example Python code
if 5 > 3:
    print('Hello, World!')  # This is a comment
""", 'comment')
        
        # additional content can go here

    def highlight_code(self):
        # Fetch the content and apply tags
        content = self.text_area.get(1.0, tk.END)

        # Reset the tags
        self.text_area.tag_remove('keyword', 1.0, tk.END)
        self.text_area.tag_remove('string', 1.0, tk.END)
        self.text_area.tag_remove('comment', 1.0, tk.END)
        self.text_area.tag_remove('number', 1.0, tk.END)

        # Example: Highlighting logic
        keywords = ['def', 'if', 'else', 'elif', 'for', 'while', 'import', 'from']
        for word in keywords:
            start_index = '1.0'
            while True:
                start_index = self.text_area.search(word, start_index, stopindex=tk.END)
                if not start_index:
                    break
                end_index = f'{start_index}+{len(word)}c'
                self.text_area.tag_add('keyword', start_index, end_index)
                start_index = end_index

        # Number highlighting example
        start_index = '1.0'
        while True:
            start_index = self.text_area.search('[0-9]+', start_index, stopindex=tk.END, regexp=True)
            if not start_index:
                break
            end_index = f'{start_index}+1c'
            self.text_area.tag_add('number', start_index, end_index)
            start_index = end_index

if __name__ == '__main__':
    root = tk.Tk()
    editor = CodeEditor(root)
    root.mainloop()