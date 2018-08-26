/**
 * Created by ruanqing on 17-12-8.
 */


$(document).ready(function(){
    $(".form-horizontal").easyform();
});

function ajax_message()
{
    var error_name = null;
    var WebHandler = $('.form-horizontal').easyform();
    $.get('/user/register_ajax/?user_name='+$('#inputUserId').val(),function (data){
        if(data.user_name==1){

            // WebHandler.submit = true;
            var tip = $("#inputUserId").easytip();
            tip.show("该用户名验证可用!");
            var error_name = true;

        }else if(data.user_name==0){

            WebHandler.submit = false;
            var tip = $("#inputUserId").easytip();
            tip.show("该用户名验证可用!");
            var error_name = false;

        }

        $("#inputUserId").trigger("easyform-ajax",error_name);
    });
}

