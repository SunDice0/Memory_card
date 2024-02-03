from PyQt5.QtWidgets import* 
app = QApplication([]) 
from main_window import* 
from random import choice, shuffle 
 
class Question: 
    def __init__(self,question,answer,w_answer1,w_answer2,w_answer3): 
        self.question=question 
        self.answer=answer 
        self.w_answer1=w_answer1 
        self.w_answer2=w_answer2 
        self.w_answer3=w_answer3 
        self.attemps = 0 
        self.correct = 0 
    def got_right(self): 
        self.attemps+= 1 
        self.correct+= 1 
        print("Це правильна відповідь!") 
     
    def got_wrong(self): 
        self.attemps+=1 
        print("Відповідь невірна") 
 
 
q1 = Question("Яблуко","Apple","Aple","Aplle","Apll") 
q2 = Question("Машина","Car","Machine","Cer","Bus") 
q3 = Question("Будинок","House","Horse","Horny","Home") 
question = [q1,q2,q3] 
 
radio_list=[rbtn1,rbtn2,rbtn3,rbtn4] 
shuffle(radio_list) 
 
def new_question(question,radio_list): 
    random_question = choice(question) 
    text_qwestion.setText(random_question.question) 
    right_answer.setText(random_question.answer) 
    answer=radio_list[0] 
    wrong_answer1,wrong_answer2,wrong_answer3=radio_list[1],radio_list[2],radio_list[3] 
    answer.setText(random_question.answer) 
    wrong_answer1.setText(random_question.w_answer1) 
    wrong_answer2.setText(random_question.w_answer2) 
    wrong_answer3.setText(random_question.w_answer3) 
    return random_question 
 
 
 
def switch_screen(): 
    global random_question 
    if btn_answer.text()=="Відповісти": 
        qwestion_group.hide() 
        answer_group.show() 
        btn_answer.setText("Наступне питання") 
    else: 
        qwestion_group.show() 
        answer_group.hide() 
        btn_answer.setText("Відповісти") 
        random_question=new_question(question,radio_list) 
 
 
main_win= QWidget() 
main_win.resize(600,500) 
main_win.setWindowTitle("Memory Card") 
main_win.move(300,300) 
 
main_win.setLayout(line)     
 
random_question=new_question(question,radio_list) 
 
btn_answer.clicked.connect(switch_screen) 
 
main_win.show() 
 
app.exec()
