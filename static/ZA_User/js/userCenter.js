(function(){
//有人拖窗口时响应
window.onresize=function(){becomeSmall()}
//使两个边框高度相等
function equalHeight(){
    $(".box1")[0].offsetHeight=$(".box2")[0].offsetHeight
}

//以768px为分界线 改变左侧样式
function becomeSmall(){
    if((document.documentElement.clientWidth)<768) {
        $('.box1').addClass("is-open")
        $(".user-Center-Container").addClass("is-open")
    }else{
        $('.box1').removeClass("is-open")
        $(".user-Center-Container").removeClass("is-open")
    }
    equalHeight()
}
//事件绑定
function bindEvent(){
    //小窗口左侧图标
    $(".user-Center-Container").click(function(){
        $('.box1').addClass("active")
        $(".becomeBlack").addClass("is-open")
    })
    //小窗口用户中心弹出，底色变暗
 $(".becomeBlack").click(function(){
    $('.box1').removeClass("active")
    $(".becomeBlack").removeClass("is-open")
})
$("aside>.nav").click(function(){
    $('.box1').removeClass("active")
    $(".becomeBlack").removeClass("is-open")
})
}

//页面加载完成时，先判断一次窗口大小,进行事件绑定
becomeSmall()
bindEvent()


//----------

})();
