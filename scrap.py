import requests
import pymysql
from bs4 import BeautifulSoup
from datetime import time
from datetime import date

def time_con(input):
    
    timecon=time(int(input.split(':')[0]),int(input.split(':')[1]))
    return timecon
def date_con(input):
    current_datetime=date.today()
    current_year = int(current_datetime.strftime("%Y"))
    datecon=date(current_year,int(input.split('.')[1]),int(input.split('.')[0]))
    return datecon

mydb=pymysql.connect(user='root',passwd="root",host='localhost',database='contest')
if(mydb!=None):
    print("connection successful")
def db():
    mycur=mydb.cursor()
    mycur.execute("drop table contest_table")

    mycur.execute("create table contest_table(Name varchar(800),web text,Time_of_contest time, Date_of_contest date);")
    for i in g:
        t=time_con(i[2].split()[2])
        d=date_con(i[2].split()[0])
        print(i[1],t,d)
        k="insert into contest_table values('{}','{}','{}','{}')".format(i[0].replace('\'',''),i[1],t,d)
        print(k)
        mycur.execute(k)
    mydb.commit()
def clist():
    url="https://clist.by/"
    res=requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    div=soup.find_all('div')
    # print(div)
    for i in div:
        j=i.find('div',class_="col-md-7 col-sm-8 event")
        n=i.find('div',class_="col-md-5 col-sm-12 start-time")
            
        if(j):
            k=j.find('a',class_="title_search")
            if('clist' not in k['href']):
                g.append([k.text,k['href'],n.text.strip()])
g=[]
# fetch_codeforces()
# fetch_leetcode()
clist()
# print(g)
db()
# fetch_codechef()
# print(soup.encode("utf-8"))