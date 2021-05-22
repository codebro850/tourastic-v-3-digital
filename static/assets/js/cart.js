var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
			var passengers=document.getElementById('adult').value
			var child=document.getElementById('child').value
			var infants=document.getElementById('infants').value
			var days=document.getElementById('tour-days').value
			var date_of_tour=document.getElementById('traveldate12').value

        
		console.log('productId:', productId, 'Action:', action)
		if(passengers=="")
		 passengers=1
		if(child=="")
			 child=0
		
		  if(infants=="")
			infants=0
		
         if(date_of_tour=="")
			 date_of_tour="1990/01/01"
		
         if(days=="")  
		      days=4
		
			
		if (user == 'AnonymousUser'){
			addCookieItem(productId,passengers,child,infants,days,date_of_tour,action)
		}else{
			updateUserOrder(productId,passengers,child,infants,days,date_of_tour,action)
		}
	})
}

function updateUserOrder(productId,passengers,child,infants,days,date_of_tour,action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId,'passengers':passengers,'child':child,'infants':infants,'date_of_tour':date_of_tour, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(productId,passengers,child,infants,days,date_of_tour,action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'passengers':1}
		console.log("ye glti ho rhi hti br br")

		}
        else{
            if(cart[productId]==null){
			cart[productId]['passengers'] = passengers
			}
			else{
				cart[productId]['passengers']+= passengers

			}
		}
	}

	if (action == 'remove'){
        delete cart[productId];
		console.log('Item should be deleted')

	}
   
	// console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	
	location.reload()
}