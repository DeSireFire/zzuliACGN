(function ($) {
    var enum_obj = {
        '1':'tf-menu',
        '2':'tf-home',
        '3':'tf-about',
        '4':'tf-team',
        '5':'tf-services#tf-services-title',
        '6':'tf-services-painter',
        '7':'tf-services-OtakuDancing',
        '8':'tf-services-WotaGeiClub',
        '9':'tf-services-TechOtakus',
        '10':'tf-services-K-onOtakus',
        '11':'tf-clients',
        '12':'tf-works',
        '13':'tf-testimonials',
        '14':'tf-contact',
        '15':'footer'
    };
    var pos = 3;
    var MAX_POS = 15;
    var LIST_ITEM_SIZE = 1;
    //滚动条距底部的距离
    var BOTTOM_OFFSET = 0;
    showItems();
    $(document).ready(function () {
        $(window).scroll(function () {
            var $currentWindow = $(window);
            //当前窗口的高度
            var windowHeight = $currentWindow.height();
            console.log("current widow height is " + windowHeight);
            //当前滚动条从上往下滚动的距离
            var scrollTop = $currentWindow.scrollTop();
            console.log("current scrollOffset is " + scrollTop);
            //当前文档的高度
            var docHeight = $(document).height();
            console.log("current docHeight is " + docHeight);
 
            //当 滚动条距底部的距离 + 滚动条滚动的距离 >= 文档的高度 - 窗口的高度
            //换句话说：（滚动条滚动的距离 + 窗口的高度 = 文档的高度）  这个是基本的公式
            if ((BOTTOM_OFFSET + scrollTop) >= docHeight - windowHeight && pos != MAX_POS) {
                showItems();
            }
        });
    });
 
    function showItems() {
        if(pos == MAX_POS){
            return;
        }
        for (var i = pos; i < pos + 1; ++i) {
            if(pos == 5){
                $("#" + enum_obj[pos].split("#")[0]).css('display','block');
                $("#" + enum_obj[pos].split("#")[1]).css('display','block');
                break;
            }
            $("#" + enum_obj[pos]).css('display','block');
        }
        pos += LIST_ITEM_SIZE;
    }
})(jQuery);
