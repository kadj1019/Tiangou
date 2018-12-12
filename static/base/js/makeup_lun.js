$(function () {

    function lunbo() {
        var j = 1;
        setInterval(function () {
            move();
            j++;
        }, 2000);

        function move() {
            var size = $(".makeup_lun img").length;

            if (j == size) {
                j = 0;
                $(".makeup_lun img").fadeOut(1000).eq(j).fadeToggle(1000);
            } else {
                $(".makeup_lun img").fadeOut(1000).eq(j).fadeToggle(1000);
            }
        }
    }
    lunbo()

});