from django.http import \
    request
from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import HttpResponse
from pymysql.cursors import \
    DictCursor
import pymysql
from django.db import connections,transaction,connection

def cla(request):
    if request.method=="POST":
        add= request.POST.get('add')
        delete=request.POST.get('delete')
        if add:
            className_sub=request.POST.get('add')
            connect1=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='ldj079161',db='db1')
            cursor=connect1.cursor(cursor=DictCursor)
            cursor.execute("insert into class(ClassName) values (%s)",className_sub)
            connect1.commit()
            cursor.close()
            connect1.close()
            return HttpResponse(1)
        if delete:
            classId=request.POST.get('delete')
            connect1=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='ldj079161',db='db1')
            cursor=connect1.cursor(cursor=DictCursor)
            cursor.execute("delete from class where id =(%s)",classId)
            connect1.commit()
            cursor.close()
            connect1.close()
            return HttpResponse(0)
    else:

        connect1=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='ldj079161',db='db1')
        cursor=connect1.cursor(cursor=DictCursor)
        connection.cursor()
        cursor.execute("select id ,ClassName from class")
        result=cursor.fetchall()
        cursor.close()
        connect1.close()
        return render(request,
                      '0cla.html',
                      {'class_list':result})

def newClass(request):
    if request.method=="GET":
        return render(request,
                      '3newClass.html',
                     )
    else:
        print(request.POST)
        className_sub=request.POST.get('className_sub')
        connect1=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='ldj079161',db='db1')
        cursor=connect1.cursor(cursor=DictCursor)
        cursor.execute("insert into class(ClassName) values (%s)",className_sub)
        connect1.commit()
        cursor.close()
        connect1.close()
        return redirect('/cla/')
def newStudent(request):

    if request.method=="GET":
        return render(request,
                      '3newClass.html',
                      )
    else:
        from django.db import connection,transaction
        cursor = connection.cursor()            #获得一个游标(cursor)对象
    #更新操作
        className_sub=request.POST.get('className_sub')
        cursor.execute( "insert into class(ClassName) values (%s)",className_sub)
        # transaction.commit()     #提交到数据库
        return redirect('/cla/')
def materials(request):
    return render(request,
                  'Materials/../materials/materials.html',
                  )
def materialsList(request):
    return render(request,
                  'Materials/../materials/materials.html',
                  )
def fabricDetail(request,id):
    print(id)
    return HttpResponse('materials '+str(id))


def index(request):
    return render(request,
                  'Materials/template_include.html',
                  )




