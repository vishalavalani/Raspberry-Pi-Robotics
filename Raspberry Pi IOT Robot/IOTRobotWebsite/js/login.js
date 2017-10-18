function LoginClicked(){
	var username = $("#inputUsername").val();
	var password = $("#inputPassword").val();
	
	$.ajax({
			type: "POST",
			url: baseuri + "/api/" + "login",
			dataType: "json",
			headers: {
				"Authorization": "Basic " + btoa(username + ":" + password)
			},
			success: function (data	){
				setCookie("username",username,1);
				setCookie("password",password,1);
				location.href = "dashboard.html";
				toastr.success("Login Successful", 'IOT Robot Sensor');
			},
			error: function(xhr, status, error) {
				if(error == "UNAUTHORIZED")
				{
					toastr.error("Username/Password incorrect");
				}
				else
				{
					toastr.error("Status: " + status + " Error: " + error, "Oops!");
				}
			}
	});
}