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
    </div>
    `,
    data:function(){
        return {
            page:this.pagedata.index,
        }
    },
    created:function(){
        console.log('xxx')
        console.log(this.ifcreated.index)
        if(this.ifcreated.index === 0){
            this.$emit('loadpage',{page:'index',part:'indeximg'})
            this.$emit('loadpage',{page:'index',part:'article',num:1})
        }
    }
})