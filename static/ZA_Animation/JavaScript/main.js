
(function(){
$("#top-carousel-carousel>div").toArray().forEach((element,index) => {
    $(element).on("mouseover",function(){
        $('#top-carousel').carousel(index)
    })
});
    Vue.use(VueLazyload)
    console.log('vue')
// Vue.use(VueLazyload)
// var week = [0,0,0,0,0,0,0]
// var date = new Date().getDay()
// week[date-1]=1
// for(let i=0;$("#timetablelist>li").length>i;i++){
//     if(i!==date-1){
//         $($("#timetablelist>li")[i]).on('click',()=>{
//             if(week[i]===0){
//                 week[i]=1
//                 sendajax(i+1)
//             }
//         })
//     }
// }
// // var week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Sunday","Saturday"]
//
//
// $(`#timetablelist li:eq(${date-1}) a`).tab('show')
// function sendajax(date){
//     this.date = date
//     $.ajax({
//         type: "get",
//         url: "/timetable",
//         data: date,
//         processData: false,    //false
//         cache: false,    //缓存
//         beforeSend:function(){
//
//         },
//         success: function(data){
//             ajaxsuccess(data)
//         },
//         error:function(){
//             ajaxerror(data,date)
//         },
//         complete:function(){
//
//         }
//     })
// }
// function ajaxerror(data,date){
//     if(week[date-1]!==2){
//         week[date-1]=2
//     $(`.timetable>div>div:nth-child(${date})>ul`).append(`<p>加载失败，点击重新加载。</p>`)
//     $(`.timetable>div>div:nth-child(${date})>ul>p`).on('click',()=>{
//         sendajax(date)
//     })
// }
// }
//
//
// data={
//     rmxf:[{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'},{title:'revisions',num:'12',img:'Images/time.jpg'}],
// }
//





})()