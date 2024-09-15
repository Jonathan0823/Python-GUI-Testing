import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,250,700, 700)
        self.setWindowTitle('IDK what is this')
        self.setWindowIcon(QIcon('sleepyy.png'))

        self.image1 = QPixmap('epic_N.png')
        self.image2 = QPixmap('thumbs.jpg')

        self.line_edit = QLineEdit(self)

        self.button = QPushButton('Submit', self)

        self.label1 = QLabel('Please enter your name: ', self)
        self.label2 = QLabel(self)
        self.label_image1 = QLabel(self)

        
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 70, 300, 50)
        self.line_edit.setStyleSheet('font-size: 30px;'
                                    'font-family: Arial;')
        
        self.button.setGeometry(320, 70, 100, 50)
        self.button.setStyleSheet('font-size: 30px;'
                                    'font-family: Arial;')
        self.button.clicked.connect(self.button_clicked)

        self.label1.setGeometry(10, 10, 400, 50)
        self.label1.setStyleSheet('font-size: 30px;'
                                    'font-family: Arial;')

        self.label2.setGeometry(10, 120, 500, 70)
        self.label2.setStyleSheet('font-size: 30px;'
                                    'font-family: Arial;')
        
        

    def button_clicked(self):
        text = self.line_edit.text()
        text = text.lower()
        if text == 'nigger' or text == 'jovan' or text == 'nigga' or text == "jamal" or text == 'dean':
            self.label_image1.setPixmap(self.image1)
            self.label_image1.setGeometry(10, 200, 300, 300)
            self.label_image1.setScaledContents(True)
            self.label2.setText(f"YOU'RE BLACK👶🏿👦🏿🍉")

            pygame.init()
            sound_file = "getout.mp3"
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

        else:
            self.label2.setText(f"Hello {text.capitalize()}")
            self.label_image1.setPixmap(self.image2)
            self.label_image1.setGeometry(10, 200, 300, 300)
            self.label_image1.setScaledContents(True)

    
def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()