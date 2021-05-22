function changecurr(value){ 
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax({
        type:"POST",
        url:'/changecurr/',
        data:{
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'curr':value,
            
        },
        success : function(data){
           if(data['message']=="Success"){
               console.log("sucess");
            location.reload();
           }
           else if(data['message']=='error'){
               alert("Something went wrong please try again!");
              
        }
    }


    });


 }