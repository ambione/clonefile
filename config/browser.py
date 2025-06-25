import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QLabel
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from googletrans import Translator

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navegador com Tradutor")
        self.setGeometry(100, 100, 1000, 700)

        # Widgets principais
        self.browser = QWebEngineView()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.translate_input = QTextEdit()
        self.translate_input.setPlaceholderText("Digite o texto para traduzir...")
        self.translate_button = QPushButton("Traduzir")
        self.translate_button.clicked.connect(self.translate_text)
        self.translation_output = QLabel("Tradução aparecerá aqui.")

        # Layout de navegação
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QLabel("URL:"))
        nav_layout.addWidget(self.url_bar)

        # Layout de tradução
        translate_layout = QVBoxLayout()
        translate_layout.addWidget(QLabel("Tradutor Google:"))
        translate_layout.addWidget(self.translate_input)
        translate_layout.addWidget(self.translate_button)
        translate_layout.addWidget(self.translation_output)

        # Layout principal
        layout = QVBoxLayout()
        layout.addLayout(nav_layout)
        layout.addWidget(self.browser)
        layout.addLayout(translate_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.translator = Translator()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(url)

    def translate_text(self):
        text = self.translate_input.toPlainText()
        if text.strip():
            try:
                translated = self.translator.translate(text, dest='pt')
                self.translation_output.setText(f"Tradução: {translated.text}")
            except Exception as e:
                self.translation_output.setText("Erro ao traduzir: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec_())
