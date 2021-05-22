$(function(){
    var dtToday = new Date();
    
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
    
    var maxDate = year + '-' + month + '-' + day;

    // or instead:
    // var maxDate = dtToday.toISOString().substr(0, 10);
    $('#traveldate12').attr('min', maxDate);
    $('#traveldate123').attr('min', maxDate);
});

$('#bookthepackage').on('click', function(e){
    e.preventDefault();
     titli=$('#productid').text();
     console.log(titli);
    // var user = "{{ request.user }}";
    // if (user == 'AnonymousUser')
    // {  
    //     console.log("user is not authenticated");
    // }
    // else{
        if(document.getElementById("traveldate12").value!=""){
     datetimeoftravel=document.getElementById("traveldate12").value;
        }
        else{
            console.log("plese enter someting in date")
        }
     adult = document.getElementById("adult").value;
     child = document.getElementById("child").value;
    infants = document.getElementById("infants").value;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    // console.log(adult);
    // console.log(child);
  
    // console.log(titli);
    


    if(adult==""){
        adult=0
        
    }
    if(child==""){
        child=0

    }
    if(infants==""){
        infants=0
    }
    
    if(datetimeoftravel!=""){
       if(adult!=0) {
    $("#daterequired").html("");
    $.ajax({
        type:"POST",
        url:'/book/'+titli,
        data:{
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'adult':adult,
            'child':child,
            'infants':infants,
            'dateoftravel':datetimeoftravel,
            
        },
        success : function(data){
           if(data['message']['sucess']=="success"){
             window.location.href =data['message']['url'] ; 
           }
           else if(data['message']=='login required'){
               
               $('#loginform234').get(0).click();

            }
            else if(data['message'] == "dateoftravel"){
                $("#daterequired").html("please enter the date of travel");
            }
            else if(data['message']=="date error"){
                $("#daterequired").html("Tour is not available at this date");
            }
            else {
                $("#daterequired").html("Some error occurred Please Try again Later!!");
            }
        }


    });
}
else{
    $("#daterequired").html("Please enter the passenger details first!");
}
}
else{
    $("#daterequired").html("please enter the date of journey first!");
}

}
);




$("#submitpassdetails").on("click",function(e){
    e.preventDefault();
    titli=$('#productid').text();
    email12 = document.getElementById("emaila").value;
    number12 = document.getElementById("mobile456").value;
   alternatemobile = document.getElementById("alternatemobile02").value;
   nam=[];
   ag=[];
   sex=[];
   nam_bool=[];
   ag_bool=[];
   sex_bool=[];
   leng=3;
   for(var i=1;i<=3;i++){
          
    fullname = document.getElementById("fullname"+i).value;
    age=document.getElementById("age"+i).value;
    gender=document.getElementById("gender"+i).value;
    if(fullname==""){
        $('#fullname'+i).parent().removeClass();
        $('#fullname'+i).parent().addClass("form_error");
        $('#fullname'+i).siblings("span").text('Please Enter the passenger Name!');
           
    } 
    else{
        nam.push(fullname);
        nam_bool[i]=true;

        
    }
    if(age=="")
    {
        $('#age'+i).parent().removeClass();
        $('#age'+i).parent().addClass("form_error");
        $('#age'+i).siblings("span").text('Please Enter the passenger Name!');
    }
    else{
        ag.push(age);
        ag_bool=true;
    }
    if(gender==""){
        $('#gender'+i).parent().removeClass();
        $('#gender'+i).parent().addClass("form_error");
        $('#gender'+i).siblings("span").text('Please Enter the passenger Name!');
    }
    else{
     sex.push(gender);
     sex_bool=true;
    }
   } 
   csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
   if(mobilenocheck(number12)){
       if(IsEmail(email12)){
        
           
        $.ajax({
        type:"POST",
        url:"/passengerdetail/"+titli,
        data:{
        'csrfmiddlewaretoken': csrfmiddlewaretoken,
        'number':number12,
        'email':email12,
        'alternate':alternatemobile,
        'pass_name':nam,
        'pass_age':ag,
        'pass_gender':sex,

        },
        success:function(data){
            if(data['message']=="success")
            {   
                window.location.href =data['url'] ; 
              }
             else if(data['message']=="error"){
                window.alert("Something went wrong please try again!!");
              }
              else if(data['message']=="empty"){
                  if(data['field']=="passenger_name"){
                    $('#fullname'+data['index']).parent().removeClass();
                    $('#fullname'+data['index']).parent().addClass("form_error");
                    $('#fullname'+data['index']).siblings("span").text('Please Enter the passenger Name!');
                  }
                  if(data['field']=="age"){
                    $('#age'+data['index']).parent().removeClass();
                    $('#age'+data['index']).parent().addClass("form_error");
                    $('#age'+data['index']).siblings("span").text('Please Enter the passenger Name!');
                  }
                  if(data['field']=="gender"){
                    $('#gender'+data['index']).parent().removeClass();
                    $('#gender'+data['index']).parent().addClass("form_error");
                    $('#gender'+data['index']).siblings("span").text('Please Enter the passenger Name!');
                  }
              }
         },
         error: function(){
             window.alert("something went wrong please try again!!"); 
          }
        
       



         });
        

        }
       
       else{
        $('#emailaddressss').parent().removeClass();
        $('#emailaddressss').parent().addClass("form_error");
        $('#emailaddressss').siblings("span").text('Please enter a valid Email Address');
       }
   }

});



function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(!regex.test(email)) {
        
      return false;
    }else{

      return true;
    }
  }
function mobilenocheck(mobNum){

    $("#number").html("");

    var filter = /^\d*(?:\.\d{1,2})?$/;
         if(mobNum!=""){
          if (filter.test(mobNum)) {
            if(mobNum.length==10){
            return true;
             } else {
                $('#mobile456').parent().removeClass();
                $('#mobile456').parent().addClass("form_error");
                $('#mobile456').siblings("span").text('Please enter a valid mobile number');
                return false;
              }
            }
            else {
                $('#mobile456').parent().removeClass();
                            $('#mobile1').parent().addClass("form_error");
                            $('#mobile1').siblings("span").text('Please enter a valid mobile number');
              return false;
           }
        }
           else{
               return true;
           }
    
  }


  function checkinputs(age,sex,nam,leng){
       for(var i=1;i<=leng;i++){
           if(age[i]==false || sex[i]==false || nam[i]==false){
             return i;
           }
           else{
               continue;
           }
       }
     return true;
  }