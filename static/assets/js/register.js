
  var username_state = false;
  var email_state = false;
  function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(!regex.test(email)) {
        
      return false;
    }else{
        console.log("checing yes email")
      return true;
    }
  }
function register(){
    email = document.getElementById("modalLRInput10").value;
    password = document.getElementById("modalLRInput11").value;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $("#errorlogin").html("");
    $.ajax({
        type:"POST",
        url:'/login/',
        data:{
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'email':email,
            'password':password,
        },
        success : function(data){
            console.log(data);
            if(data['message'] == "Success"){
                location.reload();
            }
            else if(data['message'] == "inactive"){
                $("#errorlogin").html("Please verify this E-mail address.");
            }
            else{
                $("#errorlogin").html("The E-mail and Password do not match.");
            }
        },
        error: function(){
            $("#errorlogin").html("already logged in!!");
            location.reload();
         }
    });
}

function signup(){
    console.log("error done");
    username = document.getElementById("username").value;
    email=document.getElementById("emailadd").value;
    fname = document.getElementById("firstname").value;
    lname = document.getElementById("lastname").value;
    password1 = document.getElementById("password").value;
    password2 = document.getElementById("repeat-password").value;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $("#erroremail").html("");
    $("#errorpass").html("");
    $('#errorusername').html("");
    $('#name').html("");
    if(password1 == "" || password2 == ""){
        $("#errorpass").html("password must match");
    }
     if(password1!=password2){
        $("#errorpass").html("password must match");
    }
    if(fname==""){
        $('#name').html("please wright first name");
    }
if(password1==password2){
    if(fname!=""){
  if(IsEmail(email)){ 
    console.log("emilkfj ")
      $.ajax({
    type:"POST",
    url:'/signup/',
    data:{
        'csrfmiddlewaretoken': csrfmiddlewaretoken,
      'first_name':fname,
      'last_name':lname,
      "email":email,
      'username':username,
      'password1':password1,
    },
    success : function(data){
        console.log(data['message']);
        if(data['message'] == "Success"){
            location.reload();  
            // $('#acccountinfo').get(0).click();  
        }
        
            else if( data['message']=="Username exists please try another username")
                $("#errorusername").html("Username exists please try another username");
            else if(data['message']=="email exists")
            $("#erroremail").html("email exists please try another email");
                      
           else  
                  $("#errorsignup").html("something went wrong! please try again!");
           
        
    },
    error: function(){
        $("#errorsignup").html("already logged in!!");
        location.reload();
     }
    
});
    }
    else{
        $('#email').siblings("span").css({"color":"red"});
            $('#email').siblings("span").text('Please check the email ones!');
            $('#email').parent().removeClass("form_success");
            $('#email').parent().addClass("form_error");
    }
}
}
}

// $('#savinginfo').on('click', function(e){
//     e.preventDefault();
//     console.log("clicked")
//     address = document.getElementById("address1").value;
//     zipcode=document.getElementById("zipcode").value;
//      city= document.getElementById("City").value;
//     state = document.getElementById("State").value;
//     country = document.getElementById("Country").value;
//     mobile = document.getElementById("mobile").value;
//     csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
//     check=mobilenocheck(mobile);
//     $("#number").html("");
//     $("#address12").html(""); 
//     checkzip=zipcheck(zipcode);
//     if(mobile=="")
//     { 
//         $("#number").html("Please enter a valid number!!");

//     }
//     if(check){
//         console.log("number checked")
//        if(checkzip)
//        {
//            console.log("zip checked")
//            if(city==""||country==""||state=="")
//            {
//             $("#address12").html("please complete the address details!"); 
//            }
//            else{
//             $.ajax({
//                 type:"POST",
//                 url:'/address-save/',
//                 data:{
//                     'csrfmiddlewaretoken': csrfmiddlewaretoken,
//                     'mobile':mobile,
//                     'country':country,
//                     'city':city,
//                     'zipcode':zipcode,
//                     'address':address,
//                     'state':state,
                    
//                 },
//                 success : function(data){
//                    if(data['message']['sucess']=="success"){
//                      location.reload();
//                    }
//                    else {
//                         $("#address12").html("Some error occurred Please Try again Later!!");
//                     }
//                 }
        
        
//             });





//            }


//        }
//     }

        



