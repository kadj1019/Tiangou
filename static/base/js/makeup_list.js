/**
 * Created by Administrator on 2016/9/30.
 */
$(function () {
    $.get("Tiangou/json/makeup_list.json", function (data) {
        for (
            var i = 0; i < data.length; i++) {
            var obj = data[i];
            var msg = obj.msg;
            var price = obj.price;
            var img = obj.img;

            var liNode = $("<li></li>");
            $(".makeup_list").append(liNode);
            liNode.append("<a href='#'><img src=" + img + "></a>");
            liNode.append("<span>" + msg + "</span>");
            liNode.append("<span>" + price + "</span>");
        }
    })
    console.log($())
})