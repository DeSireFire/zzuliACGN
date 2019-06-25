(function(){
Vue.component('hot-lists',{
    props:['temp1'],
template:`
<ul class="book-list">
<li v-for='item in temp'>
<a href="#" target="_blank" class="thumb">
    <span class="recom"></span>
    <img :alt="item.alt" class="cover" :src="item.src">
    <div class="label-count">
        <span class="fontstype">{{item.word}}</span>
    </div>
    <div class="book-info">
        <div class="book-info-a">
            <p><span class="d">{{item.title}}</span></p>
            <p><span class="book-info-title">类别：</span><span class="d">{{item.type}}</span></p>
        </div>
        <div class="book-info-b">
            <p><span class="book-info-title">状态：</span><span class="d">{{item.state}}</span></p>
            <p><span class="book-info-title">作者：</span><span class="d">{{item.author}}</span></p>
        </div>
    </div>
</a>
<a href="https://www.iqing.com/book/34961" target="_blank" class="title">
    <i class="icon icon-pay"></i>
    <h3 class="hasicon has-icon">{{item.title}}</h3>
</a>
</li>
</ul>
`,
data:function(){
    return {
        temp:this.temp1.list
    }
},
methods:{

},
created:function(){
    console.log(this.temp1)
}
})


let app = new Vue({
    el:'#hot-novel',
    data:{
        //要加东西的话
        temp1:{
         list:[{title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
         {title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
         {title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
         {title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
         {title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
         {title:'我的姐姐有中二病',href:'https://www.iqing.com/book/34961',alt:'轻小说：我的姐姐有中二病',src:'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg',type:'轻小说',word:'58.1万字',state:'连载中',author:'嘎嘎'},
        ]
        },

    },
    created:function(){
        //这里应该有一个获取数据赋值给temp1的函数

    }
})


}())