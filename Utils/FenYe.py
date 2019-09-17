from  materials import models
class SetPage(object):
    def __init__(self,currentPage,perPage,data_count,pageRange,pageName):
        try:
            self.currentPage=int(currentPage)
        except Exception as e:
            self.currentPage=1
        self.perPage=perPage
        self.data_count=data_count
        self.pageRange=pageRange
        self.pageName=pageName
        a,b=divmod(self.data_count,self.perPage)
        if b:
            a=a+1
        self.CalcPage=a
    def getPageCount(self):

        pageList=[]
        half=int((self.pageRange-1)/2)
        if self.CalcPage<self.pageRange:
            pageLeft=1
            pageRight=self.CalcPage
        else:
            if self.currentPage<=half:
                pageLeft=1
                pageRight=self.pageRange
            else:
                if self.currentPage+half>=self.CalcPage:
                    pageLeft=self.CalcPage-self.pageRange+1
                    pageRight=self.CalcPage
                else:
                    pageLeft=self.currentPage-half
                    pageRight=self.currentPage+half+1
        if self.currentPage<=1:
            # prev="<li><a href='#'>上一页</a></li>"
            prev="<li><a href='#'>首页</a></li>"
            pageList.append(prev)
        else:
            # prev="<li><a href" \
            #      "='http://127.0.0.1:8000/materials/?page=%s'>上一页</a></li>"%(self.currentPage-1)
            prev="<li><a href" \
                 "='http://127.0.0.1:8000/materials/%s?page=%s'>首页</a></li>"%(self.pageName,1)
            pageList.append(prev)


        for i in range(pageLeft,pageRight+1):
            if i==self.currentPage:
                temp="<li class='active'><a href" \
                     "='http://127.0.0.1:8000/materials/%s?page=%s'>%s</a></li>"%(self.pageName,i,i)
            else:
                temp="<li><a href" \
                     "='http://127.0.0.1:8000/materials/%s?page=%s'>%s</a></li>"%(self.pageName,i,i)
            pageList.append(temp)
        if self.currentPage>=self.CalcPage:
            # next="<li><a href='#'>下一页</a></li>"
            next="<li><a href='#'>第%s页</a></li>"%(self.CalcPage)
            pageList.append(next)
        else:
            # next="<li><a  href" \
            #      "='http://127.0.0.1:8000/materials/?page=%s'>下一页</a></li>"%(self.currentPage+1)
            next="<li><a  href" \
                 "='http://127.0.0.1:8000/materials/%s?page=%s'>第%s页</a></li>"%(self.pageName,self.CalcPage,self.CalcPage)
            pageList.append(next)
        return ''.join(pageList)

        # return pageList
    def getPageData(self):
        self.start=(self.currentPage-1)*self.perPage
        self.end=self.currentPage*self.perPage
        a=models.Fabric.objects.all()[self.start:self.end]
        return a
    def getLeatherData(self):
        self.start=(self.currentPage-1)*self.perPage
        self.end=self.currentPage*self.perPage
        a=models.Leather.objects.all()[self.start:self.end]
        return a