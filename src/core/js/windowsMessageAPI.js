
var domain = 'http://scriptandstyle.com';
var myPopup = window.open(domain + '/windowPostMessageListener.html','myWindow');

//periodical message sender
setInterval(function(){
	var message = 'Hello!  The time is: ' + (new Date().getTime());
	console.log('blog.local:  sending message:  ' + message);
	myPopup.postMessage(message,domain); //send the message and target URI
},6000);

//listen to holla back
window.addEventListener('message',function(event) {
	//if(event.origin !== 'http://scriptandstyle.com') return;
	console.log('received response:  ',event.data);
},false);
