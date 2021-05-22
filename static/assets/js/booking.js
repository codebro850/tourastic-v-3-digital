// var updateBtns = document.getElementById('openbook')

$('div .removeWrap #openbook').on('click',function(e){
   console.log("gmkgkgj")
    var productId = this.dataset.product
    $('#productid').text(productId);

});