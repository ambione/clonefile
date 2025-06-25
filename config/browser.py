import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QTextEdit, QPushButton, QLabel, QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from googletrans import Translator

class FullScreenBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navegador em Tela Cheia com Tradutor")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        self.home_url = "https://www.google.com"

        # Navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(self.home_url)
        self.browser.page().settings().setAttribute(
            self.browser.page().settings().ShowScrollBars, False
        )

        # Tradutor (inicialmente oculto)
        self.translator = Translator()
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Digite o texto para traduzir")
        self.translate_button = QPushButton("Traduzir")
        self.translate_button.clicked.connect(self.translate_text)
        self.translation_label = QLabel("Tradução aparecerá aqui")
        self.translation_label.setWordWrap(True)

        self.translation_widget = QWidget()
        translation_layout = QVBoxLayout()
        translation_layout.addWidget(QLabel("Tradutor Google:"))
        translation_layout.addWidget(self.input_text)
        translation_layout.addWidget(self.translate_button)
        translation_layout.addWidget(self.translation_label)
        self.translation_widget.setLayout(translation_layout)
        self.translation_widget.setVisible(False)  # Oculto por padrão

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.browser)
        main_layout.addWidget(self.translation_widget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Q or key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_B:
            if self.browser.history().canGoBack():
                self.browser.back()
        elif key == Qt.Key_F:
            if self.browser.history().canGoForward():
                self.browser.forward()
        elif key == Qt.Key_H:
            self.browser.setUrl(self.home_url)
        elif key == Qt.Key_T:
            # Alternar visibilidade do tradutor
            visible = self.translation_widget.isVisible()
            self.translation_widget.setVisible(not visible)

    def translate_text(self):
        text = self.input_text.toPlainText().strip()
        if text:
            try:
                result = self.translator.translate(text, dest='pt')
                self.translation_label.setText(f"Tradução: {result.text}")
            except Exception as e:
                self.translation_label.setText(f"Erro ao traduzir: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullScreenBrowser()
    window.show()
    sys.exit(app.exec_())
