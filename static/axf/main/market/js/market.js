// 标签对象 调用事件 . clink blur change keyup submit
// $(this) 代表的是当前的点击对象
// toggleClass会将2哥样式进行互相交换
$(function () {
    $('#all_type').click(function () {
    $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
    $('#all_type_container').toggle();

})

})



$(function () {
    $('#all_sort').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        $('#all_sort_container').toggle();

    })

})