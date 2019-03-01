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