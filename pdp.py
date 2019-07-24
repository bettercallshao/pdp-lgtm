#!/usr/bin/env python3
from tkinter import Tk, Label, Button, LEFT, Frame, X
import os
import sys


NROWS = int(os.getenv('NROWS', '30'))


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
            for word in l_line:
                item = Button(row, text=word,
                    command=lambda word=word: self._u_word(word))
                item.pack(padx=5, side=LEFT)

        self.output_row = Frame(self.root)
        self.output_row.pack(fill=X, pady=5)
        self.output_items = []

        self.root.bind('<Return>', self._u_enter)
        self.root.bind('+', self._u_plus)
        self.root.bind('=', self._u_plus)
        self.root.bind('-', self._u_minus)
        self.root.bind('_', self._u_minus)

    def _u_word(self, word):
        item = Button(self.output_row, text=word, bg="green",
            command=lambda: self._u_remove(item))
        item.pack(padx=5, side=LEFT)
        self.output_items.append(item)

    def _u_remove(self, item):
        item.destroy()
        self.output_items.remove(item)

    def _u_enter(self, event):
        print(' '.join([item['text'] for item in self.output_items]))
        self.root.quit()

    def _try_alter_first_item(self, f):
        for item in self.output_items:
            try:
                item['text'] = f(item['text'])
                break
            except:
                pass

    def _u_plus(self, event):
        self._try_alter_first_item(lambda t: str(int(t) + 1))

    def _u_minus(self, event):
        self._try_alter_first_item(lambda t: str(int(t) - 1))


def main():
    root = Tk()
    root.title("pdp")
    root.option_add( "*font", "courier 12" )
    root.geometry(
        '{w}x{h}+{x}+{y}'.format(
            w=int(os.getenv('PDP_WIDTH', '1000')),
            h=35*(NROWS + 1),
            x=9999,
            y=9999))
    root.wm_attributes("-topmost", "true")
    root.lift()

    app = Pdp(root)
    root.mainloop()


if __name__ == '__main__':
    main()

