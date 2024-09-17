import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,250,700, 700)
        self.setWindowTitle('IDK what is this')
        self.setWindowIcon(QIcon('assets/image/sleepyy.png'))

        self.image1 = QPixmap('assets/image/epic_N.png')
        self.image2 = QPixmap('assets/image/thumbs.png')
        self.image3 = QPixmap('assets/image/chinese.png')

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
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label_image1)

        
        

    def button_clicked(self):
        pygame.init()
        text = self.line_edit.text()
        text = text.lower()
        if text == 'nigger' or text == 'jovan' or text == 'nigga' or text == "jamal" or text == 'dean':
            pygame.mixer.music.stop()
            self.label_image1.setPixmap(self.image1)
            self.label_image1.setGeometry(10, 200, 300, 300)
            self.label_image1.setScaledContents(True)
            self.label2.setGeometry(10, 120, 500, 70)
            self.label2.setStyleSheet('font-size: 30px;')
            self.label2.setText(f"YOU'RE BLACK👶🏿👦🏿🍉")

            sound_file = "assets/audio/getout.mp3"
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        
        elif text == 'eguin' or text == 'ajriel':
            self.label_image1.setPixmap(self.image3)
            self.label_image1.setGeometry(10, 305, 300, 300)
            self.label_image1.setScaledContents(True)
            self.label2.setGeometry(10, 120, 700, 200)
            self.label2.setStyleSheet('font-size: 20px;')
            self.label2.setText(f"动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件\n The Tiananmen Square protests of 1989\n 天安門大屠殺 \nThe Tiananmen Square Massacre 反右派鬥爭 \nThe Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 \nHuman Rights 民運 Democratization 自 Freedom 獨立")

            sound_file = "assets/audio/yofon.mp3"
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
        else:
            pygame.mixer.music.stop()
            self.label2.setGeometry(10, 120, 500, 70)
            self.label2.setStyleSheet('font-size: 30px;')
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