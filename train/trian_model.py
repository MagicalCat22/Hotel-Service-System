import torch
import random
import time
import pandas as pd
from transformers import BertTokenizer,BertForTokenClassification,AdamW, get_linear_schedule_with_warmup
tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
model = BertForTokenClassification.from_pretrained("bert-base-chinese",num_labels = 10)

data = pd.read_csv('C:/Users/lishi/Desktop/train/test.csv',encoding = 'utf-8')
list1 = list(data["sentence"])
list2 = list(data["label"])
label = []
sentence = []
input_ids = []
temp = []
print(type(list2[1]))
for i in range(len(list2)):
    for j in range(0,len(list2[i]),2):
        temp.append(list2[i][j])
    label.append(temp)
    label[i].append('0')
    label[i].insert(0,'0')
    temp = []

for i in range(len(list1)):
    for j in range(len(list1[i])):
        temp.append(list1[i][j])
    sentence.append(temp)
    temp = []

for i in range(len(list1)):
    temp = tokenizer.encode_plus(sentence[i],add_special_tokens = True,return_tensors='pt')
    input_ids.append(temp["input_ids"])

for i in range(len(label)):
    label[i] = list(map(int ,label[i]))
    label[i] = torch.LongTensor(label[i]).unsqueeze(0)

optimizer = AdamW(model.parameters(),
                    lr = 4e-5,
                    eps = 1e-8
                )
epoch = 3
batch = 40
total_step = len(input_ids) * epoch
scheduler = get_linear_schedule_with_warmup(
                        optimizer = optimizer,
                        num_warmup_steps = 0,
                        num_training_steps = total_step
                    )      

for i in range(0,epoch):
    
    shuffle_list = [i for i in range(len(input_ids))]
    random.shuffle(shuffle_list)
    print("Epoch",i+1,":")
    total_train_loss = 0
    model.zero_grad()
    start = time.perf_counter()
    for i in range(len(shuffle_list)):
        random_num = shuffle_list[i]
        
        Forwarding = model.forward(input_ids = input_ids[random_num],labels = label[random_num])

        if i % batch == 0 and i !=0:
            total_train_loss += Forwarding["loss"]

            Forwarding["loss"].backward()

            torch.nn.utils.clip_grad_norm_(model.parameters(),1.0)

            optimizer.step()

            scheduler.step()

            model.zero_grad()
    end = time.perf_counter()
    average_train_loss = total_train_loss / len(shuffle_list)
    print("花費時間:",end-start)
    print("平均Loss:",average_train_loss)
model.save_pretrained("C:/Users/lishi/Desktop/train/")
tokenizer.save_pretrained("C:/Users/lishi/Desktop/train/")
model.eval()
print("train end")