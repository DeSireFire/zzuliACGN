(function(){
    $("#input-image").one("change",function(){
        $('#user-head-image').cropper({
            aspectRatio:1/1,
            movable:true,
            minContainerWidth:200,
            minContainerHeight:127,
            preview:$(".img-preview"),
            dragMode:'move',
            crop: function(event) {
              console.log(this)
              console.log(event.detail.x);
              console.log(event.detail.y);
              console.log(event.detail.width);
              console.log(event.detail.height);
              console.log(event.detail.rotate);
              console.log(event.detail.scaleX);
              console.log(event.detail.scaleY);
            }
          });
    });
    $("#input-image").on("change", function (e) {
        var fileInput = document.getElementById("input-image");        
        var file = fileInput.files[0];        //创建读取文件的对象
        console.log(file)        
        var reader = new FileReader();                 //创建文件读取相关的变量       
        var imgFile;                 //为文件读取成功设置事件        
        reader.onload=function(e) {            
            // alert('文件读取完成');            
            imgFile = e.target.result;            
            console.log(imgFile);       
            $('#img-container>img').cropper('replace',imgFile,false );
        };                 
        reader.readAsDataURL(file);
        $("#pre-container").addClass('active')
    });
    //剪切部分转换为base64
    $("#change-img-btn").on("click", function () {
        var cas=$('#img-container>img').cropper('getCroppedCanvas');
        var base64url=cas.toDataURL('image/jpeg');
        cas.toBlob(function (e) {
            console.log(e);  //生成Blob的图片格式
        console.log(base64url); //生成base64图片的格式
        });
        $.ajax({
            url:'127.0.0.1',
            type:'POST',
            data:base64url,
            success:function(data){
                console.log('上传成功')
            },
            error:function(){
                console.log('上传失败')
            }
        })
    })
})();