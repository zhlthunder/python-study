/**
 * Created by lin on 2017/7/30.
 */

//��һ�뷨�����ǿ��ܻᰴ������ķ�����д����ͨ�����Ƕ�д���Զ��庯������ʽ��
//jQuery.extend({
//      checktt: function() {
//        return "checking";
//      },
//      checktt2: function() {
//        return "checking2";
//      }
//    });


//���շ�����д����ִ�к�������ʽ��ͨ�õ�д��������ķ������ԣ�
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