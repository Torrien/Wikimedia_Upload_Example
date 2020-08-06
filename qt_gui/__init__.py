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
        self.edit = SmartInput("Write my name here..", self)
        self.button = QPushButton("Show Greetings")

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # layout.addWidget(self.view)
        # Set dialog layout
        self.setLayout(layout)

    # Greets the user
    def greetings(self):
        if self.edit.text() == self.edit.PROMPT:
            print("Write a name.")
        else:
            print("Hello {}".format(self.edit.text()))

    def end_edit(self):
        pass


class SmartInput(QLineEdit):
    def __init__(self, prompt="Enter value.", parent=None):
        super().__init__(prompt, parent=parent)
        self.PROMPT = prompt

    def focusInEvent(self, event):
        if self.text() == self.PROMPT:
            self.setText("")

    def focusOutEvent(self, event):
        if self.text().strip() == "":
            self.setText(self.PROMPT)




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MyFirstForm()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
