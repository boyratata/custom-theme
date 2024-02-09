from PySide2 import QtWidgets, QtGui, QtCore

class CustomTheme:
    themes = {
        "Dark Mode": """
            background-color: #1F1F1F;
            color: white;
        """,
        "Light Mode": """
            background-color: white;
            color: black;
        """
    }

    @staticmethod
    def apply_theme(widget, theme):
        widget.setStyleSheet(theme)

class StyledWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled Widget")
        self.setGeometry(100, 100, 400, 300)
        
        self.label = QtWidgets.QLabel("This is a styled label")
        self.button = QtWidgets.QPushButton("Styled Button")
        self.theme_combobox = QtWidgets.QComboBox()
        self.theme_combobox.addItems(CustomTheme.themes.keys())

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(QtWidgets.QLabel("Select Theme:"))
        layout.addWidget(self.theme_combobox)
        self.setLayout(layout)

        self.theme_combobox.currentTextChanged.connect(self.apply_custom_theme)

    def apply_custom_theme(self):
        selected_theme = self.theme_combobox.currentText()
        theme = CustomTheme.themes.get(selected_theme)
        if theme:
            CustomTheme.apply_theme(self, theme)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = StyledWidget()
    widget.show()
    app.exec_()
