const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#message').slideUp();
}, 3000);
