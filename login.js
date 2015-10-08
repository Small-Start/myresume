Parse.initialize("1lRkVkAfr6Daum7wITXFrFyk8GlCbBwx8soPwnAR", "PzbJSDOdw0ZlMHWj5x9umDB4XgqsPenbWxZrxooy");


function value()
{
var currentUser = Parse.User.current();
if (currentUser) {
    // do stuff with the user
	console.log("success");
	console.log(Parse.User.current().id);
	alogi();
}
 else {
    // show the signup or login page
	console.log("fail");
	
	alert("please login to continue");
	window.location.href="index.html";
	
 }	
	
}

						
function logo()
{  
var currentUser = Parse.User.current();
console.log(currentUser);  
	Parse.User.logOut();
	
	currentUser = Parse.User.current();
	console.log(currentUser);
	
	window.location.reload(true);
 
}




function alogi(){
	console.log("w2alogi");
	
	$("#username").val(Parse.User.current().get("username"));
}
function start(){
Parse.User.logIn($("#username").val(), $("#password").val(), {
  success: function(user) {
	console.log(Parse.User.current().get("username"));
	redirect();
	
	
  },
  error: function(user, error) {
    // The login failed. Check error to see why.
	 alert("Error: " + error.code + " " + error.message);
	document.getElementById("uname").value="";
	document.getElementById("pwd").value="";
    
  }
});
function redirect(){
window.location.href="resume.html";
console.log(Parse.User.current().get("username"));
}
function back()
{
window.location.href="index.html";	
}

}