$(function () {
    $('#changeImage').click(function () {
        // 要给img标签得src得属性重新赋值
        // 浏览器有一个缓存问题 当页面中有请求重复提交 那么服务器会认为你是误操作
        // 所以 不允许提交
        // 所以我们在后面拼接个随机数 鱼目混珠 使用Math.random()方法
        $('#changeImage').attr('src','/axfuser/getcode/?'+Math.random())
    })

})