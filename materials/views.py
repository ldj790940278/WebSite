# from django.core import \
#     paginator
from django.core.paginator import \
    Paginator
from django.http import \
    FileResponse
from django.shortcuts import \
    HttpResponse
from django.shortcuts import render

# Create your views here.
from Utils.FenYe import \
    SetPage
from materials.models import \
    Fabric, \
    Leather
from  materials import models



# django自带分页
def materials(request):

    fabric_list=models.Fabric.objects.filter(id__gt=100).delete()
    fabric_list=models.Fabric.objects.all()
    page=Paginator(fabric_list,10)
    currentPage=request.GET.get('page')
    fabric_list=page.page(currentPage)
    return render(request,
                  'Materials/materials.html',{"fabric_list":fabric_list}
                  )
# 自定义分页
def fabric(request):

    return render(request,
                  'Materials/fabric.html',
                  )
def fabric001(request):
    return render(request,
                  'Materials/fabric001.html',
                  )
def queryByOrm(request):
    from  materials import models

    #查询某个
    # fabric_list=models.Fabric.objects.filter(id=1)
    #删除大于9 ，小于是lt
    # fabric_list=models.Fabric.objects.filter(id__gt=7).delete()
    #更新
    # fabric_list=models.Fabric.objects.filter(id=2).update(img_file='images/cup.png')
    # fabric_list=models.Fabric.objects.filter(id=6).update(img_file='images/sea.jpg')
    # fabric_list=models.Fabric.objects.filter(id=7).update(img_file='images/sky.jpg')
    # fabric_list=models.Fabric.objects.filter(id=8).update(img_file='images/sea.jpg')
    # fabric_list=models.Fabric.objects.filter(id=9).update(img_file='images/sky.jpg')
    # 查询所有
    fabric_list=models.Fabric.objects.all()
    return render(request,
                  'Materials/queryByOrm.html', {"fabric_list":fabric_list}
                  )
def upload(request):
    if request.method=="GET":
        return render(request,
                      'Materials/upload.html',
                      )
    else:
        img_name=request.POST.get('img_name')
        img_file=request.FILES.get('img_file')
        Fabric.objects.create(img_name=img_name,img_file=img_file)

        from  materials import models
        fabric_list=models.Fabric.objects.all()
        print(fabric_list)

        return render(request,
                      'Materials/materials.html', {"fabric_list":fabric_list}
                      )
def materials2(request):
    data_count=models.Fabric.objects.all().count()
    currentPage=request.GET.get('page')
    defPage=SetPage(currentPage,6,data_count,10,"fabric")
    # perPage=10
    # dataStart=(currentPage-1) * perPage
    # dataEnd=currentPage * perPage
    fabric_list=defPage.getPageData()
    page_list=defPage.getPageCount()
    return render(request,
                  'Materials/materials.html',{"fabric_list":fabric_list,"allPage":page_list}
                  )
def leather(request):
    #创建数据，填充
    Leather.objects.create(img_name='adf',img_file='images/cup.png')
    data_count=models.Leather.objects.all().count()
    currentPage=request.GET.get('page')
    defPage=SetPage(currentPage,5,data_count,10,"leather")
    leather_list=defPage.getLeatherData()
    page_list=defPage.getPageCount()
    return render(request,
                  'Materials/materials.html', {"fabric_list":leather_list,"allPage":page_list}
                  )
def download(request):
    # file=open('Static/media/images/cup.png','rb')#rb代表	以二进制格式打开一个文件用于只读。
    # file=open('Static/media/images/cup.png','rb')#rb代表	以二进制格式打开一个文件用于只读。
    # response =HttpResponse(file)
    # response['Content-Type']='application/octet-stream'
    # response['Content-Disposition']='attachment;filename="fabric01"'
    file=open('Static/media/images/fuck.rar','rb')
    response =FileResponse(file)
    response['Content-Type']='application/x-zip-compressed'
    response['Content-Disposition']='attachment;filename="fuck.zip"'
    return response
