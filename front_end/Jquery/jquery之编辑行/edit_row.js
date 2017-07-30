/**
 * Created by lin on 2017/7/30.
 */


//���еĽ���༭ģʽ���˳��༭ģʽ�� ͨ����æclick�¼��ķ�ʽʵ�֣�
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
        //�����е��д���ɱ༭ģʽ
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                //�����Ѿ�����༭��ģʽ�У���Ĭ�ϲ�����Ϳ�����
            }else{
                //��û�н���༭��ģʽ���н���༭ģʽ
                check_box.prop('checked',true);
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
                check_box.prop('checked',false);
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
                check_box.prop('checked',false);
                RowOutEdit(tr);
            }else{
                //��û�н���༭��ģʽ���н���༭ģʽ
                check_box.prop('checked',true);
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

//����ȫ�ֱ���������Դ
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

                //����select��ǩ�����÷���
                //window[global_key] Ϊ����ȫ�ֱ����Ĺ̶�����
                // "onchange":"MultiSelect(this);"  Ϊselect����һ���޸��¼�
               var select_tag=CreateSelect({"onchange":"MultiSelect(this);"},{},window[global_key],'id','value',select_val);
               //������������������select��ǩ����ʽ���£�
               // <select onchange="MultiSelect(this);">
               //    <option value='1' selected='selected'>����</option>
               //    <option value='2'>����</option>
               // </select>

                //console.log(select_tag);
                $(this).html(select_tag);
            }else{
                var orgin_value=$(this).text();
                var temp="<input value='"+orgin_value+"' />";
                //�滻����ǰtd�е���������
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