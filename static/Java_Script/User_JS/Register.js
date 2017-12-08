/**
 * Created by ruanqing on 17-12-8.
 */

// $(document).ready(function(){
//     var WebHandler = $('#reg-form').easyform();
// });
// function check_user_name(){
//
//     $.get('/user/RegHandle_skip/?user_name='+$('#uid').val(),function (data) {
//         if(data.count==1){
//
//             alert("该用户名验证成功！")
//             WebHandler.submit = true
//             ajax_message(true)
//             return true
//
//         }else if(data.count==2){
//
//             alert("该用户名已被使用！")
//             WebHandler.submit = false
//             ajax_message(false)
//             return false
//         }
//         alert(data.Judgement)
//         WebHandler.submit = data.Judgement
//         return $("#uid").trigger("easyform-ajax", false);
//     });
// }
//
// function ajax_message(num)
// {
//
//     if (num==1){
//         alert(num)
//         check_user_name()
//     }
//
// }

$(document).ready(function(){
    $('#reg-form').easyform();
});
function ajax_message(num)
{
    // var WebHandler = $('#reg-form').easyform();
    //
    // var error_name = true;
    //
    // WebHandler.submit = false;
    //
    // if (num==1){
    //     $.get('/user/RegHandle_skip/?user_name='+$('#uid').val(),function (data) {
    //         WebHandler.submit = data.Judgement;
    //         error_name = data.Judgement;
    //     })
    //
    // }
    // if (error_name==false){
    //
    //     $("#uid").trigger("easyform-ajax", false);
    // }else {
    //     $("#uid").trigger("easyform-ajax", true);
    // }
    $("#uid").trigger("easyform-ajax", false);
}