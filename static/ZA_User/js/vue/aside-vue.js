Vue.component('app-aside',{
    template:`
    <aside class="col-sm-2 col-md-2 box1">
    <ul class="nav nav-pills nav-stacked navbar-inverse" @click="$emit('click-aside')">
        <li><span>个人中心</span></li>
        <li>
        <router-link to="/zhongxinshouye"><i class="fa fa-fw fa-home"></i> 中心首页 </router-link>
        </li>
        <li>
        <router-link to="/wodexinxi"><i class="fa fa-fw fa-user"></i> 我的信息 </router-link>
        </li>
        <li>
        <router-link to="/wodetouxiang"><i class="fa fa-fw fa-camera-retro"></i> 我的头像 </router-link>
        </li>
        <li>
        <router-link to="/wodexunzhang"><i class="fa fa-fw fa-flag"></i> 我的勋章 </router-link>
        </li>
        <li>
        <router-link to="/zhanghaoanquan"><i class="fa fa-fw fa-user-secret"></i> 账号安全 </router-link>
        </li>
        <li>
        <router-link to="/heimingdanguanli"><i class="fa fa-fw fa-user-times"></i> 黑名单管理 </router-link>
        </li>
        <li>
        <router-link to="/wodejilu"><i class="fa fa-fw fa-location-arrow"></i> 我的记录 </router-link>
        </li>
        <li>
        <router-link to="/shimingrenzheng"><i class="fa fa-fw fa-id-card"></i> 实名认证 </router-link>
        </li>
        <li>
        <router-link to="/yaoqingzhuce"><i class="fa fa-fw fa-user-plus"></i> 邀请注册 </router-link>
        </li>
    </ul>
</aside>
    `
})