// $(function () {
//     $('img').each(function () {
//
//         // console.log(1)
//         //获取当前的图片路径src属性
//         var img_path =$(this).attr('src')
//        // console.log(img_path)
//         //字符串拼接
//         img_path ="{% static '" +img_path + "'%}"
//        // console.log(img_path)
//
//         //设置对应原素的src
//         $(this).attr('src',img_path)
//
//
//     })
//      //输出bofy >>复制 >>替换掉原有的body的内容 >>删除该脚步
//     console.log($('body').html())
// })