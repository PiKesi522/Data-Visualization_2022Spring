import xlrd
import xlwt
data = xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\剧本杀.xls')
data2=xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\悬疑电影.xls')
data3=xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\悬疑小说.xls')
table=data.sheets()[0]
table2=data2.sheets()[0]
table3=data3.sheets()[0]
jbs=[]
movie=[]
novel=[]
year=[]
cnt =0
start_year=2011
sum=0
for rows in range(table.nrows):
    sum+=int(table.cell_value(rows,1))
    cnt+=1
    if(start_year%4!=0):
        if(cnt==365):
            cnt=0
            year.append(start_year)
            jbs.append(sum)
            #print(start_year,sum)
            start_year+=1
            sum=0
    else:
        if (cnt == 366):
            cnt = 0
            year.append(start_year)
            jbs.append(sum)
            #print(start_year, sum)
            start_year += 1
            sum = 0
cnt=0
for rows in range(table2.nrows):
    sum+=int(table2.cell_value(rows,1))
    cnt+=1
    if(start_year%4!=0):
        if(cnt==365):
            cnt=0
            movie.append(sum)
            #print(start_year,sum)
            start_year+=1
            sum=0
    else:
        if (cnt == 366):
            cnt = 0
            movie.append(sum)
            #print(start_year, sum)
            start_year += 1
            sum = 0
cnt=0
for rows in range(table3.nrows):
    sum+=int(table3.cell_value(rows,1))
    cnt+=1
    if(start_year%4!=0):
        if(cnt==365):
            cnt=0
            novel.append(sum)
            #print(start_year,sum)
            start_year+=1
            sum=0
    else:
        if (cnt == 366):
            cnt = 0
            novel.append(sum)
            #print(start_year, sum)
            start_year += 1
            sum = 0

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('剧本杀',cell_overwrite_ok=True)
col = ('year','jbs','movie','novel')
for i in range(4):
    sheet.write(0,i,col[i])
for i in range(len(jbs)):
    sheet.write(i+1,0,str(year[i]))
    sheet.write(i + 1, 1, str(jbs[i]))
    sheet.write(i + 1, 2, str(movie[i]))
    sheet.write(i + 1, 3, str(novel[i]))

savepath = r'C:\Users\84538\Desktop\数据可视化\期末\剧本杀x.xls'
book.save(savepath)
#print(table,type(table))