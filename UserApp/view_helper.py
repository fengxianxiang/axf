# 这里封装方法
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader


def sendEmail(name,email,token):
    # subject, message, from_email, recipient_list
    # 主题
    subject='天上人间十年大酬宾，随便玩'
    message=''
    from_email='18502196569@163.com'
    recipient_list=[email]

    index=loader.get_template('axf/user/register/active.html')
    context={
        'name':name,
        # url 应该是一个请求资源路径 专门用来修改当前对象的激活状态
        # token是uuid类 不能直接和字符串拼接 需要强转
        # 发送了token
        'url':'http://123.57.72.207:8000/axfuser/account/?token='+str(token)
    }



    result=index.render(context=context)
    html_message=result


    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,html_message=html_message)

    return HttpResponse('发送成功')