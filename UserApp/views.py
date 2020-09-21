import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from UserApp.models import AxfUser
from UserApp.view_helper import sendEmail
from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register/register.html')
    elif request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        # 密码加密make_password check_password()密码解密
        password = make_password(password)

        user = AxfUser()
        user.name = name
        user.password = password
        user.email = email
        user.icon = icon

        token = uuid.uuid4()
        user.token = token
        user.save()
        # 设置一个key 一个value ；
        # 谁是key谁是value token当作key user.id做value 然后过期时间是60s
        # 我们缓存的时候绑定了一个token
        # 将token和user.id都放到了缓存中
        cache.set(token, user.id, timeout=60)

        # 然后发送邮件了 执行了激活的请求
        sendEmail(name, email, token)

        # 发送邮件进行激活 1 创建一个view_helper.py 进行方法的封装

        return HttpResponse('注册成功')


def login(request):
    if request.method=='GET':
        return render(request, 'axf/user/login/login.html')
    elif request.method=='POST':
        # 先验证验证码 减少io操作

        # 然后获取到页面中你输入得验证码
        imgcode=request.POST.get('imgCode')
        # 然后将他与随机生成得验证码对比 这个验证码永远都是和session绑定的
        # 先获取到session的验证码
        verify_code=request.session.get('verify_code')
        if imgcode.lower()== verify_code.lower():
            return redirect(reverse('axfmine:mine'))
        else:
            # 这里就要给他有个错误信息
            # 然后去from表单里面用span标签进行接收
            context={
                'msg':'验证码错误'
            }
            return render(request,'axf/user/login/login.html',context=context)







def checkName(request):
    data = {
        'status': 200,
        'msg': '用户名可用'
    }

    # 先把前端传过来得数据获取到 这里获取到得是name
    name = request.GET.get('name')
    # 然后去数据库查找 进行判断
    users = AxfUser.objects.filter(name=name)
    # 获取单个数据 get first last exists count
    if users.exists():
        data['msg'] = '用户名已存在'
        data['status'] = 201
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def sendemail(request):
    # subject, message, from_email, recipient_list,
    # 主 题
    subject = '激活'
    # 邮件的内容
    message = '你果然是天下一第美男子'
    # 邮件内容的定制 message与html_message必须在一块
    # 邮件如何返回一个html界面呢 1 先写一个模板 2 使用loader方法进行加载 3使用 index.render方法渲染 这个方法里面的参数是一个字典
    # 加载
    index = loader.get_template('axf/user/register/active.html')
    # 渲染
    context = {
        'name': '老李',
        'url': 'http://www.1hhhh.com'
    }
    result = index.render(context=context)

    html_message = result

    # 发送者
    form_email = '18502196569@163.com'
    # 接收者
    recipient_list = ['3486323186@qq.com']

    send_mail(subject=subject, message=message, html_message=html_message, from_email=form_email,
              recipient_list=recipient_list)

    return HttpResponse('发送成功')


def account(request):
    # count 返回当前查询集中的对象个数
    # 进入到这个视图函数之后干啥
    # 1 将当前注册的用户的激活状态修改为True
    # 2 查询当前用户的数据 如何找呢 设置一个唯一串 token
    token = request.GET.get('token')

    # 我们在这获取到token
    user_id = cache.get(token)

    # user=AxfUser.objects.filter(token=token)
    # if user.count() >0:
    #     user=user.first()
    #     user.active=True
    #     user.save()
    #     return HttpResponse('激活成功')

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.active = True
        user.save()

        #    我们刚才做的是在缓存时间内可以一只激活
        # 所以我们要在缓存时间内激活一次之后就把缓存删除
        # 那么我们应该在哪个函数中去做呢 删除缓存的方法是delete
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送邮件')

    # 登录





def get_code(request):
    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)
    # 导包的时候  你导入的PIL下的Image的image
    # from PIL.Image import Image
    image = Image.new(mode=mode, size=size, color=color_bg)
    imagedraw = ImageDraw(image, mode=mode)
    # FONT_PATH 验证码的字体
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code