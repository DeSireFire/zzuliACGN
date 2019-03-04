(function(){
    function xxx(){
        if(localStorage.getItem('userKnow')){
            $('.popwindow').css({display:'none'})
        }
    }
    $('.btn-agree').on('click',()=>{
    let temp = []
    $("input[name='windowpopname']").each(function(index,e){
        temp.push($(e).prop('checked'))
    })
    if(temp[0]){
        localStorage.setItem('userKnow', 'true');
        let cat = localStorage.getItem('userKnow');
        console.log(cat)
    }
    if(temp[1]){
        $('.popwindow').css({display:'none'})
    }else{
        alert('请同意！')
    }
    })
    xxx()
})()