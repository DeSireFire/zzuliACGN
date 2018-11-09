let heimingdanguanli = Vue.component('black-list',{
    template:`
    <div>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <h2 @click="cons"><i class="fa fa-user-times fa-2x"></i> 黑名单管理</h2>
        </div>
    </div>
    <div class="line-border"></div>
    <main id="blackList-content" class="blackList-content">
        <div class="blackList-item" v-for="(bList,key) in bLists.data.records">
            <div class="blackList-item-lt">
                <div>
                    <img :src="bList.head">
                </div>
                <div class="blackList-item-lt-message text-left">
                    <div>
                        <p>{{bList.userName}}</p>
                    </div>
                    <div>
                        <p>添加时间：{{bList.time}}</p>
                    </div>
                </div>
            </div>
            <div class="blackList-item-rt">
                <button :value="bList.uid" class="btn btn-default" @click="removebl">移除</button>
            </div>
        </div>
    </main>
    <nav id="bl-nav"aria-label="Page navigation">
        <ul class="pagination">
            <li :class="this.bLists.pre.state">
                <span @click="topage" :data-page="this.bLists.pre.page" aria-hidden="true">&laquo;</span>
            </li>

            <li @click="topage" :class="page.current" v-for="(page) in bLists.pages"><span :data-page="page.page">{{page.page}}</span></li>
            
            <li :class="this.bLists.next.state ">
                <span @click="topage" :data-page="this.bLists.next.page" aria-hidden="true">&raquo;</span>
            </li>
            <li>
                <input type="number" placeholder="page" v-model.number="bLists.data.currentcopy" class="topage" @keyup.enter="topage(bLists.data.currentcopy)"> 
            </li>
        </ul>
        
    </nav>
</div>
    `,
    data:function(){
        return {bLists:{
            data:{
                currentcopy:null,
                current:1,
                pages:5,
                size:10,
                total:50,
                records:[
                    // {uid:1,head:"../../img/background/手机.png",userName:"userName",time:"2018-06-30 02:44:21"},
                ]
            },
            next:{
                page:2,
                state:''
            },
            pre:{
                page:1,
                state:''
            },
            pages:[
                {current:"active",page:1},
                {current:"",page:2},
                {current:"",page:3},
                {current:"",page:4},
                {current:"",page:5},
            ],
        }
    }
    },
    methods:{
        getCookie:function(name) {
            var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
            }
            return cookieValue;
        },
        cons:function(){
            console.log(this.bLists)
        },
        removebl:function(e){//点击移除时
            let user = document.cookie //读cookie验证用户
            //发送用户cookie，要移除的人和当前的页数
            let temp = {user:user,removeBl:e.target.value,page:this.bLists.data.current}
            temp= JSON.stringify(temp)
            $.ajax({
                type: "post",
                url: "/user/removeBlacklist/",
                headers:{'X-CSRFToken': this.getCookie('csrftoken')},
                data: temp, 
                processData: false,    //false
                cache: false,    //缓存
                beforeSend:function(){
                    _temp.$emit('loading-open')
                },
                success: function(data){//重新接收数据
                    console.log('成功移除')
                    ajaxSuccess(data)      
                },
                fail:function(){
                    console.log('error')
                },
                complete:function(){
                    _temp.$emit('loading-close')
                }
            })
        },
        topage:function(e){//点击页面标签时
            let user = document.cookie
            let temp={}
            console.log(typeof(e))
            if(typeof(e) === "number"){//创建时和直接输入页码时传入数字
                temp ={page:e,user:user}
            }else{
                temp ={page:e.target.dataset.page,user:user}
            }
            console.log(temp)
            let _temp = this
            temp = JSON.stringify(temp)
            $.ajax({
                type: "post",
                url: "/user/loadingBlacklist/",
                headers:{'X-CSRFToken': this.getCookie('csrftoken')},
                data: temp, 
                processData: false,    //false
                cache: false,    //缓存
                beforeSend:function(){//用来测试列表是否会被更改，上线时移到success中
                    // _temp.ajaxSuccess(
                    //     '{"code":200,"message":null,' +
                    //     '"data":{"total":18,"size":10,' +
                    //     '"pages":10,' +
                    //     '"current":2,' +
                    //     '"records":[{"uid":100,"head":"/static/ZA_User/img/HeaderImg/head.jpg","userName":"userName","time":"2018-06-30 02:44:21"},{"uid":2,"head":"/static/ZA_User/img/HeaderImg/head.jpg","userName":"userName","time":"2018-06-30 02:44:21"},{"uid":3,"head":"/static/ZA_User/img/HeaderImg/head.jpg","userName":"userName","time":"2018-06-30 02:44:21"},{"uid":4,"head":"/static/ZA_User/img/HeaderImg/head.jpg","userName":"userName","time":"2019-06-30 02:44:21"},{"uid":5,"head":"/static/ZA_User/img/HeaderImg/head.jpg","userName":"userName","time":"2018-06-30 02:44:21"}]}}'
                    // )
                }.bind(this),
                success: function(data){
                    console.log(data)
                    _temp.ajaxSuccess(data)
                },
                fail:function(){
                    console.log('error')
                },
                complete:function(){

                }
            })
        },
        ajaxSuccess:function(xxx){
            let temp = xxx
            this.bLists = Object.assign({}, this.bLists, temp)
            this.bLists.pages = []
            // this.bLists.data.currentcopy = this.bLists.data.current
            console.log(this.bLists)
            function makeLi(a,b){
                if(a===b){
                    return {page:a,current:'active'}
                }
                return {page:a,current:''}
            }
            this.bLists.pre={}
            this.bLists.next={}
            //生成前后翻页的标签属性
            if(this.bLists.data.current===1){
                this.bLists.pre.state = "disabled"
                this.bLists.next.page = this.bLists.data.current+1
            }else if(this.bLists.data.current===this.bLists.data.pages){
                this.bLists.next.state = "disabled"
                this.bLists.pre.page = this.bLists.data.current-1
            }else{
                this.bLists.pre.page = this.bLists.data.current-1
                this.bLists.next.page = this.bLists.data.current+1
            }
            //生成分页标签的属性
            if(this.bLists.data.pages<5){
                for(let i=1;i<=this.bLists.data.pages;i++){
                    this.bLists.pages.push(makeLi(i,this.bLists.data.current))
                }
            }else{
                if(this.bLists.data.pages-this.bLists.data.current>=2&&this.bLists.data.current>=3){
                    for(let i=this.bLists.data.current-2;i<=this.bLists.data.current+2;i++){
                        this.bLists.pages.push(makeLi(i,this.bLists.data.current))
                    }
                }else if(this.bLists.data.current<=2){
                    for(let i=1;i<=5;i++){
                        this.bLists.pages.push(makeLi(i,this.bLists.data.current))
                    }
                }else{
                    for(let i=this.bLists.data.pages-4;i<=this.bLists.data.pages;i++){
                        this.bLists.pages.push(makeLi(i,this.bLists.data.current))
                    }
                }
            }
            console.log(this.bLists)
            return this.bList
        }
    },
    created:function(){//组件创建完成后进行一次到第一面的函数
        let temp = 1
        this.topage(temp)
    }
})
