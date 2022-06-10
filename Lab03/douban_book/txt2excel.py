import xlsxwriter as xw
def isdigit(c):
    if(c<='9' and c>='0'):return 1
    else : return 0

def get_author(data,authors):
    author=''
    start=0
    if(data[0]!='[' and data[0]!='（' and data[0]!='(' and data[0]!='【' and data[0]!='［'):start=1
    for i in data:
        if (i=='/' or i=='、'):
            authors.append(author)
            return 0
        elif (i==']' or i=='）' or i==')' or i=='】'or i=='］'):start=1
        if(start==1 and i!=']' and i!='）'  and i!=')' and i!='】' and i!='］'):author+=i

def get_country(data,countrys):
    country = ''
    start=0
    if(data[0]=='[' or data[0]=='（' or data[0]=='(' or data[0]=='【' or data[0]=='［'):country+=data[1]
    countrys.append(country)
    return 0

def get_date(data,dates):
    date = ''
    cnt=0
    for i in data:
        if(isdigit(i)):
            date+=i
            cnt+=1
        if(cnt==4):
            dates.append(date)
            return 0
    dates.append(date)

def get_bookname(data,names):
    names.append(str(data[:-1]))
    return 0

f=open(r"C:\Users\84538\Desktop\数据可视化\期末\豆瓣读书_推理小说.txt",encoding='utf-8')
authors=[]
countrys=[]
dates=[]
names=[]
data=f.readline()
cnt=0
while(data):
    cnt+=1
    if(data[0]=='书'and data[1]=='名'):get_bookname(data[3:],names)
    elif(data[0]=='作' and data[1]=='者'):
        get_country(data[3:],countrys)
        get_date(data[3:],dates)
        get_author(data[3:],authors)
    data=f.readline()



def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['书名', '作家', '国家','年份']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j][0], data[j][1], data[j][2], data[j][3]]
        print(insertData)
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


# "-------------数据用例-------------"
testData = tuple(zip(names,authors,countrys,dates))
fileName = '豆瓣推理.xlsx'
xw_toExcel(testData, fileName)