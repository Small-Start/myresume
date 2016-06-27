function log() {
	serializedData = $('#login').serialize();
	$.ajax({
		url :'/account/login/',
		type : 'post',
		data : serializedData,
		success : function(response) {
			if (response.status == 'sucess') {
				window.location.href = "/"
			}
			else{
				var error = ""
				for (key in response){
					if (key == "error"){
						error += response[key] + "\n"
					}
					else if (key != "status"){
						error += String(response[key]).replace('This',key) + "\n"
					}
				}
				alert (error)
			}
		},
		error : function(xhr, errmsg, err){
			console.log(xhr.responseText)
		}
	})
}

function signup() {
	serializedData = $("#signup").serialize();
	$.ajax({
		url : '/account/login/',
		type : 'post',
		data : serializedData,
		success : function(response) {
			if (response.status == "sucess"){
				window.location.href="/";
			}
			else {
				var error = ""
				for (key in response){
					if (key == "error" || key == "__all__"){
						error += response[key] + "\n"
					}
					else if (key != "status"){
						error += String(response[key]).replace('This',key) + "\n"
					}
				}
				alert (error)
			}
		},
		error : function(xhr,errmsg,err) {
			console.log(xhr.responseText);
		}

	})
}
