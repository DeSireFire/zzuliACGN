let zhongxinshouye = Vue.component('user-center-home-page',{
    props:['userdata'],
    template:`
    <div class="" >
    <div class="row">
        <div class="col-md-2">
            <div class="user-head center-block">
                <img :src="userdata.userheadimg" class="img-responsive img-circle"/>
            </div>
        </div>
        <div class="col-md-10 text-left">
            <div class="user-head-left">
                <span class="user-top-name">{{userdata.username}}</span>
                <span class="user-top-tags user-top-tag1-color1">校园认证</span>
                <span class="user-top-tags user-top-tag1-color2">正式会员</span>
                <div class="user-motto">{{userdata.usermotto}}</div>
                <div class="user-level row">
                    <span class="col-sm-2 user-level-span">LV0</span>
                    <div class="col-sm-10 progress user-level-progress">
                        <div class="progress-bar progress-bar-striped active" style="width:6%"></div>
                    </div>
                </div>
                <router-link to="/wodexinxi" class="btn btn-user"> 修改资料</router-link>
                <a class="btn btn-user" href="#" role="button">个人空间</a>
            </div>
        </div>
    </div>
    <div class="line-border"></div>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <span>账号状态</span>
            <router-link class="btn btn-user btn-xs" to="/zhanghaoanquan"><i class="fa fa-fw fa-user-secret"></i> 更多设置 </router-link>
        </div>
        <div class="col-sm-6 col-md-6">
        <div class="user-msg-th">
            <img class="user-msg-th-icon" src="Images/邮箱.png"/>
            <div class="user-msg-th-cont">
                <b class="h-safe-title">我的邮箱</b>
                <p class="h-safe-desc">绑定邮箱即可邮箱登录</p>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=userdata.emailif>已认证</a>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=!userdata.emailif>未认证</a>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=userdata.emailif>更改邮箱 </router-link>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=!userdata.emailif>绑定邮箱 </router-link>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-6">
        <div class="user-msg-th">
            <img class="user-msg-th-icon" src="Images/手机.png"/>
            <div class="user-msg-th-cont">
                <b class="h-safe-title">我的手机</b>
                <p class="h-safe-desc">绑定手机即可手机登录</p>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=userdata.phoneif>已认证</a>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=!userdata.phoneif>未认证</a>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=userdata.phoneif>更改手机 </router-link>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=!userdata.phoneif>绑定手机 </router-link>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-6">
        <div class="user-msg-th">
            <img class="user-msg-th-icon" src="Images/写报告.png"/>
            <div class="user-msg-th-cont">
                <b class="h-safe-title">密保问题</b>
                <p class="h-safe-desc">设置密保，账号更安全</p>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=userdata.questionif>已设置</a>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=!userdata.questionif>未设置</a>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=userdata.questionif>更改密保 </router-link>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=!userdata.questionif>设置手机 </router-link>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-6">
        <div class="user-msg-th">
            <img class="user-msg-th-icon" src="Images/代办事项.png"/>
            <div class="user-msg-th-cont">
                <b class="h-safe-title">实名认证</b>
                <p class="h-safe-desc">学号认证、证件认证</p>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=userdata.certificationif>已认证</a>
                <a class="btn btn-user btn-xs disabled" role="button" v-if=!userdata.certificationif>未认证</a>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=userdata.certificationif>查看认证 </router-link>
                <router-link to="/zhanghaoanquan" class="btn btn-user btn-xs" v-if=!userdata.certificationif>进行认证 </router-link>
            </div>
        </div>
    </div>
        <!--<div class="col-md-6" style="background-color: #00FFCC">-->
        <!---->
        <!--</div>-->
        <!--<div class="col-md-6" style="background-color: pink"></div>-->
    </div>
    <div class="line-border"></div>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <span>成就勋章（待建预留）</span>
            <router-link class="btn btn-user btn-xs" to="/wodexunzhang">我的勋章 </router-link>
        </div>
        <div class="col-sm-6 col-md-6">
            <div class="user-msg-th">
                <img class="user-msg-th-icon" src="/static/ZA_User/img/background/邮箱.png"/>
                <div class="user-msg-th-cont">
                    <b class="h-safe-title">我的邮箱</b>
                    <p class="h-safe-desc">绑定邮箱即可邮箱登录</p>
                    <span class="btn btn-user btn-xs">已绑定</span>
                    <a href="#" class="btn btn-user btn-xs">更改邮箱</a>
                </div>
            </div>
        </div>
    </div>
</div>
    `,
    data:function(){
        return {
            userbasedata:{
            }
        }
    },
})