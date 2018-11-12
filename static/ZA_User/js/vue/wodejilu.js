let denglujilu = Vue.component('denglujilu',{
    template:`
    <div>
    <div class="text-center">
    <table id="denglujilu" class="table table-bordered table-condensed">
        <thead>
            <tr>
                <th>时间</th>
                <th>IP</th>
                <th>地理位置</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(userdata,key) in userdatas">
                <td>{{userdata.date}}</td>
                <td>{{userdata.ip}}</td>
                <td>{{userdata.place}}</td>
            </tr>
        </tbody>
    </table>
    </div>
</div>
    `,
    data:function(){
        return {
            userdatas:[{
                date:'2018-11-11 21:19:56',
                ip:'192.168.***.**',
                place:'致远星'
            },{
                date:'2018-11-10 21:19:56',
                ip:'192.168.***.**',
                place:'致远星'
            },{
                date:'2018-11-09 21:19:56',
                ip:'192.168.***.**',
                place:'致远星'
            }]
        }
    },
    methods:{
        ajaxSuccess:function(data){
            //let temp = JSON.parse(data)
            this.userdatas = Object.assign({}, this.userdatas , data)
        }
    },
    created:function(){
        let _temp = this
        let user = document.cookie
        
        $.ajax({
            type: "post",
            url: "/denglujilu",
            data: user, 
            processData: false,    //false
            cache: false,    //缓存
            beforeSend:function(){
                _temp.$emit('loading-open')
            },
            success: function(data){//重新接收数据
                _temp.ajaxSuccess(data)      
            },
            error:function(){
                console.log('error')
            },
            complete:function(){
                _temp.$emit('loading-close')
            }
        })
    }
})


let pinglunjilu = Vue.component('pinglunjilu',{
    template:`
    <div>
    <p>建设中</p>
</div>
    `,
    data:function(){
        return {
            datas:{}
        }
    },
    methods:{

    },
})



let wodejilu = Vue.component('my-record',{
    template:`
    <div>
    <div class="row user-msg text-left">
        <div class="user-msg-title"><h2><i class="fa fa-location-arrow fa-2x"></i> 我的记录</h2></div>
        <div class="line-border"></div>
    </div>
    <div class="">
    <ul class="nav nav-tabs">
    <li><router-link to="/wodejilu/denglujilu">登录记录 </router-link></li>
    <li><router-link to="/wodejilu/pinglunjilu">评论记录 </router-link></li>
    </ul>
    <router-view @loading-open="$emit('loading-open')" @loading-close="$emit('loading-close')"></router-view>
</div>
</div>
    `,
    data:function(){
        return {
            datas:{}
        }
    },
    methods:{

    },
})