# Link to start with this one: https://pythonbasics.org/pyqt/


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget)
import openai_secret_manager # this has to be replaced by my personal approach of using the api keys

class ChatGPTGui(QWidget):
    def __init__(self):
        super().__init__()

        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.submit_input)
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_input)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("ChatGPT Input:"))
        layout.addWidget(self.input_field)
        layout.addWidget(QLabel("ChatGPT Output:"))
        layout.addWidget(self.output_field)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("ChatGPT GUI")
        self.secrets = openai_secret_manager.get_secret("openai")
        self.show()

    def submit_input(self):
        input_text = self.input_field.text()
        openai_api_key = self.secrets["api_key"]
        response = openai.Completion.create(engine="text-davinci-002", prompt=(input_text+"\n"), max_tokens=2048, api_key=openai_api_key)
        self.output_field.setPlainText(response["choices"][0]["text"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_gpt_gui = ChatGPTGui()
    sys.exit(app.exec_())
