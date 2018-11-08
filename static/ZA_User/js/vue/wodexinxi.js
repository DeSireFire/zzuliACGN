let wodexinxi = Vue.component('per-inf',{
    props:['userdata'],
    template:`
    <div>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <h2><i class="fa fa-address-card-o fa-2x"></i> 我的信息</h2>
            <a href="#" class="btn btn-user btn-xs">更多设置</a>
        </div>
        <div class="line-border"></div>
        <div>
            <div class="form-group form-group-sm">
                <label class="col-sm-2 control-label" for="username">昵称：</label>
                <input class="form-control" v-model="userdatatemp.username" type="text" id="username" placeholder="昵称">
            </div>
            <!-- 个性签名做处理防止xml注入 -->
            <div class="form-group form-group-sm">
                <label class="col-sm-2 control-label" for="usermotto">个性签名：</label>
                <input class="form-control" v-model="userdatatemp.usermotto" type="text" id="usermotto" placeholder="个性签名">
            </div>
            <div class="form-group form-group-sm">
                <label class="col-sm-2 control-label" for="birthday">出生日期：</label>
                <input class="form-control" v-model="userdatatemp.birthday" type="date" id="birthday" placeholder="如：1998-05-25">
            </div>
            <div class="form-group form-group-sm sex-radio-container">
                用户性别? XiuJi?：
                <label class="radio-inline" :class="userdatatemp.sexselect[0]">
                     <input @click="sexclick" type="radio" v-model="userdatatemp.sex" name="sex" id="inlineRadio1" value="0"> 
                     <span class="sex-btn">猛汉</span>
                </label>
                <label class="radio-inline" :class="userdatatemp.sexselect[1]">
                    <input @click="sexclick" type="radio" v-model="userdatatemp.sex" name="sex" id="inlineRadio2" value="1"> 
                    <span class="sex-btn">萌妹</span>
                </label>
                <label class="radio-inline" :class="userdatatemp.sexselect[2]">
                    <input @click="sexclick" type="radio" v-model="userdatatemp.sex" name="sex" id="inlineRadio2" value="2"> 
                    <span class="sex-btn">保密</span>
                </label>
            </div>
            <div class="form-group form-group-sm">
                <label class="col-sm-2 control-label">上次登录IP：</label>
                    <input class="form-control" v-model="userdatatemp.ip" type="text" id="FromIP" placeholder="127.0.0.1" readonly>
            </div>
            <div class="form-group form-group-sm">
                <label class="col-sm-2 control-label" for="identity">用户身份：</label>
                    <input class="form-control" v-model="userdatatemp.identity" type="text" id="identity" placeholder="校外人士" readonly>
            </div>
            <button @click="upload" id="false-id-sumbit" class="btn btn-default">保存</button>
            <!-- <div class="form-group form-group-sm active">
                <label class="col-sm-2 control-label">院系 Faculty</label>
                <div class="col-sm-4" readonly>
                    <select class="form-control" name="in-school">
                        <option value="1">电气信息工程学院</option>
                        <option value="2">机电工程学院</option>
                        <option value="3">食品与生物工程学院</option>
                        <option value="4">烟草科学与工程学院</option>
                        <option value="5">材料与化学工程学院</option>
                    </select>
                </div>
            </div> -->
        </div>
    </div>
</div>
    `,
    data:function(){
        return{
            userdatatemp:{
                username:'',
                usermotto:'',
                sexselect:['','',''],
                sex:'',
                ip:'',
                birthday:'',
                identity:'',
            },
        }
    },
    methods:{
        sexclick:function(e){//高亮选中按钮与更改选中的值
            if(e.target.tagName === "INPUT"){
                console.log(e)
                console.log(e.target.value)
                for(let i=0;i<this.userdatatemp.sexselect.length;i++){
                    if(i === parseInt(e.target.value)){
                        console.log('xxx')
                        this.userdatatemp.sexselect[i] = 'active'
                        this.userdatatemp.sex=i
                    }else{
                        this.userdatatemp.sexselect[i] = ''
                    }
                }
            }
        },
        upload:function(){
            if(this.userdatatemp.username){
                if(!(/^([\w]|[\u4e00-\u9fa5]|_){4,16}$/ig.test(this.userdatatemp.username))){
                    alert('昵称只能输入4-16位英文、数字、汉字或_组合')
                    return
                }
            }else{
                alert('请填写昵称')
                return
            }
            let user = document.cookie
            let data={user:user,username:this.userdatatemp.username,usermotto:this.userdatatemp.usermotto,birthday:this.userdatatemp.birthday,sex:this.userdatatemp.sex}
            $.ajax({
                type: "post",
                url: "/uploadpreson",
                data: JSON.stringify(data),
                processData: false,    //false
                cache: false,    //缓存
                beforeSend:function(){
                    $('.loading').addClass("active")
                },
                success: function(data){
                    console.log(data);      
                },
                fail:function(){
                    console.log('error')
                },
                complete:function(){
                    setTimeout(function(){
                        $('.loading').removeClass("active")
                    },1000)
                }
          })

        }
    },
    created:function(){
        this.userdatatemp.username = this.userdata.username
        this.userdatatemp.usermotto = this.userdata.usermotto
        this.userdatatemp.sex = this.userdata.sex
        this.userdatatemp.ip = this.userdata.ip
        this.userdatatemp.birthday = this.userdata.birthday
        this.userdatatemp.identity = this.userdata.identity
        this.userdatatemp.sexselect[this.userdatatemp.sex] = 'active'
    }
})