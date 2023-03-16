
$(document).disbtn(function(){
    $("input[type='checkbox']").on("click",function(){
        let count = $("input:checked[type='checkbox']").length;
        console.log(count)
        if (count==0){
            //$(this).prop("checked",false);
            this.checked=false;
            alert("항목을 선택해주세요")
        }
    });


    $("button[type='submit']").click(function(){
    $("form").sumbit();
    })
});

// $(document).disbtn(function(){
//     $("form").submit(function(event){
//         let count = $("input:checked[type='checkbox']").val();
//         console.log(count)
//         if (count==None){
//             //$(this).prop("checked",false);
//             this.checked=false;
//             alert("항목을 선택해주세요")
//         }
//     });
// });