Parse.initialize("1lRkVkAfr6Daum7wITXFrFyk8GlCbBwx8soPwnAR", "PzbJSDOdw0ZlMHWj5x9umDB4XgqsPenbWxZrxooy");


function value()
{
var currentUser = Parse.User.current();
if (currentUser) {
    // do stuff with the user
	console.log("success");
	console.log(Parse.User.current().id);
	alogi();
	var retrieve= Parse.Object.extend("resumedb");
var query = new Parse.Query(retrieve);
query.equalTo("username", Parse.User.current().id);
query.first({
  success: function(object) {
    // The object was retrieved successfully.
	if (object) {
		var name1 = object.get("name");
		var email = object.get("email");
		var contact = object.get("contact");
		var technical = object.get("technical");
		var edu=new Object();
		var extra=new Object();
		var intern=new Object();
		var project=new Object();
		var edu=object.get("education");
		var extra=object.get("extra");
		var intern=object.get("internships");
		var project=object.get("projects");
		console.log(email);
		console.log(contact);
		console.log(technical);
		console.log(edu);
		console.log(extra);
		console.log(intern);
		console.log(project);
		document.myform.name1.value=name1;
		document.myform.email.value=email;
		document.myform.contact.value=contact;
		document.myform.course0.value=edu[0].course;
		document.myform.college0.value=edu[0].college;
		document.myform.board0.value=edu[0].board;
		document.myform.percent0.value=edu[0].percent;
		document.myform.pyear0.value=edu[0].pyear;
		document.myform.course1.value=edu[1].course;
		document.myform.college1.value=edu[1].college;
		document.myform.board1.value=edu[1].board;
		document.myform.percent1.value=edu[1].percent;
		document.myform.pyear1.value=edu[1].pyear;
		document.myform.course2.value=edu[2].course;
		document.myform.college2.value=edu[2].college;
		document.myform.board2.value=edu[2].board;
		document.myform.percent2.value=edu[2].percent;
		document.myform.pyear2.value=edu[2].pyear;
		document.myform.event0.value=extra[0].event;
		document.myform.place0.value=extra[0].place;
		document.myform.extrarole0.value=extra[0].exrarole;
		
	    document.myform.company0.value=intern[0].company;
		document.myform.duration0.value=intern[0].duration;
		document.myform.role0.value=intern[0].role;
        document.myform.technical.value=technical;
		document.myform.title0.value=project[0].title;
		document.myform.technology0.value=project[0].technology;
		document.myform.description0.value=project[0].description;
		document.myform.title1.value=project[1].title;
		document.myform.technology1.value=project[1].technology;
		document.myform.description1.value=project[1].description;
		document.myform.title2.value=project[2].title;
		document.myform.technology2.value=project[2].technology;
		document.myform.description2.value=project[2].description;
		 
		document.myform.event1.value=extra[1].event;
		document.myform.place1.value=extra[1].place;
		document.myform.extrarole1.value=extra[1].exrarole;
		document.myform.event2.value=extra[2].event;
		document.myform.place2.value=extra[2].place;
		document.myform.extrarole2.value=extra[2].exrarole;
		console.log(name);
	}
  },
  error: function(object, error) {
    console.log("The object was not retrieved successfully.");
    // error is a Parse.Error with an error code and message.
  }
});	
}
 else {
    // show the signup or login page
	console.log("fail");
	$( "html" ).removeClass( "loading" );
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
	console.log(Parse.User.current().id);
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