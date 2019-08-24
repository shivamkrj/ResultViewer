import re
from robobrowser import RoboBrowser

fl=open("result_tpc.txt",'w')
fl.write("Result:\n")
i=0
for i in range(1604310009,1604310013):

    br = RoboBrowser(history=True)
    br.open('http://www.bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx')
    form = br.get_form()
    form["ctl00$ContentPlaceHolder1$ddlAcademicSession"].value = '2017-2018'
    # form[" "] = "3"
    form['ctl00$ContentPlaceHolder1$ddlSem'].value = '3'
    form['ctl00$ContentPlaceHolder1$ddlResultCategory'].value = 'R'
    form['ctl00$ContentPlaceHolder1$txtRollno'] = i
    # br.session.headers['Referer'] ='frmprintreport.aspx'
    html = br.submit_form(form)
    src = str(br.parsed())
    # print(src)
    m = re.search('<span id="ctl00_ContentPlaceHolder1_omk">', src)
    print("hello1")
    if(not m):
        continue
    t = m.end()
    newstring = src[t:t + 3]
    f = int(newstring)
    f = f / 10

    m = re.search('<span id="ctl00_ContentPlaceHolder1_sName">', src)

    t = m.end()
    new = src[t:t + 50]
#    print(new)
    m = re.search('</span></td>', new)
    # print(newstring)
    t=m.start()
    new2=new[0:t]
    print(new2)
    n=str(new2)
    print(n)




    fl.write(str(i))
    fl.write(" : ")
    fl.write(n)
    fl.write(" : ")
    fl.write(str(f))
    fl.write("\n")

 #   print("Percentage is :")
    print(i)


