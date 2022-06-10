import xlrd
import xlwt
data = xlrd.open_workbook(r'C:\Users\84538\Desktop\数据可视化\期末\douban_book\豆瓣推理.xls')
table=data.sheets()[0]
europe=[]
america=[]
china=[]
japan=[]
cnte=0#欧洲
cntc=0#中国
cntj=0#日本
cnta=0#美国

start=1950
end=1960
cnt=0
for rows in range(table.nrows):
    if(cnt!=0):
        country=table.cell_value(rows,2)
        year=int(table.cell_value(rows, 3))
        if(start<year and year<=end ):
            if(country=="中"):
                cntc+=1
            elif (country=="日"):
                cntj+=1

            elif (country == "美"):
                cnta+=1
            else:
                cnte+=1
        else:

            europe.append([start,end,cnte])
            america.append([start,end,cnta])
            china.append([start, end, cntc])
            japan.append([start, end, cntj])
            start=end
            if(start>=2000): end+=5
            else :end+=10
            cnte = 0  # 欧洲
            cntc = 0  # 中国
            cntj = 0  # 日本
            cntam = 0  # 美国
    cnt+=1

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('电影整理',cell_overwrite_ok=True)
col = ('start','end','europe','america','china','japan')
for i in range(6):
    sheet.write(0,i,col[i])
for i in range(len(america)):
    sheet.write(i+1,0,str(america[i][0]))#start
    sheet.write(i + 1, 1, str(america[i][1]))#end
    sheet.write(i + 1, 2, str(europe[i][2]))#europe
    sheet.write(i + 1, 3, str(america[i][2]))#america
    sheet.write(i + 1, 4, str(china[i][2]))#china
    sheet.write(i + 1, 5, str(japan[i][2]))#japan

savepath = r'C:\Users\84538\Desktop\数据可视化\期末\douban_book\统计.xls'
book.save(savepath)
#print(table,type(table))