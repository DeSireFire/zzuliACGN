const hot = Vue.component('hot',{
    props:['pagedata','ifcreated'],
    template:`                    
                    <aside class="right-side">
                        <div>
                            <h4>热点</h4>
                            <hr>
                            <ul>
                                <li v-for="(item,index) in page.hot">
                                <router-link :to="item.href">{{item.title}}</router-link><span>{{item.date}}</span>
                                </li>
                            </ul>
                        </div>
                    </aside>
`,
    data:function(){
        return{
            page:this.pagedata.hot,
        }
    },
    created:function(){
        if(this.ifcreated.hot === 0){
            //修改
            this.$emit('loadpage',{page:'hot',part:'hot'})
        }
    }
})