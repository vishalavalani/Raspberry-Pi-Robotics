
var username = "";
var password = "";
$(document).ready(function(){
	username = getCookie("username");
	password = getCookie("password");
	if (username != "") {
        toastr.success("Welcome again " + username);
    } else {
        location.href = "login.html";
    }
	var width = $( window ).width();
	var height = $( window ).height();
	
	if(width < 640){
		$("#streamimg").width(width - 60);
	}
});

function LedOn(){
	CallControlApi("lighton");
}
function LedOff(){
	CallControlApi("lightoff");
}
function Forward(){
	CallControlApi("forward");
}
function Left(){
	CallControlApi("left");
}
function Brake(){
	CallControlApi("brake");
}
function Right(){
	CallControlApi("right");
}
function Reverse(){
	CallControlApi("reverse");
}
function FrontSensor(){
	$.ajax({
			type: "GET",
			url: baseuri + "/api/" + "frontsensor",
			dataType: "json",
			headers: {
				"Authorization": "Basic " + btoa(username + ":" + password)
			},
			success: function (data){
					$("#response").prepend(JSON.stringify(data) + '</br>');
					toastr.success(data.reading + " cms", 'IOT Robot Sensor');
			},
			error: function(xhr, status, error) {
				toastr.error("Status: " + status + " Error: " + error, "Oops!");
			}
	});
}

function AllSideSensor(){
	$.ajax({
			type: "GET",
			url: baseuri + "/api/" + "detailsensorreadings",
			dataType: "json",
			headers: {
				"Authorization": "Basic " + btoa(username + ":" + password)
			},
			success: function (data){
				$("#response").prepend(JSON.stringify(data) + '</br>');
				toastr.success("Left: " + data.detailsensorreadings[0] + " cms,"
					+ "Left1: " + data.detailsensorreadings[1] + " cms,"
					+ "Straight: " + data.detailsensorreadings[2] + " cms,"
					+ "Right1: " + data.detailsensorreadings[2] + " cms,"
					+ "Right: " + data.detailsensorreadings[3] + " cms"
				, 'IOT Robot Sensor');
			},
			error: function(xhr, status, error) {
				toastr.error("Status: " + status + " Error: " + error, "Oops!")
			}
	});
}


function CallControlApi(control){
	$.ajax({
		type: "GET",
		url: baseuri + "/api/" + control,
		dataType: "json",
		headers: {
			"Authorization": "Basic " + btoa(username + ":" + password)
		},
		success: function (data){
			$("#response").prepend(JSON.stringify(data) + '</br>');
			var msg = '';
			if(control == "lighton"){
				msg = 'LED 37 is On';
			}
			else if(control == 'lightoff'){
				msg = 'LED 37 is Off';
			}
			else if(control == 'brake'){
				msg = 'I am resting now!';
			}
			else{
				msg = 'I am moving ' + control;
			}
			toastr.success(msg, 'IOT Robot');
	    },
		error: function(xhr, status, error) {
			toastr.error('Error in calling: ' + control + " Status: " + status + " Error: " + error, "Oops!")
		}
	});

	
}