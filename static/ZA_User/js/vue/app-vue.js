
    const routes = [
        { path: '/', component: zhongxinshouye },
        { path: '/zhongxinshouye', component: zhongxinshouye },
        { path: '/wodexinxi', component: wodexinxi},
        { path: '/wodetouxiang', component: wodetouxiang },
        { path: '/wodexunzhang', component: wodexunzhang },
        { path: '/zhanghaoanquan', component: zhanghaoanquan },
        { path: '/heimingdanguanli', component: heimingdanguanli },
        { path: '/wodejilu', component: wodejilu },
        { path: '/shimingrenzheng', component: shimingrenzheng },
        { path: '/yaoqingzhuce', component: yaoqingzhuce }
      ]

      const router = new VueRouter({
        routes
      })

    let appVue = new Vue({
        el:'#tf-home',
        router,
        data:{
          ifblack:false,
          ifloading:true,
          userdata:{//里面的默认填的信息为从后台获取失败时会显示的内容
            username:'用户名',//用户名
            userid:'8080',//用户id
            usermotto:'个性签名',//没有就返回空
            userheadimg:'/static/ZA_User/img/HeaderImg/head.jpg',//用户头像
            emailif:1,//判断邮箱是否存在，0不存在，1存在，下面if同理
            emailvalue:"example@email.com",//若存在返回邮箱exa***@qq.com,不存在返回空值
            phoneif:1,
            phonevalue:13312345678,//手机号同邮箱
            passwordif:1,
            passwordvalue:"已设置",//占位，不用传
            questionif:0,
            questionvalue:"未设置密保问题",//占位，不用传
            certificationif:0,
            certificationvalue:"未实名认证",//占位，不用传
            birthday:'1990-01-01',
            sex:2,//性别
            sexselect:['','',''],//占位，不用带
            ip:'127.0.0.1',
            identity:'校外人士',
            truename:'*哈哈',//实名认证页面
            idcard:'41***************3',//实名认证页面
          } 
        },
        methods:{
          asideOpen:function(){
            this.ifblack = true;
          },
          asideClose:function(){
            this.ifblack = false;
          },
          loadingOpen:function(){
            this.ifloading = true;
          },
          loadingClose:function(){
            this.ifloading = false;
          },
          ajaxsuccess:function(data){
            // let temp=JSON.parse(data)
            this.userdata=Object.assign({}, this.userdata,data)

            if(this.userdata.emailif != 1){
                this.userdata.emailvalue="未绑定邮箱"
            }
            if(this.userdata.phoneif != 1){
                this.userdata.phonevalue="未绑定手机"
            }
            if(this.userdata.passwordif != 1){
                this.userdata.passwordvalue="未设置密码"
            }else{
                this.userdata.passwordvalue="已设置密码"
            }
            if(this.userdata.questionif != 1){
                this.userdata.questiondvalue="未设置密保问题"
            }else{
                this.userdata.questiondvalue="已设置密保问题"
            }
            if(this.userdata.certificationif != 1){
                this.userdata.certificationvalue="未实名认证"
            }else{
                this.userdata.certificationvalue="已实名认证"
            }
        }
        },
        created:function(){
        //从后台拿信息
        let user = document.cookie
        _temp = this
        console.log(_temp.userdata)
        console.log(_temp)
        $.ajax({
            type: "post",
            url: "/downloadpreson",
            data:user,
            processData: false,    //false
            cache: false,    //缓存
            beforeSend:function(){
              console.log(_temp)
              _temp.loadingOpen()
              _temp.ajaxsuccess(_temp.userdata)
            },
            success: function(data){
              //_temp.ajaxsuccess(data)     
            },
            fail:function(){
              console.log('请刷新页面重试')
            },
            complete:function(){
              console.log(_temp)
              _temp.loadingClose()
            }
      })
        },
    }).$mount('#tf-home')
