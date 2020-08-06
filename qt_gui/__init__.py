import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog,\
     QLineEdit, QVBoxLayout
from PySide2.QtCore import QUrl, Slot

# class WiCU(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)


# if __name__ == "__main__":
#     app = QApplication([])
#     window = WiCU()
#     window.show()
#     sys.exit(app.exec_())

#My original Dialog Class

class MyFirstForm(QDialog):
    def __init__(self, parent=None):
        super(MyFirstForm, self).__init__(parent)
        self.setWindowTitle("My First Form")
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        # self.edit.focusInEvent(self.start_edit)
        # self.edit.focusOutEvent(self.end_edit)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # layout.addWidget(self.view)
        # Set dialog layout
        self.setLayout(layout)

    # Greets the user
    def greetings(self):
        if self.edit.text() == "Write my name here..":
            print("Write a name.")
        else:
            print("Hello {}".format(self.edit.text()))

    def start_edit(self):
        if self.edit.text() == "Write my name here..":
            self.edit.ORIGINAL_TEXT = self.edit.text()
            self.edit.setText("")

    def end_edit(self):
        pass


# class SmartInput(QLineEdit):
#     def __init__(self, prompt="Enter value.", parent=None):
#         super().__init__(parent=parent)
#         self.PROMPT = prompt
    
#     def focusInEvent(self):
#         if self.text() == self.PROMPT:
#             self.setText("")

#     def focusOutEvent(self):
#         if self.text().strip() == "":
#             self.setText(self.PROMPT)




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MyFirstForm()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
