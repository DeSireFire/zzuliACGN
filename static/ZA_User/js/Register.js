//easytip 错误提示
// 调用方法：（样例）
//     var tip = $("#inputUserId").easytip();
//     tip.show("该用户名验证可用!")
//
//     在html相应id的标签中加入“data-easytip="position:top;class:easy-red;"”即可。

(function ($, window, document, undefined)
{
    var _easytip = function (ele, opt)
    {
        this.parent = ele;
        this.is_show = false;

        if (0 == this.parent.length) {
            throw new Error("easytip's is null !");
        }

        this.defaults = {
            left: 0,
            top: 0,
            position: "right",          //top, left, bottom, right
            disappear: "other",       	//self, other, lost-focus, none, N seconds, out
            speed: "fast",
            class: "easy-white",
            arrow: "bottom",          	//top, left, bottom, right 自动，手动配置无效
            onshow: null,               //事件
            onclose: null,               //事件
            hover_show: "false"			//鼠标移动到绑定目标时，是否自动出现
        };

        this._fun_cache = Object();    //响应函数缓存，用来保存show里面自动添加的click函数，以便于后面的unbind针对性的一个一个删除

        //从控件的 data-easytip中读取配置信息
        // var data = easy_load_options(ele[0].id, "easytip"); // # by galandeo, fix bug
        var data = easy_load_options(ele[0], "easytip");

        this.options = $.extend({}, this.defaults, opt, data);

        this.id = "easytip-div-main-" + ele[0].id;
    };

    _easytip.prototype = {

        init: function ()
        {
            var tip = $("#" + this.id);

            var $this = this;

            //同一个控件不会多次初始化。
            if (tip.length == 0) {
                $(document.body).append("<div id=\"" + this.id + "\"><div class=\"easytip-text\"></div></div>");

                tip = $("#" + this.id);
                var text = $("#" + this.id + " .easytip-text");

                tip.css({
                        "text-align": "left",
                        "display": "none",
                        "position": "absolute",
                        "z-index": 9000
                    }
                );

                text.css({
                        "text-align": "left",
                        "min-width": "120px"
                    }
                );

                tip.append("<div class=\"easytip-arrow\"></div>");
                var arrow = $("#" + this.id + " .easytip-arrow");
                arrow.css({
                        "padding": "0",
                        "margin": "0",
                        "width": "0",
                        "height": "0",
                        "position": "absolute",
                        "border": "10px solid"
                    }
                );

                if (this.options.hover_show == "true") {
                    this.options.disappear = "none";
                    this.options.speed = 1;
                    this.parent.hover(function ()
                        {
                            $this.show();
                        }, function ()
                        {
                            $this.close();
                        }
                    );
                }
            }

            return this;
        },

        _size: function ()
        {
            var parent = this.parent;
            var tip = $("#" + this.id);

            if (tip.width() > 300) {
                tip.width(300);
            }
        },

        _css: function ()
        {
            var tip = $("#" + this.id);
            var text = $("#" + this.id + " .easytip-text");
            var arrow = $("#" + this.id + " .easytip-arrow");

            text.addClass(this.options.class);

            arrow.css("border-color", "transparent transparent transparent transparent");
            tip.css("box-sizing", "content-box");
        },

        _arrow: function ()
        {
            var tip = $("#" + this.id);
            var text = $("#" + this.id + " .easytip-text");
            var arrow = $("#" + this.id + " .easytip-arrow");

            switch (this.options.arrow) {
                case "top":
                    arrow.css({
                            "left": "25px",
                            "top": -arrow.outerHeight(),
                            "border-bottom-color": text.css("borderTopColor")
                        }
                    );
                    break;

                case "left":
                    arrow.css({
                            "left": -arrow.outerWidth(),
                            "top": tip.innerHeight() / 2 - arrow.outerHeight() / 2,
                            "border-right-color": text.css("borderTopColor")
                        }
                    );
                    break;

                case "bottom":
                    arrow.css({
                            "left": "25px",
                            "top": tip.innerHeight(),
                            "border-top-color": text.css("borderTopColor")
                        }
                    );
                    break;

                case "right":
                    arrow.css({
                            "left": tip.outerWidth(),
                            "top": tip.innerHeight() / 2 - arrow.outerHeight() / 2,
                            "border-left-color": text.css("borderTopColor")
                        }
                    );
                    break;
            }
        },

        _position: function ()
        {
            var tip = $("#" + this.id);
            var text = $("#" + this.id + " .easytip-text");
            var arrow = $("#" + this.id + " .easytip-arrow");
            var offset = $(this.parent).offset();
            var size = {
                width: $(this.parent).outerWidth(),
                height: $(this.parent).outerHeight()
            };

            switch (this.options.position) {
                case "top":

                    //tip.css("left", offset.left - this.padding);
                    tip.css("left", offset.left);
                    tip.css("top", offset.top - tip.outerHeight() - arrow.outerHeight() / 2);
                    this.options.arrow = "bottom";

                    break;

                case "left":

                    tip.css("left", offset.left - tip.outerWidth() - arrow.outerWidth() / 2);
                    tip.css("top", offset.top - (tip.outerHeight() - size.height) / 2);
                    this.options.arrow = "right";

                    break;

                case "bottom":

                    //tip.css("left", offset.left - this.padding);
                    tip.css("left", offset.left);
                    tip.css("top", offset.top + size.height + arrow.outerHeight() / 2);
                    this.options.arrow = "top";

                    break;

                case "right":

                    tip.css("left", offset.left + size.width + arrow.outerWidth() / 2);
                    tip.css("top", offset.top - (tip.outerHeight() - size.height) / 2);
                    this.options.arrow = "left";

                    break;
            }

            var left = parseInt(tip.css("left"));
            var top = parseInt(tip.css("top"));

            tip.css("left", parseInt(this.options.left) + left);
            tip.css("top", parseInt(this.options.top) + top);
        },

        close: function (fn)
        {
            var tip = $("#" + this.id);
            var parent = this.parent;
            var onclose = this.options.onclose;
            this.is_show = false;

            //onclose事件
            if (!!onclose) {
                onclose(parent, tip[0]);
            }

            tip.fadeOut(this.options.speed, fn);
        },

        _show: function ()
        {
            var tip = $("#" + this.id);
            var text = $("#" + this.id + " .easytip-text");
            var arrow = $("#" + this.id + " .easytip-arrow");
            var speed = this.options.speed;
            var disappear = this.options.disappear;
            var parent = this.parent;
            var $this = this;
            this.is_show = true;

            if (this.options.hover_show == "true") {
                tip.show();
                return;
            }

            tip.fadeIn(speed, function ()
                {
                    if (!isNaN(disappear)) {
                        //如果disappear是数字，则倒计时disappear毫秒后消失
                        setTimeout(function ()
                            {
                                $this.close();

                            }, disappear
                        );
                    }
                    else if (disappear == "self" || disappear == "other") {
                        $(document).bind('click', $this._fun_cache[tip[0].id] = function (e)
                            {
                                if (disappear == "self" && e.target == text[0]) {
                                    $this.close(function ()
                                        {
                                            $(document).unbind("click", $this._fun_cache[tip[0].id]);
                                        }
                                    );

                                }
                                else if (disappear == "other" && e.target != tip[0]) {
                                    $this.close(function ()
                                        {
                                            $(document).unbind("click", $this._fun_cache[tip[0].id]);
                                        }
                                    );
                                }
                            }
                        );
                    }
                    else if (disappear == "lost-focus") {
                        $(parent).focusout(function ()
                            {
                                $this.close(function ()
                                    {
                                        $(parent).unbind("focusout");
                                    }
                                );
                            }
                        );
                    }

                }
            );
        },

        show: function (msg)
        {
            var tip = $("#" + this.id);
            var text = $("#" + this.id + " .easytip-text");
            var arrow = $("#" + this.id + " .easytip-arrow");
            var speed = this.options.speed;
            var disappear = this.options.disappear;
            var parent = this.parent;
            var $this = this;
            var onshow = this.options.onshow;

            if (!msg) {
                msg = parent.data("easytip-message");
            }

            text.html(msg);

            this._size();
            this._css();
            this._position();
            this._arrow();

            if ("none" == tip.css("display")) {
                //onshow事件
                if (!!onshow) {
                    onshow(parent, tip[0]);
                }
                $this._show();
            }
            else {
                tip.hide(1, function ()
                    {
                        if (!!onshow) {
                            onshow(parent, tip[0]);
                        }

                        $this._show();
                    }
                );
            }
        }
    };

    $.fn.easytip = function (options)
    {
        var tip = new _easytip(this, options);

        return tip.init();
    };

})(jQuery, window, document);

