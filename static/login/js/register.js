/**
 * Created by Administrator on 2016/10/8.
 */
$(function () {
    $(".loginLeft input").eq(0).blur(function () {
        var str = $(this).val();
        var email = /^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$/;
        if (!email.test(str)) {
            $(this).parent().find("strong").html("邮箱不正确");
        } else {
            $(this).parent().find("strong").html("输入正确");
        }
    }).focus(function () {
        $(this).parent().find("strong").html("填写正确的邮箱");
    });

    $(".loginLeft input").eq(1).blur(function () {
        var str1 = $(this).val();
        var user = /^\w{4,20}$/;
        if (!user.test(str1)) {
            $(this).parent().find("strong").html("你输入的用户名不正确");
        } else {
            $(this).parent().find("strong").html("用户名可以注册");
        }
    }).focus(function () {
        $(this).parent().find("strong").html("4-20英文字符,数字,'_'的组合。");
    });

    $(".loginLeft input").eq(2).blur(function () {
        var str2 = $(this).val();
        var psw = /^.{6,16}$/;
        if (!psw.test(str2)) {
            $(this).parent().find("strong").html("密码不合法,请确认");
        } else {
            $(this).parent().find("strong").html("密码合法");
        }
    }).focus(function () {
        $(this).parent().find("strong").html("6-16位字符");
    });

    $(".loginLeft input").eq(3).blur(function () {
        var str3 = $(this).val();
        var psw1 = /^.{6,16}$/;
        if (!psw1.test(str3)) {
            $(this).parent().find("strong").html("密码不合法,请确认");
        } else if (str3 != $(".loginLeft input").eq(2).val()) {
            $(this).parent().find("strong").html("2次密码不一致,请确认");
        } else {
            $(this).parent().find("strong").html("密码一致");
        }
    }).focus(function () {
        $(this).parent().find("strong").html("6-16位字符");
    });


    $(".suiJi").click(function () {
        var sstr = "";
        for (var i = 0; i < 4; i++) {
            var num = Math.round(Math.random());
            if (num == 0) {
                var sstr1 = parseInt(Math.random() * 10);
                sstr += sstr1;
            } else {
                var sstr2 = String.fromCharCode(parseInt(Math.random() * 24 + 65));
                sstr += sstr2;
            }
        }
        $(".suiJi").html(sstr);
    });


    $(".loginLeft input").eq(5).click(function () {
        if ($(".loginLeft input").eq(0).parent().find("strong").html() != "输入正确") {
            alert("邮箱不正确");
        } else if ($(".loginLeft input").eq(1).parent().find("strong").html() != "用户名可以注册") {
            alert("你输入的用户名不正确");
        } else if ($(".loginLeft input").eq(2).parent().find("strong").html() != "密码合法") {
            alert("密码不合法,请确认");
        } else if ($(".loginLeft input").eq(3).parent().find("strong").html() != "密码一致") {
            alert("2次密码不一致,请确认");
        } else if ($(".loginLeft input").eq(4).val() != $(".suiJi").html()) {
            alert("验证码输入错误")
        } else {
            $(".loginLeft input").eq(5).click(function () {

                console.log("1")

            })
        }


    });


    // 登录页面
    $(".loginRight input").eq(2).click(function () {
        if ($(".loginRight input").eq(0).val() == "") {
            alert("不能为空");
        } else if ($(".loginRight input").eq(1).val() == "") {
            alert("不能为空");
        } else {
            $(".loginRight input").eq(2).click(function () {

                console.log("1")

            })
        }
    });
});