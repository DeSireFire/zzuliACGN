let zhanghaoanquan = Vue.component('account-safe',{
    props:['userdata'],
    template:`<div>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <h2><i class="fa fa-user-secret fa-2x"></i>账号安全</h2>
        </div>
    </div>
    <div class="line-border"></div>
    <main>
        <ul>
            <li class="safe-list-li" v-for="(userdatax,index) in this.userdatatemp">
                <div class="container">
                    <div class="col-xs-4 text-left"><i :class="userdatax.classname"></i>{{userdatax.lt}}</div>
                    <div class="col-xs-4">{{userdatax.value}}</div> 
                    <div class="col-xs-4">{{userdatax.rt}}</div> 
                </div>
            </li>
        </ul>
    </main>
</div>

    `,
    data:function(){
        return {
            userdatatemp:[{//邮箱
                lt:'绑定邮箱',value:' ',rt:' ',classname:'xxx'
            },{//电话
                lt:' ',value:' ',rt:' ',classname:' '
            },{//密码
                lt:' ',value:' ',rt:' ',classname:' '
            },{ //密保
                lt:' ',value:' ',rt:' ',classname:' '
            },{//实名
                lt:' ',value:' ',rt:' ',classname:''
            }]
            }
        },
        methods:{
            creatpage:function(){
                this.userdatatemp[0].lt="绑定邮箱"
                this.userdatatemp[1].lt="绑定手机"
                this.userdatatemp[2].lt="设置密码"
                this.userdatatemp[3].lt="密保问题"
                this.userdatatemp[4].lt="实名认证"

                if(this.userdata.emailif != 1){
                    this.userdatatemp[0].value="未绑定邮箱"
                    this.userdatatemp[0].rt="绑定邮箱"
                    this.userdatatemp[0].classname="fa fa-fw fa-exclamation-circle"
                }else{
                    this.userdatatemp[0].value=this.userdata.emailvalue
                    this.userdatatemp[0].rt="更换邮箱"
                    this.userdatatemp[0].classname="fa fa-fw fa-check-circle"
                }

                if(this.userdata.phoneif != 1){
                    this.userdatatemp[1].value="未绑定手机"
                    this.userdatatemp[1].rt="绑定手机"
                    this.userdatatemp[1].classname="fa fa-fw fa-exclamation-circle"
                }else{
                    this.userdatatemp[1].value=this.userdata.phonevalue
                    this.userdatatemp[1].rt="更换邮箱"
                    this.userdatatemp[1].classname="fa fa-fw fa-check-circle"
                }

                if(this.userdata.passwordif != 1){
                    this.userdatatemp[2].value="未设置密码"
                    this.userdatatemp[2].rt="设置密码"
                    this.userdatatemp[2].classname="fa fa-fw fa-exclamation-circle"
                }else{
                    this.userdatatemp[2].value="已设置密码"
                    this.userdatatemp[2].rt="更换密码"
                    this.userdatatemp[2].classname="fa fa-fw fa-check-circle"
                }

                if(this.userdata.questionif != 1){
                    this.userdatatemp[3].value="未设置密保问题"
                    this.userdatatemp[3].rt="设置"
                    this.userdatatemp[3].classname="fa fa-fw fa-exclamation-circle"
                }else{
                    this.userdatatemp[3].value="已设置密保问题"
                    this.userdatatemp[3].rt="更换"
                    this.userdatatemp[3].classname="fa fa-fw fa-check-circle"
                }

                if(this.userdata.certificationif != 1){
                    this.userdatatemp[4].value="未实名认证"
                    this.userdatatemp[4].rt="查看认证"
                    this.userdatatemp[4].classname="fa fa-fw fa-exclamation-circle"
                }else{
                    this.userdatatemp[4].value="已实名认证"
                    this.userdatatemp[4].rt="未认证"
                    this.userdatatemp[4].classname="fa fa-fw fa-check-circle"
                }
            }
        },
    mounted:function(){
        this.creatpage()
          },
    watch:{
        userdata:function(val){
            this.creatpage()
        }
    }

})