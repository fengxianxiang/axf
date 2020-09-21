$(function () {
init_mySwiper();
init_mySwiper1();
})

function init_mySwiper() {
        var mySwiper=new Swiper('#topSwiper',{
        loop:true,
        autoplay:2000,
        autoplayDisableOnInteraction: false,
        //分页器
        pagination: '.swiper-pagination',
    })

}

function init_mySwiper1() {
        var mySwiper1=new Swiper('#swiperMenu',{
            slidesPerView :3,
        })
}