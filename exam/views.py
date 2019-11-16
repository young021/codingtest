from django.shortcuts import render,redirect
from .models import Seed
from .forms import SeedForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def write(request):        # model 로 자기소개  저는 블로그 형식처럼 제출하고 싶은데
                           # 아니 사실 model 잘 못쓰겠어요..
                           # 오류나요... 

    if request.method=="POST":
        intro=SeedForm(request.POST)
        return redirect('index')
    else:
        return render(request,'intro.html')


#단어 수 세기
# 일단 이거라도 함수는 알고 있어요 시간이 부족해서...ㅠㅠㅠ

# def count(request):          
#     longg=request.GET['']
#     longlong=longg.split()
#     fin={}
#     for a in longlong: 
        #  if a=fin[longlong]:
        #      fin[longlong]+=1
        #  else:
        #      fin[longlong]=1    
       


def about(request):
    return render(request,'aboutrestful.html')


## 엉망진창 죄송해요 ㅠㅠㅠ ㅠㅠㅠㅠ