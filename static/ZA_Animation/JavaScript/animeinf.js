const animeinf = Vue.component('newanime', {
    props:['pagestate'],
    template: `
<div id="animeinf-container-con" class="text-left">
    <div id="animeinf-container">
        <div id="animeinf-img-container">
            <img :src="animedata.img">
        </div>
        <div id="animeinf-right" class="text-left">
            <div>
                <h2 style="color:white">{{animedata.title}}</h2>
            </div>
            <ul>
                <li>类型:<span v-for="item in animedata.type">
                    <span>{{item}}</span>
                    </span>
                </li>
                <li>时间:{{animedata.time}}</li>
                <li>声优:<span v-for="item in animedata.cv">
                    <span>{{item.name}}</span>
                    </span>
                </li>
                <li>动画制作:{{animedata.staff[0].name}}</li>
            </ul>
        </div>      
    </div>
    <div>
    <h4>简介</h4>
    <p>{{animedata.inf}}</p>
</div>
<section>
<div>

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">
    <li v-for="(item,index) in source" role="presentation" @click="tlclick(index)" :class="item.sourceclass">
    <span>{{item.name}}</span>
    </li>
  </ul>

  <!-- Tab panes -->
  <div class="animeinf-panes">
    <div v-for="item in source" :class="item.sourceclass" >
    <span v-for="(itema,index) in item.part"><a :href="itema">第{{(index+1)}}集</a></span>
    </div>
  </div>

</div>
</section>
</div>
    `,
    data:function(){
        return {
            animedata: {
                exist: '1',
                title: '灵能百分百 II',
                img: '../Images/201812311546251159.png',
                time: '2019-1',
                num: '4',
                type: ['科幻', '动画'],
                inf: '当有什么东西达到“100”的时候，就会爆发的少年·路人（龙套）。外表极其普通——不如说是不起眼。不擅长迎合气氛的他，实际上拥有着强力的超能力。盯上了这样的他的能力，而接连现身的伪灵能力者以及宗教团体、不良头头、谜之秘密组织……。在追求普通青春的龙套之处，平稳的日子究竟会不会到来？',
                cv: [{part: '影山茂夫（龙套）', name: '伊藤节生'},
                    {part: '灵幻新隆', name: '樱井孝宏'},
                    {part: '小酒窝', name: '大冢明夫'},
                    {part: '影山律', name: '入野自由'},
                    {part: '花泽辉气', name: '松冈祯丞'},
                    {part: '鬼瓦天牙', name: '细谷佳正'},
                    {part: '米里一', name: '藤村步'}
                ],
                staff: [{part: '动画制作', name: 'bones'}]

            },
            source: [
                {name: 'bilibili', part: ['#1', '#2', '#3'],sourceclass:'active'},
                {name: '271', part: ['#1', '#2', '#3','#4'],sourceclass:''}
            ],
        }
    },
    watch:{
        '$route' (to, from) {
            this.ajaxstart()
            console.log('xx')
        }
    },
    mounted:function(){
        this.ajaxstart()
        console.log('x')
    },
    methods:{
        ajaxstart:function (){
            //测试用
            let name = this.$route.params.name
            let data = {type:'anime',name:name}
            let _temp = this
            $.ajax({
                type: "get",
                url: "/anime",
                data: data,
                cache: false,    //缓存
                beforeSend:function(data){
                    _temp.ajaxsuccess(data)
                },
                success: function(data){

                },
                error:function(){
                    // alert('加载失败，请刷新页面重试')
                },
                complete:function(){
                    _temp.ajaxsuccess()
                }
            })
        },
        ajaxsuccess:function(data){
            // this.animedata=data.animedata
            // this.source = data.source
            this.creattabclass()
        },
        tlclick:function(index){
            for(let i=0;i<this.source.length;i++){
                this.source[i].sourceclass = ""
            }
            this.source[index].sourceclass= "active"
        },
        creattabclass:function(data){
            for(let i=0;i<this.source.length;i++){
                if(i===0){
                    this.source.sourceclass='active'
                }else{
                    this.source.sourceclass=''
                }
            }
        }
    }
})