import sys
from PySide2.QtWidgets import *

app = QApplication([])
label = QLabel('    Hello, Qt for Python ')
label.show()

sys.exit(app.exec_())
