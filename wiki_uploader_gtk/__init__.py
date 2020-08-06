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

        self.exit_button = Gtk.Button(label="Exit")
        self.exit_button.connect("clicked", self.destroy_wicu)
        # self.box.pack_end(self.exit_button, True, True, 2)

        # self.show()
        # self.connect("destroy", Gtk.main_quit)

        self.grid.attach(self.press_test_button, 0, 0, 3, 1)
        self.grid.attach(self.exit_button, 3, 1, 4, 2)
    
    def destroy_wicu(self, widget):
        self.destroy()
    
    def on_button_clicked(self, widget):
        print("Hello World")
        widget.PRESSED_TIMES += 1
        widget.set_label(f"Clicked {widget.PRESSED_TIMES} times.")
        if widget.PRESSED_TIMES > 5:
            self.destroy()




if __name__ == "__main__":
    WiCU = WikiCommonsUploader(title="Hello World")
    WiCU.connect("destroy", Gtk.main_quit)
    WiCU.show_all()
    Gtk.main()