/**
 * Created by lin on 2017/7/30.
 */

//第一想法，我们可能会按照下面的方法来写，但通常我们都写成自定义函数的形式；
//jQuery.extend({
//      checktt: function() {
//        return "checking";
//      },
//      checktt2: function() {
//        return "checking2";
//      }
//    });


//最终方法：写成自执行函数的形式，通用的写法，上面的方法忽略；
(function(arg){
   arg.extend({
      test: function() {
        return "testing";
      },
      test2: function() {
        return "testing2";
      }
    });
})(jQuery);