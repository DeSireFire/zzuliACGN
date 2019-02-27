const index = Vue.component('index', {
    props:['pagestate'],
    template: `
            <div>
                <aside id="anime-aside">
                <ul>
                    <li><a href="#">时间表</a></li>
                    <li><a href="#">新番更新</a></li>
                    <li><a href="#">历年动画</a></li>
                    <li><a href="#">剧场ova</a></li>
                </ul>
            </aside>
                <section class="timetable">
                <!-- Nav tabs -->
                <ul id="timetablelist" class="nav nav-tabs" role="tablist">
                    <li v-for="(item,index) in week" role="presentation" @click="tlclick(index)"><a :href=item.en :aria-controls=item.en role="tab" data-toggle="tab">{{item.zh}}</a>
                    </li>
                    <!--<li role="presentation"><a href="#Monday" aria-controls="Monday" role="tab" data-toggle="tab">周一</a>-->
                    <!--</li>-->
                    <!--<li role="presentation"><a href="#Tuesday" aria-controls="Tuesday" role="tab"-->
                                               <!--data-toggle="tab">周二</a></li>-->
                    <!--<li role="presentation"><a href="#Wednesday" aria-controls="Wednesday" role="tab" data-toggle="tab">周三</a>-->
                    <!--</li>-->
                    <!--<li role="presentation"><a href="#Thursday" aria-controls="Thursday" role="tab"-->
                                               <!--data-toggle="tab">周四</a></li>-->
                    <!--<li role="presentation"><a href="#Friday" aria-controls="Friday" role="tab" data-toggle="tab">周五</a>-->
                    <!--</li>-->
                    <!--<li role="presentation"><a href="#Saturday" aria-controls="Saturday" role="tab"-->
                                               <!--data-toggle="tab">周六</a></li>-->
                    <!--<li role="presentation"><a href="#Sunday" aria-controls="Sunday" role="tab" data-toggle="tab">周日</a>-->
                    <!--</li>-->
                </ul>

                <!-- Tab panes -->

                <div class="tab-content">
                    <div role="tabpanel" :class="item.class" :id="item.name" v-for="item in timeline.datas">
                        <ul class="time-ul">
                          <li v-for="datax in item.datas">
                                <img :src=datax.img>
                                <div>
                                    <span class="time-title">{{datax.title}}</span>
                                    <span class="time-update">{{datax.num}}</span>
                                </div>
                            </li>
                        </ul>
                    </div>



                                     <!--<div role="tabpanel" class="tab-pane active" id="Monday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[0].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Tuesday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[1].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Wednesday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[2].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Thursday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[3].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Friday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[4].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Saturday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[5].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <!--<div role="tabpanel" class="tab-pane" id="Sunday">-->
                                                <!--<ul class="time-ul">-->
                            <!--<li v-for="datax in timeline.datas[6].datas">-->
                                <!--<img :src=datax.img>-->
                                <!--<div>-->
                                    <!--<span class="time-title">{{datax.title}}</span>-->
                                    <!--<span class="time-update">{{datax.num}}</span>-->
                                <!--</div>-->
                            <!--</li>-->
                        <!--</ul>-->
                    <!--</div>-->
                </div>
                </section>
<section class="anime-con-con">
<div class="text-left"><h4><span class="icon-rmxf"></span>日漫新番</h4></div>
<div class="anime-flex">
    <div class="anime-container" v-for="item in maindata.newanimeindex">
        <div class="anime-img-con" ><a :href="item.href"><img v-lazy='item.img' class="anime-img" src="../Images/zhanwei.png"></a></div>
        <div class="anime-title-con">
            <h4>{{item.title}}</h4>
            <span>更新至{{item.num}}话</span>
        </div>
    </div>
    </div>
</section>
<section class="anime-con-con">
<div class="text-left"><h4><span class="icon-rmxf"></span>历年动画</h4></div>
<div class="anime-flex">
    <div class="anime-container" v-for="item in maindata.pastanimeindex">
        <div class="anime-img-con" ><a :href="item.href"><img v-lazy='item.img' class="anime-img" src="../Images/zhanwei.png"></a></div>
        <div class="anime-title-con">
            <h4>{{item.title}}</h4>
            <span>更新至{{item.num}}话</span>
        </div>
    </div>
    </div>
</section>
            </div>
    `,
    data:function() {
        return {
            timeline: {
                datas: [
                    {
                        datas: [],
                        name: "Monday",
                        class:'tab-pane'
                    },
                    {
                        datas: [],
                        name: "Tuesday",
                        class:'tab-pane'
                    },
                    {
                        datas: [],
                        name: "Wednesday",
                        class:'tab-pane'
                    },
                    {
                        datas: [],
                        name: "Thursday",
                        class:'tab-pane'
                    }, {
                        datas: [],
                        name: "Friday",
                        class:'tab-pane'
                    },
                    {
                        datas: [],
                        name: "Saturday",
                        class:'tab-pane'
                    },
                    {
                        datas: [],
                        name: "Sunday",
                        class:'tab-pane'
                    },
                ]
            },
            week: [{en:"Monday",zh:'周一'}, {en:"Tuesday",zh:'周二'}, {en:"Wednesday",zh:'周三'}, {en:"Thursday",zh:'周四'}, {en:"Friday",zh:'周五'}, {en:"Sunday",zh:'周六'}, {en:"Saturday",zh:'周日'}],
            tlifclick:[0,0,0,0,0,0,0],
            testdata: {
                tl: [{title: 'revisions', num: '12', img: 'Images/time.jpg'}, {
                    title: 'revisions',
                    num: '12',
                    img: 'Images/time.jpg'
                }, {title: 'revisions', num: '12', img: 'Images/time.jpg'}, {
                    title: 'revisions',
                    num: '12',
                    img: 'Images/time.jpg'
                }, {title: 'revisions', num: '12', img: 'Images/time.jpg'}, {
                    title: 'revisions',
                    num: '12',
                    img: 'Images/time.jpg'
                }, {title: 'revisions', num: '12', img: 'Images/time.jpg'}, {
                    title: 'revisions',
                    num: '12',
                    img: 'Images/time.jpg'
                }, {title: 'revisions', num: '12', img: 'Images/time.jpg'}],
            },
            maindata:{
                newanimeindex:[],
                pastanimeindex:[],
                ovaindex:[],
            }
        }

    },
    methods:{
        tlajax:function(num){
            let date = num
            let _temp = this
            $.ajax({
                type: "get",
                url: "/timetable",
                data: date,
                processData: false,    //false
                cache: false,    //缓存
                beforeSend:function(){

                },
                success: function(data){
                    // _temp.datas[num].datas = data
                },
                error:function(){
                    console.log(_temp,date)
                    _temp.ajaxerror(num)
                    //test

                    $(`#timetablelist li:eq(${{num}}) a`).tab('show')
                },
                complete:function(){

                }
            })
        },
        tlclick:function(index){
            if(this.tlifclick[index]===0){
                this.tlajax(index)
            }
            for(let i=0;i<=6;i++){
                this.timeline.datas[i].class = "tab-pane"
            }
            this.timeline.datas[index].class = "tab-pane active"
        },
        ajaxerror:function(num){
            this.timeline.datas[num].datas = this.testdata.tl
            console.log(num)
            console.log(this.timeline.datas[num].datas)
        },
        rmxfajax:function(){
            $.ajax({
                type: "get",
                url: "/timetable",
                data: date,
                processData: false,    //false
                cache: false,    //缓存
                beforeSend:function(){

                },
                success: function(data){
                    // _temp.datas[num].datas = data
                },
                error:function(){
                    console.log(_temp,date)
                    _temp.ajaxerror(num)
                    //test

                    $(`#timetablelist li:eq(${{num}}) a`).tab('show')
                },
                complete:function(){

                }
            })
        },
        ajaxstart:function (){
            //测试用
            let data = {type:'index'}
            let _temp = this
            $.ajax({
                type: "get",
                url: "/newanime",
                data: data,
                success: function(data){
                    pagestate_temp.mainajaxsucess(xxx)
                },
                error:function(){

                },
                complete:function(){
                    let xxx = {
                        newanimeindex:[{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'}],
                        pastanimeindex:[{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},],
                        ovaindex:[{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},{title:'辉夜姬想让人告白 天才们的恋爱头脑战',num:'1',img:'../Images/201812311546250656.png',href:'#'},{title:'佐贺偶像是传奇',num:'12',img:'../Images/201810121539281100.jpg',href:'#'},]

                    }
                    _temp.mainajaxsucess(xxx)
                }
            })
        },
        mainajaxsucess:function(data){
            let _temp = this
            console.log(data)
            Object.keys(this.maindata).forEach(function(currentValue){
                _temp.maindata[currentValue] = data[currentValue]
                console.log(data[currentValue])
            })
            Vue.use(VueLazyload)
            this.$emit('indexopen',_temp.maindata)
        }
    },
    created:function(){
        let date = new Date().getDay()
        console.log($(`.tab-content div:eq(${date-1})`))
        // $(`.tab-content div:eq(${date-1})`).addClass('active')
        this.timeline.datas[date-1].class = "tab-pane active"
        this.tlclick(date-1)

    },
    mounted:function(){
        let date = new Date().getDay()
        $(`#timetablelist li:eq(${date-1}) a`).tab('show')

            this.maindata =  this.pagestate.index.data
            if(this.pagestate.index.num === 0) {
                this.ajaxstart()
                console.log('xxx')
            }
            console.log(this.animedata)

    }

})