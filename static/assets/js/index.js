function emailsent1(){

    var text = document.getElementById("sendemaillink");
     var email=document.getElementById("validationDefault03").value;
     csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
     $("#checkemail").html("");
     if(email==""){
        $("#checkemail").html("please enter email first!!");
     }
     else if(isValidEmailAddress(email)){
         
        $("#checkemail").html("sending..............");
            $.ajax({
                type:"POST",
                url:'/password_reset_request/',
                data:{
                    'csrfmiddlewaretoken': csrfmiddlewaretoken,
                    'email':email,
                },
                success : function(data){
                    if(data['message'] == "Success"){
                        $("#checkemail").html("please check your email");
                        var check = document.getElementById("checkemail");
                        text .innerHTML = "Email send";
                                            }
                    else if(data['message'] == "inactive"){
                        $("#checkemail").html("your accounts seems to be Inactive!");
                    }
                    else{
                        $("#checkemail").html("please try again !");
                    }
                }
            });
        }
            else{
                $("#checkemail").html("pease wright correct email!");
            }
          
    
     

   
}
function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
    return pattern.test(emailAddress);
}
function sendmail(){
 var name=document.getElementById("name").value;
 var email=document.getElementById("email-add").value;
 var subject=document.getElementById("subject").value;
 var message=document.getElementById("message").value;
 csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;


 if(email==""){
    $("#status").html("please enter email first!!");
 }
 else if(name==""){
    $("#status").html("please enter name first!!");
 }
 else if(subject==""){
    $("#status").html("please enter appropriate subject first!!");
 }
 else if(message==""){
    $("#status").html("please enter message first!!");
 }
 else {
     if (isValidEmailAddress(email)){
        $.ajax({
            type:"POST",
            url:'/messagesend/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'email':email,
                'subject':subject,
                'message':message,
                'name':name,
            },
            success : function(data){
                console.log(data);
                if(data['message'] == "Success"){
                    $("#status").html("your message is recorded succesfuly we will contact you shortly!");
                    var check = document.getElementById("checkemail");
                    check.innerHTML = "Check Your Email...";
                                        }
                else if(data['message'] == "inactive"){
                    $("#status").html("your accounts seems to be Inactive!");
                }
                else{
                    $("#status").html("please try again !");
                }
            }
        });
      

 }
 else{
    $("#status").html("please enter a valid email address");
 }
}
 

}