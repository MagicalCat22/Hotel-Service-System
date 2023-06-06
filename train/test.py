from transformers import BertTokenizer,BertForTokenClassification
tokenizer = BertTokenizer.from_pretrained("C:/Users/lishi/Desktop/train")
model = BertForTokenClassification.from_pretrained("C:/Users/lishi/Desktop/train",num_labels = 10)

question = "我要訂四間雙人房"
testing_ids = tokenizer.encode_plus(question,return_tensors = 'pt')
result = model(testing_ids["input_ids"])
ans = []
for i in range(len(result[0][0])):
    temp = max(result[0][0][i])
    temp = [k for k, j in enumerate(result[0][0][i]) if j == temp]
    ans.extend(temp)
ans = ans[1:len(ans)-1]
print(ans)