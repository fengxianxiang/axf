from django.urls import path

from UserApp import views
app_name='axfuser'

urlpatterns=[

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    # 注册的后端验证
    path('checkName/',views.checkName,name='checkName'),
    # 发送邮件 邮件的格式修改
    path('sendemail/',views.sendemail),
    # 邮件的激活 扩展https=http+ssl（安全套接层）
    path('account/',views.account),

    # 登录
    path('getcode/',views.get_code),

]