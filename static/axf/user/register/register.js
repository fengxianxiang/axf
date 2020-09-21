$(function () {
    var flagname =false;
    var flagpassword=false;
    $('#exampleInputName').blur(function () {
        // 获取文本框中的内容
        var name = $('#exampleInputName').val();
        // 定义一个正则 正则在js里如何定义呢 regular正则
        var reg = /^[a-z]{3,8}$/;
        // 判断内容是否符合正则
        var boolean = reg.test(name);
        // 如果符合提示可以 绿色字体
        // 提示框去 注册界面写
        // 如果不符合提示用户名字必须符合正则规则 红色字体
        if (boolean){
            // $('#nameinfo').html('用户名可用').css('color','green')
            // 前端验证通过后会执行请求 然后将这个用户名 传到视图函数
            // 视图函数会去数据库验证是否有这个数据 如果有 提示名字不可用
            // 如果没有 那么显示用户名可以使用
            // ajax发送得请求有这几个
            // $.getJson $.get $.post $.ajax
            // 发送ajax第一个方法 $.getJson得参数
            // $.getJson(请求资源路径，请求参数，执行完请求之后获取得值)
            // data就是服务器响应得json数据
            $.getJSON(
                '/axfuser/checkName/',
                {'name':name},function (data) {
                    if (data['status']==200){

                        $('#nameinfo').html(data['msg']).css('color','green');
                        flagname=true
                    }else {
                        $('#nameinfo').html(data['msg']).css('color','red');
                    }
                }
            )
        }else{
            $('#nameinfo').html('用户名不可用，必须是3到8个英文字模').css('color','red');
        }
    })

    $('#exampleInputPassword2').blur(function () {
        var password1 = $('#exampleInputPassword1').val()
        var password2 = $('#exampleInputPassword2').val()
        if (password1==password2){
            $('#passwordinfo').html('密码一致').css('color','green')
            flagpassword=true
        }else {
            $('#passwordinfo').html('密码不一致').css('color','red')
        }
    })
        $('form').submit(function () {
            // submit 方法中 只有返回true 才可以提交表单 否则提交不了
            var name =$('#exampleInputName').val();
            if (!name){
                $('#nameinfo').html('用户名不能为空').css('color','red')
            }
            var password =$('#exampleInputPassword1').val()
            if ('!password'){
                $('#passwordinfo').html('密码不能为空').css('color','red')

            }   return false;
            var boolean=flagpassword&flagname;
            if (boolean==1){
                // 对密码进行md5加密
                password=md5(password)
                // 然后将加密后得密码重新赋值给密码
                $('#exampleInputPassword1').val(password);
                return true;
            }else {
                return false;

            }


        })

})