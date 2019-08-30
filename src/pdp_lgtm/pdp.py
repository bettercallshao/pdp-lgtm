# -*- coding: utf-8 -*-
"""Tkinter UI class implementation."""

import os
import sys
from tkinter import END, FLAT, LEFT, Tk, Entry, Frame, Label, Button, ttk

from .config import get_config
from .history import get_history, put_history

config = get_config()


def base_root():
    root = Tk()
    root.title('https://github.com/timlyrics/pdp-lgtm')
    root.option_add('*font', 'courier 12')
    root.geometry(
        '{w}x{h}+{x}+{y}'.format(
            w=config['options']['width'],
            h=config['options']['height'],
            x=9999,
            y=9999))
    root.wm_attributes('-topmost', 'true')
    root.lift()
    return root


def l2_from_text(text):
    l_text = []
    for line in text.split('\n'):
        l_line = tuple(word for word in line.strip().split(' ') if word)
        if l_line and l_line not in l_text:
            l_text.insert(0, l_line)
    return l_text


def make_section(name, words):
    return {'name': name, 'words': words}


class Pdp(object):
    def __init__(self, root):
        self.root = root

        sections = [make_section('history', get_history())]

        if not sys.stdin.isatty():
            sections.append(
                make_section('stdin', l2_from_text(sys.stdin.read())))

        if len(sys.argv) > 1:
            sections.append(make_section('arg', [sys.argv[1:]]))

        sections += config['sections']

        self.nb = ttk.Notebook(self.root)
        self.nb.pack(expand=1, fill='both')
        self.cur_tab = 0

        for section in sections:
            tab = Frame(self.nb)
            self.nb.add(tab, text=section['name'])

            for l_line in section['words']:
                l_line = l_line or []
                row = Frame(tab)
                row.pack(fill='x')
                head = Button(
                    row, text='<',
                    command=lambda ll=l_line:
                        [self.u_word(w or '') for w in ll])
                head.pack(padx=5, side=LEFT)
                for word in l_line:
                    item = Button(
                        row, text=word,
                        command=lambda w=word: self.u_word(w or ''))
                    item.pack(padx=5, side=LEFT)

        self.output_row = Label(self.root, bg='green')
        self.output_row.pack(fill='x', pady=5)
        self.output_items = []

        self.root.bind('<Return>', self.u_enter)
        self.root.bind('<Escape>', self.u_escape)
        self.root.bind('<Key>', self.u_flip)

    def process_output(self):
        items = [item.get() for item in self.output_items]
        put_history(items)
        command = ' '.join(items)
        print(command)
        return command

    def u_word(self, word):
        item = Entry(self.output_row, relief=FLAT)
        item.insert(0, word)
        item.pack(padx=5, side=LEFT)
        item.bind('<Up>', lambda e: self.u_add(e, 1))
        item.bind('<Down>', lambda e: self.u_add(e, -1))
        item.bind('<BackSpace>', self.u_backspace)
        item.bind('<Tab>', self.u_move)
        item.focus_set()
        self.output_items.append(item)

    def u_enter(self, event):
        command = self.process_output()
        self.root.destroy()
        os.system(command) # noqa

    def u_escape(self, event):
        self.process_output()
        self.root.destroy()

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

    def u_flip(self, event):
        if event.keysym.lower() in ('shift_l', '??'):
            self.cur_tab = (self.cur_tab + 1) % len(self.nb.children)
            self.nb.select(self.cur_tab)

    def u_move(self, event):
        idx = ((self.output_items.index(event.widget) + 1)
               % len(self.output_items))
        self.output_items[idx].focus_set()
        return 'break'


def main():
    root = base_root()
    Pdp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
