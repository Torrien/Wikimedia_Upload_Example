#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class WikiCommonsUploader(Gtk.Window):
    def __init__(self, title="Wiki Commons Uploader"):
        super().__init__(title=title)

        # self.box = Gtk.Box(spacing=10)
        # self.add(self.box)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.press_test_button = Gtk.Button(label="Click Here")
        self.press_test_button.connect("clicked", self.on_button_clicked)
        self.press_test_button.PRESSED_TIMES= 0
        # self.box.pack_start(self.press_test_button, True, True, 2)

        self.status_textview: Gtk.TextView = Gtk.TextView.new()
        # self.status_textview.

        self.exit_button = Gtk.Button(label="Exit")
        self.exit_button.connect("clicked", self.destroy_wicu)
        # self.box.pack_end(self.exit_button, True, True, 2)

        # self.show()
        # self.connect("destroy", Gtk.main_quit)

        self.grid.attach(self.press_test_button, 1, 0, 1, 1)
        self.grid.attach(self.status_textview, 0, 1, 3, 1)
        self.grid.attach(self.exit_button, 1, 6, 1, 1)
    
    def destroy_wicu(self, widget):
        self.destroy()
    
    def on_button_clicked(self, widget):
        print("Hello World")
        widget.PRESSED_TIMES += 1
        widget.set_label(f"Clicked {widget.PRESSED_TIMES} times.")
        if widget.PRESSED_TIMES > 5:
            self.destroy()


def hello_world():
    WiCU = WikiCommonsUploader(title="Hello World")
    WiCU.connect("destroy", Gtk.main_quit)
    WiCU.show_all()
    Gtk.main()


if __name__ == "__main__":
    hello_world()

