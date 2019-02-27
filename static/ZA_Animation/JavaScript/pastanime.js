const pastanime = Vue.component('pastanime', {
    props:['pagestate'],
    template: `
<div id="pastanime-container">
<nav>
<ul>

<li>字母</li>

</ul>
</nav>
<section class="anime-con-con text-left">
<div class="anime-flex">
    <div class="anime-container" v-for="item in animedata.data">
        <div class="anime-img-con" ><a :href="item.href"><img class="anime-img" :src=item.img></a></div>
        <div class="anime-title-con">
            <h4>{{item.title}}</h4>
            <span>更新至{{item.num}}话</span>
        </div>
    </div>
</div>
</section>
</div>
    `,
    data:function(){
        return {
            animedata:{}
        }
    },
    mounted:function(){
        this.animedata =  this.pagestate.pastanime.data
        if(this.pagestate.pastanime.num === 0) {
            this.ajaxstart()
        }
        console.log(this.animedata)
    },
    methods:{
        ajaxstart:function (){
            //测试用
            this.$emit('pastanimeopen')
            let data = {type:'pastanime',page:'1'}
            let _temp = this
            $.ajax({
                type: "get",
                url: "/pastanime",
                data: data,
                cache: false,    //缓存
                beforeSend:function(){

                },
                success: function(data){
                    _temp.ajaxsuccess(data)
                },
                error:function(){

                },
                complete:function(){
                    let xxx = {data:[{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                            {title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},
                        ]}
                    _temp.ajaxsuccess(xxx)
                }
            })
        },
        ajaxsuccess:function(data){
            console.log('123')
            this.animedata=data
            console.log(data)
            this.$emit('pastanimeopen',this.animedata)
        }
    }
})