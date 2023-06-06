import cn2an
Room_menu = {'單人':1000,'雙人':1750,'四人':3500,'六人':5000}
Room_serve = {'沙拉':220,'三明治':320,'義大利麵':580,'炒麵':380,'炒飯':320,'湯':220}
Liquor = {'雞尾酒':320,'葡萄酒':580,'香檳':420,'啤酒':100,'可樂':80}

def get_meal_price(string,num):
    if num == 1:
        return Room_menu[string]
    if num == 2:
        return Room_serve[string]
    if num == 3:
        return Liquor[string]
def get_number(num_str):
    num = 0
    if ascii('0')<=ascii(num_str[0]) and ascii(num_str[0])<=ascii('9'):
        return int(num_str[0])
    else:
        if num_str[0]=="兩":
            temp = num_str[1:len(num_str)]
            num_str = "二" + temp
        num_str = num_str[0:-1]
        for i in range(len(num_str)):
            num += cn2an.cn2an(num_str[i])
            if cn2an.cn2an(num_str[i])==10:
                continue
            else:
                num *=10
        num /=10
        return int(num)

print(cn2an.an2cn("123",'low'))