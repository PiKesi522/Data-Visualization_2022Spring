import xlrd
import xlwt
data = xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\福尔摩斯.xls')
data2=xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\神探夏洛克.xls')
table=data.sheets()[0]
table2=data2.sheets()[0]
fms=[]
slk=[]
year=[]
cnt =0
start_year=2011
sum=0
print('fms')
for rows in range(table.nrows):
    sum+=int(table.cell_value(rows,1))
    cnt+=1
    if(start_year%4!=0):
        if(cnt==365):
            cnt=0
            year.append(start_year)
            fms.append(sum)
            #print(start_year,sum)
            start_year+=1
            sum=0
    else:
        if (cnt == 366):
            cnt = 0
            year.append(start_year)
            fms.append(sum)
            #print(start_year, sum)
            start_year += 1
            sum = 0
print('slk')
cnt=0
for rows in range(table2.nrows):
    sum+=int(table2.cell_value(rows,1))
    cnt+=1
    if(start_year%4!=0):
        if(cnt==365):
            cnt=0
            slk.append(sum)
            #print(start_year,sum)
            start_year+=1
            sum=0
    else:
        if (cnt == 366):
            cnt = 0
            slk.append(sum)
            #print(start_year, sum)
            start_year += 1
            sum = 0
print(fms)
print(slk)
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('福尔摩斯与神探夏洛克',cell_overwrite_ok=True)
col = ('year','fms','slk')
for i in range(3):
    sheet.write(0,i,col[i])
for i in range(len(slk)):
    sheet.write(i+1,0,str(year[i]))#start
    sheet.write(i + 1, 1, str(fms[i]))#end
    sheet.write(i + 1, 2, str(slk[i]))#europe

savepath = r'C:\Users\84538\Desktop\数据可视化\期末\统计热度.xls'
book.save(savepath)
#print(table,type(table))