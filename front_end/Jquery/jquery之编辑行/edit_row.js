/**
 * Created by lin on 2017/7/30.
 */

function Selectall(mode,tb){
    if ($(mode).hasClass('editing')) {
        //将所有的行处理成编辑模式
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //对于已经进入编辑行模式行，就默认不处理就可以了
            }else{
                //让没有进入编辑行模式的行进入编辑模式
                check_box.prop('check',true);
                //让一行进入编辑模式的子函数
                RowIntoEdit(tr);
            }

        })
    } else
        {
            //只执行简单的选中的功能
            $(tb).find(':checkbox').prop('checked', true);
        }
    }

function deleteall(mode,tb){
    if ($(mode).hasClass('editing')) {
        //让所有的处于编辑模式的行退出编辑模式
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //对于已经进入编辑行模式的行，需要退出编辑模式
                check_box.prop('check',false);
                RowOutEdit(tr);
            }else{

            }

        })
    } else
        {
            //只执行简单的选中的功能
            $(tb).find(':checkbox').prop('checked', false);
        }
    }


function Reverse(mode,tb){
    if ($(mode).hasClass('editing')) {
        //将所有的行处理成编辑模式
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //对于已经进入编辑行模式的行，需要退出编辑模式
                check_box.prop('check',false);
                RowOutEdit(tr);
            }else{
                //让没有进入编辑行模式的行进入编辑模式
                check_box.prop('check',true);
                //让一行进入编辑模式的子函数
                RowIntoEdit(tr);

            }

        })
    } else
        {
            //只执行简单的选中的功能
            $('table :checkbox').each(function(){
                $(this).prop('checked',!$(this).prop('checked'))
            })

        }
    }





