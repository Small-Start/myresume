Parse.initialize("1lRkVkAfr6Daum7wITXFrFyk8GlCbBwx8soPwnAR", "PzbJSDOdw0ZlMHWj5x9umDB4XgqsPenbWxZrxooy");
var currentUser = Parse.User.current();
if (currentUser) {
	console.log("success");
    // do stuff with the user
} else {
    // show the signup or login page
	console.log("Errorrr");
}



function signu(){
var user = new Parse.User();
user.set("username", $("#uname").val());
user.set("password", $("#password1").val());
user.set("email", $("#email1").val());
user.signUp(null, {
  success: function(user) {
  
  alert("You are succesfull signed up");
   
  
  
  },
  error: function(user, error) {
    // Show the error message somewhere and let the user try again.
    alert("Error: " + error.code + " " + error.message);
  }
});
};
