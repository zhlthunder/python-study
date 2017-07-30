/**
 * Created by lin on 2017/7/30.
 */


//单行的进入编辑模式和退出编辑模式， 通过帮忙click事件的方式实现；
$(function(){
    BindSingleCheck('#edit_mode','#tb1');
})

function BindSingleCheck(mode,tb){
    $(tb).find(":checkbox").bind('click',function(){
        var _tr=$(this).parent().parent();
        if($(mode).hasClass('editing')){
            if($(this).prop('checked')){
                RowIntoEdit(_tr);
            }else{
                RowOutEdit(_tr);
            }
        }
    })
}



function CreateSelect(attrs,csses,option_dict,item_key,item_value,current_val){
   var sel=document.createElement('select');
   $.each(attrs,function(k,v){
   $(sel).attr(k,v);
    });
   $.each(csses,function(k,v){
    $(sel).css(k,v);
   });
  //console.log(sel);

   $.each(option_dict,function(k,v){
   var optl=document.createElement('option');
   var sel_text=v[item_value];
   var sel_value=v[item_key];

   if(sel_value==current_val){
   $(optl).text(sel_text).attr('value',sel_value).attr('text',sel_text).attr('selected','selected');
   }else{
   $(optl).text(sel_text).attr('value',sel_value).attr('text',sel_text);
   };
    $(sel).append(optl);

   });
    return sel;
}




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
                check_box.prop('checked',true);
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
                check_box.prop('checked',false);
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
                check_box.prop('checked',false);
                RowOutEdit(tr);
            }else{
                //让没有进入编辑行模式的行进入编辑模式
                check_box.prop('checked',true);
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

//定义全局变量的数据源
STATUS=[
{'id':1,'value':"online"},
{'id':2,'value':"offline"}
];


function RowIntoEdit(xtr){
    xtr.children().each(function(){
        if($(this).attr('edit')=="true"){
            if($(this).attr('edit-type')=="select"){

               var select_val=$(this).attr('sel-val');
               var global_key=$(this).attr('global-key');

                //创建select标签的内置方法
                //window[global_key] 为访问全局变量的固定方法
                // "onchange":"MultiSelect(this);"  为select绑定了一个修改事件
               var select_tag=CreateSelect({"onchange":"MultiSelect(this);"},{},window[global_key],'id','value',select_val);
               //经过上面的命令，产生的select标签的样式如下：
               // <select onchange="MultiSelect(this);">
               //    <option value='1' selected='selected'>在线</option>
               //    <option value='2'>下线</option>
               // </select>

                //console.log(select_tag);
                $(this).html(select_tag);
            }else{
                var orgin_value=$(this).text();
                var temp="<input value='"+orgin_value+"' />";
                //替换掉当前td中的所有内容
                $(this).html(temp);
            }
        }
    })
}



function EditMode(ths){
    if($(ths).hasClass('editing')){
        $(ths).removeClass('editing');
        $(ths).css('background-color','#a9a3a3');
    }else{
    $(ths).addClass('editing');
     $(ths).css('background-color','red');
        }
}

function RowOutEdit(xtr){
    xtr.children().each(function(){
        if($(this).attr('edit')=="true"){
            if($(this).attr('edit-type')=="select"){

                var ttt=$(this).attr('sel-val');
                //console.log(ttt);
                $.each(STATUS,function(k,v){
                    if(v.id==ttt){
                        sel_val= v.value;
                    };
                });

                $(this).text(sel_val);
            }else{
                var tt=$(this).children().val();

                $(this).text(tt);
            }
        }
    })
}