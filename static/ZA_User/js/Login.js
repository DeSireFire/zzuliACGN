/**
 * Created by ruanqing on 17-9-4.
 */
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

// 用户名验证
function usernameCheck() {
    // var
    var _username = $("#inputUserId").val();
    var _usernameLen = _username.length;

    if (_usernameLen <= 0){
        var tip = $("#inputUserId").easytip();
        tip.show("好家伙，你居然不写用户名，这是让本站怎么登陆呢？");
        return false
    } else if (_usernameLen < 4){
        var tip = $("#inputUserId").easytip();
        tip.show("敢不敢用户名再长一点呐？");
        return false
    } else {
        return true
    }
}

//密码验证
function pwd() {
    var _pwd = $("#inputPassword1").val();
    var _pwdLen = _pwd.length;
    if (_pwdLen <= 0){
        var tip = $("#inputPassword1").easytip();
        tip.show("朋友，你写一下密码好不好啦？");
        return false
    } else{
        return true
    }
}

//拼图验证
var VC_ticket = null;
window.callback = function(res){
    // res（未通过验证）= {ret: 1, ticket: null}
    // res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
    if(res.ret === 0){
        // alert(res.ticket); // 票据
        VC_ticket = res.ticket;
        return VC_ticket;
    } else {
        return VC_ticket;
    }
};

//记忆登录状态！
function checkBox() {
    //var
    var checkBox = $("#inputcheckbox");
    //检查checked
    if (checkBox.is(":checked")) {
        return true;
    } else {
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

function login(){
    // var
    var _checkBox = checkBox();
    var _usernameCheck = usernameCheck();
    var _pwd = pwd();
    var _loginTicket = VC_ticket;
    var _usernameVal = $("#inputUserId").val();
    var _pwdVal = $("#inputPassword1").val();
    console.log(_usernameVal);
    console.log(_pwdVal);
    console.log(_loginTicket);
    console.log(_checkBox);
    if(_usernameCheck === true && _pwd === true && _loginTicket !== null){

        $.ajax({
            url: "http://192.168.0.104:5360/user/loginHandle/",     // 此处URL一定要改！
            method: "post",
            headers:{'X-CSRFToken': getCookie('csrftoken')},
            data: {
            'user_name':_usernameVal,
            'password':_pwdVal,
            'loginTicket':_loginTicket,
            'rememberme':_checkBox
            },


            // 回调函数
            success: function(data){

                if(data.login === "ok"){
                    // 后端验证通过ok
                    console.log("max_age:"+data.max_age);
                    if(data.max_age == -1){
                        $.cookie("url",'',{ path: '/', max_age:-1 });
                        $.cookie("zzuliacgn_user_name", data.zzuliacgn_user_name ,{ path: '/', max_age:-1 });
                    } else {
                        $.cookie("url",'',{ expires: data.Expires, path: '/', max_age: data.max_age });
                        $.cookie("zzuliacgn_user_name", data.zzuliacgn_user_name ,{ expires: data.Expires, path: '/', max_age: data.max_age });
                    }
                    window.location.href='/';
                } else if(data.login === "no"){
                    // 后端验证不通过no
                    var tip = $(".btn-login").easytip();
                    tip.show("用户名、邮箱或者密码不正确呢！");
                }
            }
        });

        //用户名和密码等函数检查通过，防止submit在未通过ajax时依然出现无差别跳转。
        return false
    } else {
        var tip = $(".btn-login").easytip();
        tip.show("用户名、邮箱或者密码不正确呢！");
        //用户名和密码等函数检查不通过返回false
        return false
    }

}



// 前端登陆主函数
$(document).ready(function() {
    $("#inputUserId").blur(usernameCheck);
    $("#inputPassword1").blur(pwd);
    $("#inputcheckbox").blur(checkBox);
    $(".btn-login").click(login);
});