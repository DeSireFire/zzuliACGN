(function(){
    function xxx(){
        if(!localStorage.getItem('userKnow')){
            $('.popwindow').css({display:'flex'})
        }
    }
    $('.btn-agree').on('click',()=>{
    let temp = []
    $("input[name='windowpopname']").each(function(index,e){
        temp.push($(e).prop('checked'))
    })
    if(temp[0]){
        localStorage.setItem('userKnow', 'true');
        let cat = localStorage.getItem('userKnow');
        console.log(cat)
    }
    if(temp[1]){
        $('.popwindow').css({display:'none'})
    }else{
        alert('请同意！')
    }
    
    })
    function yyy(){
        let data = {
            exit:[0,1,1,1,0,0,1,0,0],
            data:[
                {type:'全部',num:0},
                {type:'动画',num:1,arr:[{name:'季度全集',num:11}]},
                {type:'漫画',num:2,arr:[{name:'港台漫画',num:21},{name:'日本漫画',num:22}]},
                {type:'音乐',num:3,arr:[{name:'动漫音乐',num:31},{name:'同人音乐',num:32},{name:'流行音乐',num:33}]},
                {type:'日剧',num:4},
                {type:'raw',num:5},
                {type:'游戏',num:6,arr:[{name:'电脑游戏',num:61},{name:'电视游戏',num:62},{name:'掌机游戏',num:63},{name:'网络游戏',num:64},{name:'游戏周边',num:65}]},
                {type:'特摄',num:7},
                {type:'其他',num:8},        
            ],
        }
        let temp=``
        data.data.forEach(function(e,index){
            if(e.arr){
                temp=temp + `<li>
                <a href="?category=${e.num}">${e.type}</a>
                <ul class="liList">`
                e.arr.forEach(function(e,index){
                    temp=temp+`<li><a href="?category=${e.num}">${e.name}</a></li>`
                })
                temp = temp + `
                </ul>
                        </li>
                `
            }else{
                temp=temp+`<li>
                <a href="?category=${e.num}">${e.type}</a>
            </li>`
            }
        })
        console.log(temp)
        $('.topbar>ul').append(temp)
        }
    yyy()
    xxx()
})()