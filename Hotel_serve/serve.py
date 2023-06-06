class hotle_serve:
    def __init__(self, room_list = None,meal_list = None,flag = False,type = False):
        self.room_list = room_list
        self.meal_list = meal_list
        self.flag = flag
        self.type = type
    def data_clear(self):
        self.room_list = []
        self.meal_list = []
        self.flag = False
        self.type = int(0)
    def ans(self,sentence,ans):
        if self.flag==False:    
            temp = []
            serve = dict()
            serve['count'] = None
            serve['room'] = None
            serve['date'] = None
            serve['room_num'] = None
            sentence = list(sentence)
            for i in range(len(ans)):
                if ans[i]==0:
                    continue
                if ans[i]==1:
                    if i==(len(ans)-1):
                        temp.extend(sentence[i])
                        serve['count'] = temp
                        self.room_list.append(serve)
                        return
                    elif ans[i+1]!=1:
                        temp.extend(sentence[i])
                        serve['count'] = temp
                        temp = []
                        if serve['room'] != None:
                            self.room_list.append(serve)
                            serve = {}
                            serve['room'] = None
                            serve['count'] = None
                            serve['date'] = None
                            serve['room_num'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i]==2:
                    if i==(len(ans) -1):
                        temp.extend(sentence[i])
                        serve['room'] = temp
                        self.room_list.append(serve)
                        return
                    elif ans[i+1]!=2:
                        temp.extend(sentence[i])
                        serve['room'] = temp
                        temp = []
                        if serve['count'] != None:
                            self.room_list.append(serve)
                            serve = {}
                            serve['room'] = None
                            serve['count'] = None
                            serve['date'] = None
                            serve['room_num'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i]==3:
                    if i==(len(ans) -1):
                        temp.extend(sentence[i])
                        serve['date'] = temp
                        self.room_list.append(serve)
                        return
                    elif ans[i+1]!=3:
                        temp.extend(sentence[i])
                        serve['date'] = temp
                        temp = []
                        if serve['room'] != None:
                            self.room_list.append(serve)
                            serve = {}
                            serve['room'] = None
                            serve['count'] = None
                            serve['room_num'] = None
                            serve['date'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i] == 4:
                    self.type = 1
                if ans[i] == 5:
                    self.type = 2
                if ans[i]==6:
                    if i==(len(ans) -1):
                        temp.extend(sentence[i])
                        serve['room_num'] = temp
                        self.room_list.append(serve)
                        return
                    elif ans[i+1]!=6:
                        temp.extend(sentence[i])
                        serve['room_num'] = temp
                        temp = []
                        self.room_list.append(serve)
                        serve = {}
                        serve['room'] = None
                        serve['count'] = None
                        serve['room_num'] = None
                        serve['date'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i] == 7:
                    self.type = 3
        else:
            temp =[]
            serve = dict()
            serve['count'] = None
            serve['Meal'] = None
            sentence = list(sentence)
            for i in range(len(ans)):
                if ans[i]==0:
                    continue
                if ans[i]==1:
                    if i==(len(ans)-1):
                        temp.extend(sentence[i])
                        serve['count'] = temp
                        self.meal_list.append(serve)
                        return
                    elif ans[i+1]!=1:
                        temp.extend(sentence[i])
                        serve['count'] = temp
                        temp = []
                        if serve['Meal'] != None:
                            self.meal_list.append(serve)
                            serve = {}
                            serve['count'] = None
                            serve['Meal'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i]==8:
                    self.flag = True
                    self.type = 4
                    if i==(len(ans)-1):
                        temp.extend(sentence[i])
                        serve['Meal'] = temp
                        self.meal_list.append(serve)
                        return
                    elif ans[i+1]!=8:
                        temp.extend(sentence[i])
                        serve['Meal'] = temp
                        temp = []
                        if serve['count'] != None:
                            self.meal_list.append(serve)
                            serve = {}
                            serve['count'] = None
                            serve['Meal'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
                if ans[i]==9:
                    self.flag = True
                    self.type = 4
                    if i==(len(ans)-1):
                        temp.extend(sentence[i])
                        serve['Meal'] = temp
                        self.meal_list.append(serve)
                        return
                    elif ans[i+1]!=9:
                        temp.extend(sentence[i])
                        serve['Meal'] = temp
                        temp = []
                        if serve['count'] != None:
                            self.meal_list.append(serve)
                            serve = {}
                            serve['count'] = None
                            serve['Meal'] = None
                        continue
                    else:
                        temp.extend(sentence[i])
    def final_process(self):
        if self.flag == False:
            for i in range(len(self.room_list)):
                if  self.room_list[i]['room'] != None:
                    self.room_list[i]['room'] = str(''.join(self.room_list[i]['room']))
                if self.room_list[i]['count'] != None:
                    self.room_list[i]['count'] = str(''.join(self.room_list[i]['count']))
                if self.room_list[i]['date'] != None:
                    self.room_list[i]['date'] = str(''.join(self.room_list[i]['date']))
                if self.room_list[i]['room_num'] != None:
                    self.room_list[i]['room_num'] = str(''.join(self.room_list[i]['room_num']))
        else:
            for i in range(len(self.meal_list)):
                if self.meal_list[i]['Meal'] != None:
                    self.meal_list[i]['Meal'] = str(''.join(self.meal_list[i]['Meal']))
                if self.meal_list[i]['count'] != None:
                    self.meal_list[i]['count'] = str(''.join(self.meal_list[i]['count']))