/**
 * Created by lin on 2017/7/30.
 */

function Selectall(mode,tb){
    if ($(mode).hasClass('editing')) {
        //�����е��д���ɱ༭ģʽ
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //�����Ѿ�����༭��ģʽ�У���Ĭ�ϲ�����Ϳ�����
            }else{
                //��û�н���༭��ģʽ���н���༭ģʽ
                check_box.prop('check',true);
                //��һ�н���༭ģʽ���Ӻ���
                RowIntoEdit(tr);
            }

        })
    } else
        {
            //ִֻ�м򵥵�ѡ�еĹ���
            $(tb).find(':checkbox').prop('checked', true);
        }
    }

function deleteall(mode,tb){
    if ($(mode).hasClass('editing')) {
        //�����еĴ��ڱ༭ģʽ�����˳��༭ģʽ
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //�����Ѿ�����༭��ģʽ���У���Ҫ�˳��༭ģʽ
                check_box.prop('check',false);
                RowOutEdit(tr);
            }else{

            }

        })
    } else
        {
            //ִֻ�м򵥵�ѡ�еĹ���
            $(tb).find(':checkbox').prop('checked', false);
        }
    }


function Reverse(mode,tb){
    if ($(mode).hasClass('editing')) {
        //�����е��д���ɱ༭ģʽ
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //�����Ѿ�����༭��ģʽ���У���Ҫ�˳��༭ģʽ
                check_box.prop('check',false);
                RowOutEdit(tr);
            }else{
                //��û�н���༭��ģʽ���н���༭ģʽ
                check_box.prop('check',true);
                //��һ�н���༭ģʽ���Ӻ���
                RowIntoEdit(tr);

            }

        })
    } else
        {
            //ִֻ�м򵥵�ѡ�еĹ���
            $('table :checkbox').each(function(){
                $(this).prop('checked',!$(this).prop('checked'))
            })

        }
    }





