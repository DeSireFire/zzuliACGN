/**
 * Created by ruanqing on 17-12-8.
 */


$(document).ready(function(){
    $('#reg-form').easyform();
});


// function check_user_name(error_name) {
//     var WebHandler = $('#reg-form').easyform();
//     $.get('/user/RegHandle_skip/?user_name='+$('#uid').val(),function (data) {
//         if(data.count==1){
//
//             // alert("该用户名验证成功！");
//             WebHandler.submit = true;
//             WebHandler.success = function () {
//                 WebHandler.show("#uid", "自定义消息");
//             };
//             var error_name = true;
//
//
//         }else if(data.count==2){
//
//             // alert("该用户名已被使用！");z
//             WebHandler.submit = false;
//             var error_name = false;
//
//         }
//         return error_name;
//     });
// }

// function ajax_message(num)
// {
//     var error_name = null;
//     check_user_name(error_name);
//     alert(error_name);
//     $("#uid").trigger("easyform-ajax",error_name);
// }

function ajax_message()
{
    var error_name = null;
    var WebHandler = $('#reg-form').easyform();
    $.get('/user/RegHandle_skip/?user_name='+$('#uid').val(),function (data){
        if(data.count==1){

            WebHandler.submit = true;
            var tip = $("#uid").easytip();
            tip.show("该用户名验证可用!");
            var error_name = true;

        }else if(data.count==2){

            WebHandler.submit = false;
            var error_name = false;

        }
        $("#uid").trigger("easyform-ajax",error_name);
    });

}