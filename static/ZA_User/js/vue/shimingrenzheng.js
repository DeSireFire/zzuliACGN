let shimingrenzheng = Vue.component('certification-id',{
    props:['userdata'],
    template:`
    <div>
    <div v-if=!userdatatemp.authenticated>
    <div class="row user-msg text-left">
        <div class="user-msg-title">
            <h2><i class="fa fa-user-plus fa-2x"></i> 实名认证</h2>
        </div>
        <div class="line-border"></div>
        <div class="notice-sth">
            <p style="acolor:#00a1d6;font-size:18px">实名认证成功后,可以享受开通直播间等服务!</p>
            <p><i class="fa fa-exclamation-triangle"></i>注意事项 </p>
            <p>1.每个证件只能绑定一个账号
            <p>2.证件照不清晰或与输入的信息不匹配,将导致实名认证被驳回
            <p>3.您提供的证件信息将受到严格保护,仅用于身份验证,未经本人许可不会用于其他用途</p>
            <p><i class="fa fa-exclamation-triangle" style="color:#F25D8E"></i>证件要求</p>
            <p>1.需上传本人露脸手持二代身份证背面照＋身份证正反面照片（不需手持）</p>
            <p>2.证件必须在有效期内，有效期需在一个月以上</p>
            <p><i class="fa fa-exclamation-triangle" style="color:#F25D8E"></i>照片要求</p>
            <p>1.本人手持证件正面露脸，五官清晰可辨</p>
            <p>2.证件照上信息需完整且清晰可辨（无反光、遮挡、水印、证件套、logo等）</p>
            <p>3.申请人填写的“真实姓名”和“证件号码”需和提交证件照片信息一致</p>
            <p>4.证件必须真实拍摄，不能使用复印件</p>
            <p>5.确保照片完整（不缺边角），证件周围不允许加上边角框（如：加上红框等）</p>
        </div>
    </div>
    <main>
        <label for="true-name">真实姓名：<input type="text" v-model=userdatatemp.truename value="xx" name="true-name"></label>
        <select name="itype" v-model=userdatatemp.itype>
            <option value="0">身份证</option>
            <option value="1">港澳居民来往内地通行证</option>
            <option value="2">台湾居民来往大陆通行证</option>
            <option value="3">护照(中国签发)</option>
            <option value="4">护照(外国签发)</option>
            <option value="5">外国人永久居留证</option>
        </select>
        <label for="id-number">证件号：<input type="text" v-model=userdatatemp.idcard name="id-number"></label>
        <div>
            <div id="idcard-obverse-container" class="idcard-container">
                <p>正面</p>
                <img id="idcard-obverse" :src="userdatatemp.idcardobverse">
            </div>
            <div class="btn-container">
                <label class="btn btn-primary btn-upload" for="input-idcard-obverse" title="Upload image file">
                    <input @change="selectimg" type="file" class="sr-only" id="input-idcard-obverse" name="idcardobverse" accept=".jpg,.jpeg,.png,.gif,.bmp,.tiff">
                    <span class="docs-tooltip" data-toggle="tooltip" data-animation="false" title="Import image with Blob URLs">
                     选择图片<span class="fa fa-upload"></span>
                    </span>
                </label>
            </div>
        </div>
    </main>
    <div>
        <div id="idcard-reverse-container" class="idcard-container">
            <p>反面</p>
            <img id="idcard-reverse" :src="userdatatemp.idcardreverse">
        </div>
        <div class="btn-container">
           <label class="btn btn-primary btn-upload" for="input-idcard-reverse" title="Upload image file">
                <input @change="selectimg" type="file" class="sr-only" id="input-idcard-reverse" name="idcardreverse" accept=".jpg,.jpeg,.png,.gif,.bmp,.tiff">
                <span class="docs-tooltip" data-toggle="tooltip" data-animation="false" title="Import image with Blob URLs">
                  选择图片<span class="fa fa-upload"></span>
                </span>
            </label>                                  
        </div>
    </div>
    <button @click="updata" id="true-id-sumbit" class="btn btn-default">上传</button>
    </div>
    <div v-if=userdatatemp.authenticated>
        <div><h3>您已通过了实名认证</h3></div>
        <div>
            <p><span>真实姓名：</span>{{userdata.truename}}</p>
            <p><span>证号号码：</span>{{userdata.idcard}}</p>
        </div>
    </div>
    </div>
    `,
    data:function(){
        return{
            userdatatemp:{
                authenticated:false,
                truename:'哈哈',
                idcard:'41***************3',
                itype:'0',
                idcardreverse:'../../img/background/head-zhanwei.png',
                idcardobverse:'../../img/background/head-zhanwei.png',
                formdata:'',
            }
        }
    },
    methods:{
        selectimg:function(e){
            _temp = this
            console.log(e)
            let fileInput = e.target;
            console.log(fileInput.files[0])        
            let file = fileInput.files[0];
            if(file.size > 5242880){
                alert('上传图片请小于5mb')
                return
            }
            if(file.type.indexOf("image") < 0){
                alert('请上传图片文件')
                return
            }   
            //创建一个临时链接用来预览图片
            //兼容性可能有问题，待定
            _temp.userdatatemp[e.target.name] = window.URL.createObjectURL(file)
            //------------   
            this.userdatatemp.formdata.set(e.target.name, file,e.target.name)
        },
        updata:function(){
            let _temp = this
            if(!this.userdatatemp.truename){
                alert('请输入名字')
                return
            }else if(!/^[\u4E00-\u9FA5\uf900-\ufa2d·]{2,20}$/.test(this.userdatatemp.truename)){
                console.log(this.userdatatemp.truename)
                alert('输入名字不符合规范,至少两个汉字')
                return
            }else{
                this.userdatatemp.formdata.set('truename',_temp.userdatatemp.truename)
            }
            if(!this.userdatatemp.idcard){
                alert('请输入证件号')
                return
            }else if(!/(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/.test(this.userdatatemp.idcard)){
                alert('身份证号填写有误');  
                return
            }else{
                this.userdatatemp.formdata.set('idcard',_temp.userdatatemp.idcard)
            }
            if(!(this.userdatatemp.formdata.has('idcardreverse')&&this.userdatatemp.formdata.has('idcardobverse'))){
                alert('请上传身份证照片')
            }
            console.log(_temp.userdatatemp.formdata)
            $.ajax({
                url:'/xxx',
                type:'POST',
                processData:false,
                contentType: false,
                data:_temp.userdatatemp.formdata,
                beforeSend:function(){
                    _temp.$emit('loading-open')
                },
                success:function(data){
                    console.log('上传成功')
                },
                fail:function(){
                    console.log('上传失败')
                    _temp.$emit('updata-fail')
                },
                complete:function(){
                    _temp.$emit('loading-close')
                }
            })
        }
    },
    created:function(){
        if(this.userdata.certificationif == 1){
            this.userdatatemp.authenticated = true
        }
        this.userdatatemp.formdata = new FormData()
    }
})