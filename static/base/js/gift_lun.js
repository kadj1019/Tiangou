/**
 * Created by Administrator on 2016/9/29.
 */
$(function(){

    function lunbo(){
        var j=1;
        setInterval(function(){
            move();
            j++;
        },2000);
        function move(){
            var size = $(".gift_lun img").length;

            if(j==size){
                j=0;
                $(".gift_lun img").fadeOut(1000).eq(j).fadeToggle(1000);
            }else {
                $(".gift_lun img").fadeOut(1000).eq(j).fadeToggle(1000);
            }
        }
    }
    lunbo();

});