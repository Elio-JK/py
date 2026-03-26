from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
  return  HttpResponse("Hello World!")

def page1(request):
  return  HttpResponse(render(request, 'app1.html'))

def news(request):
  import requests
  resp = requests.get('https://parkm.fangte.com/api/web/getNewslList?pageIndex=1&pageSize=4&news_type=7&park_id=1')
  news = resp.json();
  m = ['a', 'b', 'c']

  n = { 'x': 1, 'y': 2 }

  return  HttpResponse(render(request, 'news.html', {'news': news, 'm': m, 'n': n}))

def login(request):
  '''
    request.method 接口的请求方法: GET POST
    - 接口请求的参数
    request.GET  get 方式
    request.POST post 方式
  '''


  if request.method == 'GET':
    return  HttpResponse(render(request, 'login.html'))
  
  print(request.POST)

  username = request.POST.get('username')
  password = request.POST.get('password')

  print(username, password)

  if username == 'admin' and  password == '123':
    return redirect('/news/')
  
  return HttpResponse(render(request, 'login.html', {'error': '用户名或密码错误'}))
  

def orm(request):
  from app1.models import UserInfo

  # 新增
  # UserInfo.objects.create(name='admin', password='123')
  # UserInfo.objects.create(name='root', password='222', age=18, size=1.75)


  # 删除
  # UserInfo.objects.filter(name='admin').delete()
  # UserInfo.objects.all().delete()

  # 修改
  # UserInfo.objects.filter(name='admin').update(password='111')
  # UserInfo.objects.all().update(size=1.8)

  # 查询 [<QuerySet>, <QuerySet>]
  # data_list = UserInfo.objects.filter(name='admin') 
  # data_list = UserInfo.objects.all()
  # for item in data_list:
  #   print(item.name, item.password, item.age, item.size)
  obj = UserInfo.objects.all().first() # 获取第一个
  print(obj.name, obj.password, obj.age, obj.size)

  return HttpResponse("ORM 操作成功!")

def users(request):
  from app1.models import UserInfo

  if request.method == 'GET':
    data_list = UserInfo.objects.all()
    return HttpResponse(render(request, 'users.html', { 'users': data_list }))

  obj = request.POST  # 接口请求的参数
  
  name = obj.get('name')
  password = obj.get('password')
  age = obj.get('age')
  size = obj.get('size')

  if age == '':
    age = 2
  
  if size == '':
    size = None

  print(name, password, age, size)
  # 传参： 传递的是什么值，插入数据库的就是什么值
  # 若要取数据库的该字段的默认值, 则直接不传该参数，
  UserInfo.objects.create(name=name, password=password, age=age, size=size)
  return redirect('/users/')

def user_detail(request, id):
  from app1.models import UserInfo

  obj = UserInfo.objects.filter(id=id).first()
  return HttpResponse(render(request, 'user_detail.html', { 'user': obj }))

def template(request):
  return HttpResponse(render(request, 'template.html'))

def student(request):
  # return HttpResponse(render(request, 'student.html'))

  from app1.models import Student
  data_list = Student.objects.all()
  for item in data_list:
    # sex 数据库 1,2 获得 男,女
    # 班级 数据库 1,2,3 获得 1班,2班,3班
    # 创建时间 create_time.strftime('%Y-%m-%d %H:%M:%S'), 在模版中 create_time|date:'%Y-%m-%d %H:%M:%S'
    # 在模版HTML, 也是同样的写法，且函数不需要结尾的括号

    print(item.id, item.name, item.age, item.get_sex_display(), item.grade.name)


  return HttpResponse('学生列表')
