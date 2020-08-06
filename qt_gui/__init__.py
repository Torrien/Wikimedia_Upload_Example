import PySide2 as ps2
import sys
from PySide2.QtWidgets import QApplication, QMainWindow


class WiCU(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
    
    


if __name__ == "__main__":
    app = QApplication([])
    window = WiCU()
    window.show()
    sys.exit(app.exec_())