/**
 * 读取一个控件的指定data属性，并通过：和；来分割成key/value值对
 * @id string 控件id
 * @name string 属性名称
 **/
if (typeof(easy_load_options) == "undefined") {
    // function easy_load_options(id, name) // # by galandeo, fix bug
    function easy_load_options(obj, name)
    {
        var options = $(obj).data(name);
        // var options = $("#" + id).data(name);

        //将字符串用；分割
        options = (!!options ? options.split(";") : undefined);

        var data = Object();

        if (!!options) {
            var index;
            for (index in options) {
                var temps = options[index];
                var p = temps.indexOf(":");

                var temp = [];
                if (-1 == p) {
                    temp[0] = temps;
                    temp[1] = "";
                }
                else {
                    temp[0] = temps.substring(0, p);
                    temp[1] = temps.substring(p + 1);
                }

                if (temp[0].length > 0) {
                    data[temp[0]] = temp[1];
                }
            }
        }

        return data;
    }
}


var _user = false;
// 用户名检测以及ajax
function username() {
    //var
    var _username = $("#inputUserId");
    var _usernameVal = _username.val();
    var _usernameLen = _usernameVal.length;
    var _usernameReg = /^([\w]|[\u4e00-\u9fa5]|[ 。，、？￥“”‘’！：【】《》（）——.,?!$'":+-]){4,16}$/;
    // 判断是否符合前端正则
    if (_usernameReg.test(_usernameVal)) {
        // 符合前端验证，发送ajax请求进行后端验证
        $.get('/user/register_ajax/?user_name='+_usernameVal,function (data){
            if(data.count==0){
                var tip = $("#inputUserId").easytip();
                tip.show("该用户名验证可用!");
                $(".logoAction1").attr("class","logoAction1 glyphicon glyphicon-ok form-control-feedback");
                $(".uname").attr("class","form-group has-feedback uname has-success");
                _user = true;
                alert(_user);
                return _user;
            }else if(data.count>0){

                var tip = $("#inputUserId").easytip();
                tip.show("该用户名已被使用！");
                $(".uname").attr("class","form-group has-feedback uname has-error");
                $(".logoAction1").attr("class","logoAction1 glyphicon glyphicon-remove form-control-feedback");
                return false;
            }
        });
    } else {
        var tip = $("#inputUserId").easytip();
        $(".uname").addClass("has-error");
        $(".logoAction1").attr("class","logoAction1 glyphicon glyphicon-remove form-control-feedback");

        tip.show("用户名必须为4—16位的英文字母、数字或汉字！当前已经输入用户名的长度为："+_usernameLen+"。");
        return false;
    }
}

// 密码验证
function pwd() {
    //var
    var _pwd = $("#inputPassword1");
    var _pwdVal = _pwd.val();
    var _pwdLen = _pwdVal.length;
    var _pwdReg = /^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$/;
    // console.log($(".has-feedback")[1]);

    if (_pwdReg.test(_pwdVal)) {
        $(".pwd1").attr("class","form-group has-feedback pwd1 has-success");
        $(".logoAction2").attr("class","logoAction2 glyphicon glyphicon-ok form-control-feedback");
        return true;
    } else {
        $(".pwd1").attr("class","form-group has-feedback pwd1 has-error");
        $(".logoAction2").attr("class","logoAction2 glyphicon glyphicon-remove form-control-feedback");
        if ( _pwdLen < 6) {
            var tip = $("#inputPassword1").easytip();
            tip.show("密码过于短小，要至少六位密码哦");
        } else {
            var tip = $("#inputPassword1").easytip();
            tip.show("最少6位，包含至少1个大写字母，1个小写字母，1个数字，1个英文标点符号（比如英文“?”）！");
        }
        return false;
    }
}

// 密码确认
function pwdConfirm() {
    //var
    var _pwd1 = $("#inputPassword1");
    var _pwd2 = $("#inputPassword2");
    var _pwdVal1 = _pwd1.val();
    var _pwdVal2 = _pwd2.val();
    var _pwdLen = _pwdVal1.length;

    if (_pwdVal1 === _pwdVal2  && _pwdLen >= 6 ) {
        $(".pwd2").attr("class","form-group has-feedback pwd2 has-success");
        $(".logoAction3").attr("class","logoAction3 glyphicon glyphicon-ok form-control-feedback");
        return true;
    } else {
        $(".pwd2").attr("class","form-group has-feedback pwd2 has-error");
        $(".logoAction3").attr("class","logoAction3 glyphicon glyphicon-remove form-control-feedback");
        if (_pwdLen < 6){
            var tip = $("#inputPassword2").easytip();
            tip.show("密码太短了！");
        } else {
            var tip = $("#inputPassword2").easytip();
            tip.show("密码两次输入得不相同欸！");
        }
        return false;
    }
}

// 邮箱验证以及ajax验证
var _email = false;
function email() {
    //var
    var _useremail = $("#inputEmail1");
    var _useremailVal = _useremail.val();
    var _useremailReg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    // 判断是否符合前端正则
    if (_useremailReg.test(_useremailVal)) {
        // 符合前端验证，发送ajax请求进行后端验证
        $.get('/user/register_ajax/?user_email='+_useremailVal,function (data){
            if(data.count==0){
                var tip = $("#inputEmail1").easytip();
                tip.show("该电子邮箱验证可用!");
                $(".logoAction4").attr("class","logoAction4 glyphicon glyphicon-ok form-control-feedback");
                $(".email").attr("class","form-group has-feedback email has-success");
                _email = true;
                alert(_email);
                return _email;
            }else if(data.count>0){

                var tip = $("#inputEmail1").easytip();
                tip.show("该邮箱已被使用过，同个邮箱不能重复注册！");
                $(".email").attr("class","form-group has-feedback email has-error");
                $(".logoAction4").attr("class","logoAction4 glyphicon glyphicon-remove form-control-feedback");
                return false;
            }
        });
    } else {
        var tip = $("#inputEmail1").easytip();
        $(".email").attr("class","form-group has-feedback email has-error");
        $(".logoAction4").attr("class","logoAction4 glyphicon glyphicon-remove form-control-feedback");

        tip.show("电子邮箱的格式好像不太对！");
        return false;
    }
}

var _phone = false;
// 手机号码验证以及ajax验证
function phone() {
    //var
    var _userphone = $("#inputphone1");
    var _userphoneVal = _userphone.val();
    var _userphoneLen = _userphoneVal.length;
    var _userphoneReg = /^1[34578]\d{9}$/;
    // 判断是否符合前端正则
    if (_userphoneLen !== 0){
        if (_userphoneReg.test(_userphoneVal)) {
            // 符合前端验证，发送ajax请求进行后端验证
            $.get('/user/register_ajax/?user_phone='+_userphoneVal,function (data){
                if(data.count==0){
                    var tip = $("#inputphone1").easytip();
                    tip.show("该号码验证可用!");
                    $(".logoAction1").attr("class","logoAction1 glyphicon glyphicon-ok form-control-feedback");
                    $(".phone").attr("class","form-group has-feedback phone has-success");
                    _phone = true;
                    return _phone
                }else if(data.count>0){

                    var tip = $("#inputphone1").easytip();
                    tip.show("该手机号已被注册！");
                    $(".phone").attr("class","form-group has-feedback phone has-error");
                    $(".logoAction5").attr("class","logoAction5 glyphicon glyphicon-remove form-control-feedback");
                    return _phone;
                }
            });

        } else {
            var tip = $("#inputphone1").easytip();
            $(".phone").attr("class","form-group has-feedback phone has-error");
            $(".logoAction5").attr("class","logoAction5 glyphicon glyphicon-remove form-control-feedback");

            tip.show("号码的格式好像不太对！");
            return _phone;
        }
    } else {
        _phone = true;
        return true;
    }

}

var VC_res = false;
window.callback = function(res){
    // res（未通过验证）= {ret: 1, ticket: null}
    // res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
    if(res.ret === 0){
        // alert(res.ticket); // 票据
        VC_res = true;
        return VC_res;
    } else {
        VC_res = false;
        return VC_res;
    }
};


//阅读协议勾选
function checkBox() {
    //var
    var checkBox = $("#inputcheckbox");
    //检查checked
    if (checkBox.is(":checked")) {
        return true;
    } else {
        var tip = $("#inputcheckbox").easytip();
        tip.show("必须勾选同意协议才能注册哦");
        return false;
    }
}

function getCookie(name) {
    var cookieValue = null;
     if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
        }
    }
    }
    return cookieValue;
}

