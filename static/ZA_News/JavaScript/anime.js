//修改
let anime = Vue.component('anime',{
    props:['pagedata','ifcreated'],
    template:`
    <div>
        <div class="left-side">
            <div class="partition-name"><h3>推荐文章</h3></div>
            <div class="article-content">
                <section class="article" v-for="(item,index) in page.article">
                <a :href="item.href">
                <div class="article-left">
                    <h4 class="article-tittle">xxx</h4>
                    <p>{{item.abstract}}</p>
                    <div class="article-inf"><span>{{item.source}}</span><span>{{item.type}}</span><span>{{item.date}}</span></div>
                </div>
                <div class="article-right"><img :src="item.img" width="120" height="90"></div>
                </a>
                </section>               
            </div>
        </div>
    </div>
    `,
    data:function(){
        return {
            //修改
            page:this.pagedata.anime,
            indeximg:[{img:'./Images233/66474729_p0.jpg',href:'#',abstract:'ccc',},
                {img:'./Images/8c007b5cgy1fqwefu5tkrj20xc0nkqv5.jpg',href:'#',abstract:'xxx'},
                {img:'./Images/8c007b5cly1fkayrbqu9sj216b0ovke1.jpg',href:'#',abstract:"zzz"}
            ],
            article:[],
            hot:[{href:'#',title:'东京动画奖2019”年度最佳动画作品奖与个人奖结果发表',date:'2019-2-21'}]
        }
    },
    created:function(){
        //修改a
        if(this.ifcreated.anime === 0){
            //修改
            this.$emit('loadpage',{page:'anime',part:'article',num:1})
            
        }
    }
})