import sys
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from goal import Ui_Form2
from UI import Ui_Form
from ans_analysis import analysis
import speech_recognition as sr
import serve
from checkt import checkt
import voice_output
from transformers import BertTokenizer,BertForTokenClassification
tokenizer = BertTokenizer.from_pretrained("C:/Users/lishi/Desktop/train")
model = BertForTokenClassification.from_pretrained("C:/Users/lishi/Desktop/train",num_labels = 10)

class GuiWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton1.clicked.connect(self.serve)
        self.ui.textBrowser.setFont(QtGui.QFont('DFKai-SB',12))
        self.ui.input_label.setFont(QtGui.QFont('DFKai-SB',16))
        self.ui.decode_label.setFont(QtGui.QFont('DFKai-SB',16))
        self.ui.say_label.setFont(QtGui.QFont('DFKai-SB', 16))
        self.ui.say_label.setAlignment(Qt.AlignCenter)
    def serve(self):
        customer = serve.hotle_serve()
        customer.data_clear()
        self.ui.textBrowser.clear()
        QtWidgets.QApplication.processEvents()
        speak="您好 歡迎光臨本飯店"
        voice_output.speak_sentence(speak)
        check = 0
        sum = 0
        while True:
            if sum > 0 and checkt(ans) == 1:
                speak="不好意思請再說一遍"
                voice_output.speak_sentence(speak)
            elif sum == 1 and checkt(ans) == 2 and check == 0:
                speak="請問要甚麼房型"
                self.ui.textBrowser.append("訂房")
                voice_output.speak_sentence(speak)
                check+=1
            elif sum == 1 and checkt(ans) == 3 and check == 0:
                speak="請問需要甚麼餐點"
                self.ui.textBrowser.append("點餐")
                voice_output.speak_sentence(speak)
                check+=1
            elif sum>1 and checkt(ans)==5 and len(customer.meal_list) > 0 or len(customer.room_list) >0:
                speak = "請問還有其他需求嗎"
                voice_output.speak_sentence(speak)
            question = self.speechinput()
            question = "房號是一五九"
            
            self.say_tip_open()
            
            self.say_tip_close()
            self.ui.input_label.setText("輸入:"+question)
            if question == "我要入住":
                speak = "請問房號是多少呢"
                voice_output.speak_sentence(speak)
            print(question)
            if question == "沒有" or question == "不用" or question == "沒有了" or question == "沒了":
                break
            if question == None:
                speak="輸入空白請再說一遍"
                print(speak)
                voice_output.speak_sentence(speak)
                continue
            testing_ids = tokenizer.encode_plus(question,return_tensors = 'pt')
            result = model(testing_ids["input_ids"])
            
            ans = []
            for i in range(len(result[0][0])):
                temp = max(result[0][0][i])
                temp = [k for k, j in enumerate(result[0][0][i]) if j == temp]
                ans.extend(temp)
            ans = ans[1:len(ans)-1]
            for i in range(len(ans)):
                if ans[i]==5:
                    customer.flag = True
                    break
            print(ans)
            self.ui.decode_label.setText("解碼:"+str(ans))
            customer.ans_analysis(question,ans)
            customer.final_process()
            self.sp1(customer)
            sum +=1
    def sp1(self,customer):
        self.ui.textBrowser.clear()
        if customer.flag== False:
            for i in range(len(customer.room_list)):
                temp = customer.room_list[0]['room']  + " " + customer.room_list[0]['count']   
                self.ui.textBrowser.append(temp)
        else:
            for i in range(len(customer.meal_list)):
                temp = customer.meal_list[i]['Meal'] + " "
                if customer.meal_list[i]['quantifier'] != None:
                    temp += customer.meal_list[i]['quantifier'] + " "
                if customer.meal_list[i]['count'] != None:    
                    temp += customer.meal_list[i]['count']
                self.ui.textBrowser.append(temp)
        QtWidgets.QApplication.processEvents()
    def say_tip_open(self):
        self.ui.say_label.setText("Say something!")
        QtWidgets.QApplication.processEvents()
    def say_tip_close(self):
        self.ui.say_label.setText("")
        QtWidgets.QApplication.processEvents()
    def speechinput(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.say_label.setText("請稍等")
            QtWidgets.QApplication.processEvents()
            print("Please wait. Calibrating microphone...")#listen for 5 seconds and create the ambient noise energy level
            r.adjust_for_ambient_noise(source, duration=2)
            print("Say something!")
            self.say_tip_open()
            audio=r.listen(source)
        try:
            sen=r.recognize_google(audio, language="zh-TW")
            print("Google Speech Recognition thinks you said:")            
            return sen
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))
Gui=QApplication(sys.argv)
w=GuiWindow()
w.show()
sys.exit(Gui.exec_())