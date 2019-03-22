(function(){
    $('.vipLink>.vipLinkHref').one('click',getMagnet)
    // $('#BTList>.downloadList>p.vipLink>.vipLinkHref').one('click',getMagnet)
    function getMagnet(e){
        let _temp = e.target
        $.ajax({
            type: "post",
            // type: "get",
            url: "/tools/loadingmagnet/?magnet=",
            headers:{'X-CSRFToken': getCookie('csrftoken')},
            data: {magnetURL:$('.generalLlink>a').attr('href')},
            cache: false,    //缓存
            beforeSend:function(){
                $(_temp).text('加载中，大约需要20秒...')
                $(e.target).off('click',getMagnet)
            },
            success: function(data){
                // $(_temp).text(data.magnetInfo)
                let xxx = `<a href="${data.magnetURL}">已获取，点击下载</a>`
                $(_temp).text('')
                $(_temp).append(xxx)
                // _temp.setAttribute('data-clipboard-text',data.magnetInfo)
                // var clipboard = new ClipboardJS('.vipLinkHref', {
                //     text: function(trigger) {
                //         return trigger.getAttribute('data-clipboard-text');
                //     }
                // });
            //     clipboard.on('success', function(e) {
            //         alert('复制成功')
            //     });
            //     clipboard.on('error', function(e) {
            //         alert('复制失败，请手动复制')
            //     });
            },
            error:function(){
               $(_temp).text('加载失败点击重试')
               $(e.target).one('click',getMagnet)
            //    let test=`<input class="test" value="yyext in this element.">`
            // $('#body-container').append(test)
            //    $(_temp).on('click',()=>{
            //     document.getElementsByClassName("test")[0].select()
            //     document.execCommand("Copy")
            //     console.log('xxx')
            //    })
            },
            complete:function(){

            }
        })
    }

    function getCookie(name) {
    var cookieValue = null;
     if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
        }
    }
    }
    return cookieValue;
}

    function changeIco(){
        $('.fileList>ul>li').each(function(index,e){
            let xLink = e.getAttribute('alt')
            let temp
            switch(xLink){
                case 'mp4':
                    temp = 'shipinmp'
                    break
                case 'mkv':
                    temp = 'shipinmkv'
                    break
                case 'avi':
                    temp = 'shipinavi'
                    break
                case 'flv':
                    temp = 'shipinflv'
                    break
                case 'rmvb':
                    temp = 'shipinrmvb'
                    break
                case 'jpg':
                    temp = 'tupianjpeg'
                    break
                case 'bmp':
                    temp = 'tupianbmp'
                    break
                case 'png':
                    temp = 'tupianpng'
                    break
                case 'jpeg':
                    temp = 'tupianjpeg'
                    break
                case 'mp3':
                    temp = 'yinpinmp'
                    break
                case 'aac':
                    temp = 'yinpinaac'
                    break
                case 'flac':
                    temp = 'flac'
                    break
                    default:
                    temp = 'weizhi'
                    break

            }
            let tempSvg = `<svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-geshi_${temp}"></use>
        </svg>`
            $(e).prepend(tempSvg)
        })
    }
    changeIco()
})()