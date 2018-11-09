let wodetouxiang = Vue.component('my-head',{
    props:['userdata'],
    template:`
    <div>
    <div class="row user-msg text-left">
        <div class="user-msg-title"><h2><i class="fa fa-user-o fa-2x"></i> 我的头像</h2></div>
        <div class="line-border"></div>
    </div>
    <div class="text-center">
        <div class="user-head">
            <img :src="userdata.userheadimg" class="img-circle"  width="105" height="105"/>
        </div>
        <div class="cas-container">
            <div id="img-container">
                <img id="user-head-image" src="/static/ZA_User/img/background/head-zhanwei.png">
            </div>
            <div id="pre-container">
                <div class=""><div class="img-preview squ"><img src="/static/ZA_User/img/background/preview.png"></div><p>方形头像</p></div>
                <div class=""><div class="img-preview cir"><img src="/static/ZA_User/img/background/preview.png"></div><p>圆形头像</p></div>
            </div>
        </div>
        <div class="btn-container">
            <label @change="selectimg"class="btn btn-primary btn-upload" for="input-image" title="Upload image file">
                <input type="file" class="sr-only" id="input-image" name="file" accept=".jpg,.jpeg,.png,.gif,.bmp,.tiff">
                <span class="docs-tooltip" data-toggle="tooltip" data-animation="false" title="Import image with Blob URLs">
                  选择图片<span class="fa fa-upload"></span>
                </span>
            </label>
        </div>
        <button @click="updatehead" id="change-img-btn"type="button" class="btn btn-user">上传头像</button>
    </div>
</div>
    `,
    data:function(){
        return {xxx:1}
    },
    methods:{
        selectimg:function(e){
            let fileInput = e.target;
            console.log(fileInput.files[0])        
            let file = fileInput.files[0];        //创建读取文件的对象
            if(file.size > 5242880){
                alert('上传图片请小于5mb')
                return
            }
            if(file.type.indexOf("image") < 0){
                alert('请上传图片文件')
                return
            }
            if(this.xxx===1){
                $('#user-head-image').cropper({
                    aspectRatio:1/1,
                    movable:true,
                    minContainerWidth:200,
                    minContainerHeight:127,
                    preview:$(".img-preview"),
                    dragMode:'move',
                    crop: function(event) {
                    }
                  })
                  this.xxx=0
            }  
            let reader = new FileReader();                 //创建文件读取相关的变量       
            let imgFile;                 //为文件读取成功设置事件        
            reader.onload=function(e) {            
                // alert('文件读取完成');            
                imgFile = e.target.result;                 
                $('#img-container>img').cropper('replace',imgFile,false );
            };                 
            reader.readAsDataURL(file);
        },
        updatehead:function(e){
            let user = document.cookie
            if(this.xxx === 1){
                alert('请选择图片')
                return
            }
            let cas=$('#img-container>img').cropper('getCroppedCanvas');
            let base64url=cas.toDataURL('image/jpeg');
            cas.toBlob(function (e) {
                console.log(e);  //生成Blob的图片格式，base64卡顿时使用
            })
            console.log(base64url); //生成base64图片的格式
            let temp = {user:user,userheadimg:base64url}
            _temp = this
            $.ajax({
                url:'/user/header_Update/',
                type:'POST',
                data:temp,
                beforeSend:function(){
                    _temp.$emit('loading-open')
                },
                success:function(data){
                    console.log('上传成功')
                },
                fail:function(){
                    console.log('上传失败')
                },
                complete:function(){
                    _temp.$emit('loading-close')
                }
            })
        },
    },
})