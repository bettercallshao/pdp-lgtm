import os
import sys
from tkinter import END, FLAT, LEFT, Button, Entry, Frame, Label, Tk, X

NROWS = int(os.getenv('NROWS', '20'))


def base_root():
    root = Tk()
    root.title('https://github.com/timlyrics/pdp-lgtm')
    root.option_add('*font', 'courier 12')
    root.geometry(
        '{w}x{h}+{x}+{y}'.format(
            w=int(os.getenv('PDP_WIDTH', '1000')),
            h=35*(NROWS + 1),
            x=9999,
            y=9999))
    root.wm_attributes('-topmost', 'true')
    root.lift()
    return root


class Pdp(object):
    def __init__(self, root):
        self.root = root
        text = sys.stdin.read()

        l_text = []
        for line in reversed(text.split('\n')):
            if line.find('history') >= 0:
                continue
            l_line = tuple(word for word in line.strip().split(' ') if word)
            if l_line and l_line not in l_text:
                l_text.insert(0, l_line)
            if len(l_text) >= NROWS:
                break

        for l_line in l_text:
            row = Frame(self.root)
            row.pack(fill=X)
            head = Button(
                row, text='<',
                command=lambda ll=l_line: [self.u_word(w) for w in ll])
            head.pack(padx=5, side=LEFT)
            for word in l_line:
                item = Button(
                    row, text=word,
                    command=lambda w=word: self.u_word(w))
                item.pack(padx=5, side=LEFT)

        Label(self.root).pack()

        self.output_row = Label(self.root, bg='green')
        self.output_row.pack(fill=X, pady=5)
        self.output_items = []

        self.root.bind('<Return>', self.u_enter)
        self.root.bind('<Escape>', self.u_escape)

    def u_word(self, word):
        item = Entry(self.output_row, relief=FLAT)
        item.insert(0, word)
        item.pack(padx=5, side=LEFT)
        item.bind('<Up>', lambda e: self.u_add(e, 1))
        item.bind('<Down>', lambda e: self.u_add(e, -1))
        item.bind('<BackSpace>', self.u_backspace)
        self.output_items.append(item)

    def u_enter(self, event):
        print(' '.join([item.get() for item in self.output_items]))
        self.root.quit()

    def u_escape(self, event):
        self.root.quit()

    def u_backspace(self, event):
        if not event.widget.get():
            event.widget.destroy()
            self.output_items.remove(event.widget)
            return 'break'

    def u_add(self, event, delta):
        try:
            new = str(int(event.widget.get()) + delta)
            event.widget.delete(0, END)
            event.widget.insert(0, new)
        except ValueError:
            pass
        finally:
            return 'break'


def main():
    root = base_root()
    Pdp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
