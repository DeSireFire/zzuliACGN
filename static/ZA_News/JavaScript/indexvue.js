let index = Vue.component('index',{
    props:['pagedata','ifcreated'],
    template:`
    <div>
        <div class="left-side">
            <div>
                <div class="block" id="top-carousel">
                    <el-carousel height="210px" arrow="never">
                        <el-carousel-item v-for="(item,index) in page.indeximg" :key="index">
                            <a :href="item.href"><img :src="item.img" alt="..."></a>
                            <h3>{{ item.abstract }}</h3>
                        </el-carousel-item>
                    </el-carousel>
                </div>
            </div>
            
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
        <!--<aside class="right-side">-->
            <!--<div>-->
            <!--<h4>热点</h4>-->
            <!--<hr>-->
            <!--<ul>-->
                <!--<li v-for="(item,index) in hot">-->
                    <!--<a :href="item.href">{{item.title}}</a><span>{{item.date}}</span>-->
                <!--</li>-->
            <!--</ul>-->
            <!--</div>-->
        <!--</aside>-->
    </div>
    `,
    data:function(){
        return {
            page:this.pagedata.index,
            indeximg:[{img:'../Images/66474729_p0.jpg',href:'#',abstract:'ccc',},
                {img:'../Images/8c007b5cgy1fqwefu5tkrj20xc0nkqv5.jpg',href:'#',abstract:'xxx'},
                {img:'../Images/8c007b5cly1fkayrbqu9sj216b0ovke1.jpg',href:'#',abstract:"zzz"}
                ],
            article:[],
            hot:[{href:'#',title:'东京动画奖2019”年度最佳动画作品奖与个人奖结果发表',date:'2019-2-21'}]
        }
    },
    created:function(){
        console.log('xxx')
        console.log(this.ifcreated.index)
        if(this.ifcreated.index === 0){
            this.$emit('loadpage',{page:'index',part:'indeximg'})
            this.$emit('loadpage',{page:'index',part:'article'})
        }
    }
})