//   });

  function mobilenocheck(mobNum){

    $("#number").html("");

    var filter = /^\d*(?:\.\d{1,2})?$/;
         if(mobNum!=""){
          if (filter.test(mobNum)) {
            if(mobNum.length==10){
            return true;
             } else {
                $('#mobile1').parent().removeClass();
                $('#mobile1').parent().addClass("form_error");
                $('#mobile1').siblings("span").text('Please enter a valid mobile number');
                return false;
              }
            }
            else {
                $('#mobile1').parent().removeClass();
                            $('#mobile1').parent().addClass("form_error");
                            $('#mobile1').siblings("span").text('Please enter a valid mobile number');
              return false;
           }}
           else{
               return true;
           }
    
  }
  function zipcheck(mobNum){

    $("#zip").html("");
            if(mobNum.length==6){
            return true;
             } else {
                $('#zipcode1').parent().removeClass();
                $('#zipcode1').parent().addClass("form_error");
                $('#zipcode1').siblings("span").text('Please enter a valid postal code');
                return false;
              }
            }

          
            $('#check_username').on('blur', function(){
                username=document.getElementById("check_username").value;
             usernamechecked(username);
            });

            function usernamechecked(username){ 
                

                csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
                if (username == '') {
                    username_state = false;
                    $('#check_username').siblings("span").css({"color":"red"});
                    $('#check_username').siblings("span").text('please enter the username!');
                    $('#check_username').parent().removeClass();
                    $('#check_username').parent().removeClass("from_success");
                            $('#check_username').parent().addClass("form_error");
                          
                    return ;
                }
                else{
                    $.ajax({
                        type:"POST",
                        url:'/username-check/',
                        data:{
                            'csrfmiddlewaretoken': csrfmiddlewaretoken,
                            'username':username,
                            
                        },
                        success : function(data){
                           if(data['message']=="success"){
                   
                   $('#check_username').siblings("span").css({"color":"green"});
                            $('#check_username').siblings("span").text('Saved');
                            $('#check_username').parent().removeClass("form_error");
                            $('#check_username').parent().addClass("form_success");
                          
                            username_state = true;
                            // return true;
                           }
                           if ((data['message']=="taken")){
                            username_state = false;
                            // $('#check_username').siblings("span").removeClass("color-green");
                            $('#check_username').siblings("span").css({"color":"red"});
                            $('#check_username').siblings("span").text('Sorry... Username already taken');
                            $('#check_username').parent().removeClass();
                            $('#check_username').parent().removeClass("from_success");
                            $('#check_username').parent().addClass("form_error");
                           
                            // return false;  
                        }

                        }

                
                
                    });
        

                }
             }

            $('#email1').on('blur', function(){
                email=document.getElementById("email1").value;
     emailchecked(email);
            });
            function emailchecked(email) {
                console.log("coming");
                csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
                if (email=='') {
                    email_state=false;
                    // $('#email1').siblings("span").removeClass("color-green");
                    $('#email1').siblings("span").css({"color":"red"});
                    $('#email1').siblings("span").text('please enter the email!');
                    $('#email1').parent().removeClass();
                            $('#email1').parent().addClass("form_error");
                          
                    return ;
                }
                else{
                  if(IsEmail(email)) { $.ajax({
                        type:"POST",
                        url:'/email-check/',
                        data:{
                            'csrfmiddlewaretoken': csrfmiddlewaretoken,
                            'email':email,
                            
                        },
                        success : function(data){
                           if(data['message']=="success"){
                        email_state = true;
                        // $('#email1').siblings("span").removeClass("color-red");
                        // $('#email1').siblings("span").addClass("color-green");
                        $('#email1').siblings("span").css({"color":"green"});
                        $('#email1').siblings("span").text('saved');
                        $('#email1').parent().removeClass("form_error");
                        $('#email1').parent().addClass("form_success");
                            
                           }
                           if ((data['message']=="taken")){
                            email_state = false;
                            // $('#email1').siblings("span").removeClass("color-green");
                            // $('#email1').siblings("span").addClass("color-red");
                            $('#email1').siblings("span").css({"color":"red"});
                            $('#email1').siblings("span").text('Sorry... email already taken');
                            $('#email1').parent().removeClass("form_success");
                            $('#email1').parent().addClass("form_error");
                          
                            // return false;
                        }

                        }

                
                
                    });
        }
        else{
            $('#email1').siblings("span").css({"color":"red"});
            $('#email1').siblings("span").text('Please check the email ones!');
            $('#email1').parent().removeClass("form_success");
            $('#email1').parent().addClass("form_error");
          
        }

                }

              }

          city_check=true;
          country_check=true;
          state_check=true;
          first_name_check=true; 