// 前端认证汇总
function register() {
    // var _user = _user;
    var _pwd = pwd();
    var _pwd2 = pwdConfirm();
    // var _email = _email;
    var _checkBox = checkBox();
    // var _callback = VC_res;
    // var _phone = _phone;
    alert("user:"+_user);
    alert("pwd:"+_pwd);
    alert("pwd2:"+_pwd2);
    alert("email:"+_email);
    alert("checkBox:"+_checkBox);
    alert("callback:"+_callback);
    alert("phone:"+_phone);
    //judge
    if (_user === true && _pwd === true && _pwd2 === true && _email === true && _checkBox === true && _callback === true && _phone === true ){
    // if (_user === true && _pwd === true && _pwd2 === true && _email === true && _checkBox === true && _phone === true ){
        var _usernameVal = $("#inputUserId").val();
    //     var _usernameVal = $("#inputPassword1").val();
        $.post(url, {
            'user_name':_usernameVal,
            'key2':val2
        });
        return true;
    } else {
        var tip = $(".btn-register").easytip();
        tip.show("注册信息不够完善！无法提交！请检查");
        return false;
    }


}

// 前端认证主函数
$(document).ready(function() {
    $("#inputUserId").blur(username);
    $("#inputPassword1").blur(pwd);
    $("#inputPassword2").blur(pwdConfirm);
    $("#inputEmail1").blur(email);
    $("#inputphone1").blur(phone);
    $("#inputcheckbox").blur(checkBox);
    $(".btn-register").click(register);
});
