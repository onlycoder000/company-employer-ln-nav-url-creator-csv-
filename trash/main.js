function fn_btn(){
    document.querySelector('div[class^="FindAllButton__ButtonContainer"] button').click();
    var tm=window.setTimeout(()=>{
       nxt_btn();
    },16000);
}
function nxt_btn(){
    document.querySelector('#PageActionsContainer button:nth-child(3)').click();
    var tm=window.setTimeout(()=>{
       fn_btn();
    },7000);
}
fn_btn()