$("#editinfo").on('click',function(e){
    e.preventDefault();
    first_name=document.getElementById("first-name").value;
    last_name=document.getElementById("last-name").value;
    address = document.getElementById("address").value;
    zipcode=document.getElementById("zipcode1").value;
     city= document.getElementById("city").value;
    state = document.getElementById("state").value;
    country = document.getElementById("country").value;
    username=document.getElementById("check_username").value;
    mobile = document.getElementById("mobile1").value;
    email=document.getElementById("email1").value;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    check=mobilenocheck(mobile);
    checkzip=zipcheck(zipcode);
   
    
    if(check){
        console.log("number checked")
       if(checkzip)
       {
           console.log("zip checked")
           if(city=="" || country=="" ||state==""||first_name=="")
           {
               if(city==""){
            $('#city').parent().removeClass();
            $('#city').parent().addClass("form_error");
            $('#city').siblings("span").text('please enter the city!');
             city_check=false;
               }
            if(country=="")
            {$('#country').parent().removeClass();
            $('#country').parent().addClass("form_error");
            $('#country').siblings("span").text('please enter the country!');
            country_check=false;
            }
            if(state=="")
            {$('#state').parent().removeClass();
            $('#state').parent().addClass("form_error");
            $('#state').siblings("span").text('please enter the state!');
 
           state_check=false;
            }
            if(first_name==""){
                $('#first-name').parent().removeClass();
            $('#first-name').parent().addClass("form_error");
            $('#first-name').siblings("span").text('please enter the first name!');
            first_name_check=false;    
        }
        
        }
        console.log("city_check:"+city_check+"city:"+city);
        console.log("country_check"+country_check+"country:" +country);
        console.log("fisrt_name:"+first_name+"check:"+first_name_check);
        console.log("state:"+state+"check:"+state_check);
        console.log("email_checked:"+email_state+"username:"+username);
        console.log("username:"+username_state+"email:"+email);
        if( city_check && country_check )
        {if(first_name_check && state_check){

        
        console.log("posting request");
            $.ajax({
                type:"POST",
                url:'/address-save/',
                data:{
                    'csrfmiddlewaretoken': csrfmiddlewaretoken,
                    'mobile':mobile,
                    'country':country,
                    'city':city,
                    'zipcode':zipcode,
                    'address':address,
                    'first_name':first_name,
                    'last_name':last_name,
                    'username':username,
                    'state':state,
                    'email':email,
                    'username':username,
                    
                },
                success : function(data){
                   if(data['message']=="success"){
                    
                     location.reload();
                     $("#success").html("profile is updated successfully")
                     
                   }
                   else {
                        $("#address12").html("Some error occurred Please Try again Later!!");
                    }
                }
        
        
            });

           

        
    }
}
}
    }

});  
promo_state=false;

$('#promocode').on('blur', function(){
    promocode=document.getElementById("promocode").value;
    titli=$('#productid').text();
 promocodecheck(promocode,titli);
});

function promocodecheck(promocode,title){
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    if(promocode!=""){
    $.ajax({
        type:"POST",
        url:'/promo-check/',
        data:{
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'promocode':promocode,
            'title':title,
            
        },
        success : function(data){
            console.log(data);
           if(data['message']=="success"){
        promo_state = true;
        // $('#email1').siblings("span").removeClass("color-red");
        // $('#email1').siblings("span").addClass("color-green");
        $('#promocode').siblings("span").css({"color":"green"});
        $('#promocode').siblings("span").text(promocode+"    "+data['discount']+"% applied");
        $('#promocode').parent().removeClass();
        $('#promocode').parent().removeClass("form_error");
        $('#promocode').parent().addClass("form_success");
            
           }
           if ((data['message']=="Invalid promocode")){
            promo_state = false;
            // $('#email1').siblings("span").removeClass("color-green");
            // $('#email1').siblings("span").addClass("color-red");
            $('#promocode').siblings("span").css({"color":"red"});
            $('#promocode').siblings("span").text('promocode did not exists');
            $('#promocode').parent().removeClass("form_success");
            $('#promocode').parent().addClass("form_error");
          
            // return false;
        }
        if(data['message']=="you are not eligible for this promocode"){
           
            promo_state = false;
            // $('#email1').siblings("span").removeClass("color-green");
            // $('#email1').siblings("span").addClass("color-red");
            $('#promocode').siblings("span").css({"color":"red"});
            $('#promocode').siblings("span").text(data['message']);
            $('#promocode').parent().removeClass("form_success");
            $('#promocode').parent().addClass("form_error");
        }
        if(data['message']=="this package is not eligible for this"){
              // $('#email1').siblings("span").addClass("color-red");
              $('#promocode').siblings("span").css({"color":"red"});
              $('#promocode').siblings("span").text(data['message']);
              $('#promocode').parent().removeClass("form_success");
              $('#promocode').parent().addClass("form_error");
        }

        }
    


    });

    }
}