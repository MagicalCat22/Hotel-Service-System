import sys
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from UI import Ui_Form
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
        self.ui.input_label.setFont(QtGui.QFont('DFKai-SB',12))
        self.ui.decode_label.setFont(QtGui.QFont('DFKai-SB',12))
        self.ui.say_label.setFont(QtGui.QFont('DFKai-SB', 16))
        self.ui.say_label.setAlignment(Qt.AlignCenter)
    def serve(self):
        customer = serve.hotle_serve()
        customer.data_clear()
        self.ui.textBrowser.clear()
        QtWidgets.QApplication.processEvents()
        speak="您好 歡迎光臨本飯店"
        voice_output.speak_sentence(speak)
        ans =[]
        sum = 0
        check = 0
        flag = 0
        while True:
            if sum > 0 and checkt(ans) == 0:
                speak = "不好意思請再說一遍"
                voice_output.speak_sentence(speak)
            elif sum == 1 and checkt(ans) == 1 and customer.type == 1:
                speak = "請問房型跟數量呢"
                check += 1
                self.ui.textBrowser.append("訂房")
                voice_output.speak_sentence(speak)
            elif sum > 0 and checkt(ans) == 2:
                speak = "請問甚麼時候會入住呢"
                check += 1
                voice_output.speak_sentence(speak)
            elif sum > 0 and (checkt(ans) == 3 and (check == 2 or check == 1) or checkt(ans) == 4):
                speak = "好的已幫您完成訂房手續"
                voice_output.speak_sentence(speak)
                flag = 1
                break
            elif sum > 0 and checkt(ans) == 5 and customer.type == 2:
                speak = "請問房號是多少呢"
                self.ui.textBrowser.append("退房")
                voice_output.speak_sentence(speak)
            elif sum > 0 and checkt(ans) == 6 and customer.type == 2:
                speak = "好的已幫您完成退房手續祝您旅途平安"
                voice_output.speak_sentence(speak)
                flag = 1
                break
                
            elif sum > 0 and checkt(ans) == 7 and customer.type == 3:
                self.ui.textBrowser.append("入住")
                speak = "請問房號是多少呢"
                voice_output.speak_sentence(speak)
            elif sum > 0 and checkt(ans) == 6 and customer.type == 3:
                speak = "好的以幫您辦好入住手續祝您入住愉快"
                voice_output.speak_sentence(speak)
                flag = 1
                break
            elif sum > 0 and checkt(ans) == 8 and customer.type == 4:
                speak = "好的請問還有其他需求嗎"
                voice_output.speak_sentence(speak)
            sum+=1
            question = self.speechinput()
            self.say_tip_close()
            if question!="":
                question=question.replace('駐','住')
                question = self.an2cn(question)
            self.ui.input_label.setText("輸入:"+question)
            print(question)
            if question == "沒有" or question == "不用" or question == "沒有了" or question == "沒了" or question == "謝謝" or question == "好的" or question == "好的謝謝":
                if customer.type == 4:
                    speak = "祝您用餐愉快"
                    voice_output.speak_sentence(speak)
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
                if ans[i] == 8 or ans [i] == 9:
                    customer.flag = True
            print(ans)
            self.ui.decode_label.setText("解碼:"+str(ans))
            customer.ans(question,ans)
            customer.final_process()
            self.ui.textBrowser.clear()
            self.sp1(customer)
            if flag == 1:
                break
            
    def sp1(self,customer):
        self.ui.textBrowser.clear()
        temp = ""
        if customer.flag== False:
            for i in range(len(customer.room_list)):
                if customer.room_list[i]['room'] != None:
                    temp = "房型:" + customer.room_list[i]['room']
                if customer.room_list[i]['count'] != None:
                    temp += '\n' + "數量:" + customer.room_list[i]['count']
                if customer.room_list[i]['date'] != None:
                    temp +='\n' + "日期:" + customer.room_list[i]['date']
                if customer.room_list[i]['room_num'] != None:
                    temp += "房號:" + customer.room_list[i]['room_num']
                self.ui.textBrowser.append(temp)
        else:
            for i in range(len(customer.meal_list)):
                if customer.meal_list[i]['Meal'] != None:
                    temp += "餐點:" + customer.meal_list[i]['Meal'] + " "
                if customer.meal_list[i]['count'] != None:
                    temp += "數量:" + customer.meal_list[i]['count'] + '\n'
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
            print("Please wait. Calibrating microphone...")
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
    def an2cn(self,input):
        input = input.replace('1','一')
        input = input.replace('2','二')
        input = input.replace('3','三')
        input = input.replace('4','四')
        input = input.replace('5','五')
        input = input.replace('6','六')
        input = input.replace('7','七')
        input = input.replace('8','八')
        input = input.replace('9','九')
        return input       
Gui=QApplication(sys.argv)
w=GuiWindow()
w.show()
sys.exit(Gui.exec_())