var has_rendered_car = false;

// Maps of names to items for acquiring resources, 
var pythonage_objects = {}

var canvas_context = null;
var key_listener = null;
var web_socket = null;

// shorthand to get an doc element by its id
function id(theid){
	return document.getElementById(theid);
}

// add to on screen log
function log(text){
	var div = document.createElement("div");
	div.innerHTML = text;
	id("log").appendChild(div);
}

// clear on screen log
function clearlog(){
	var s = id("log");
	while (s.firstChild) {
	    s.removeChild(s.firstChild);
	}
}

// error function - so you can hook in more error handling
function pythonage_error(message){
	//log(message);
}

function tick(){
	if(has_rendered_car == false && pythonage_objects['cardata'].loaded){
		log("trying to render");
		has_rendered_car = true;
		//pythonage_consume_nugget("(new-img,mycar,cardata,100,100,true)");
		//pythonage_consume_nugget("(new-tran,carposition,0,0,true)");
		//pythonage_consume_nugget("(append,mycar,carposition)");
		//pythonage_consume_nugget("(render,carposition)");
	}
}

function load(){
	key_listener = new keyboard_listener();
	
	var c = id("my_canvas");
	canvas_context = c.getContext("2d");
	
	web_socket = new MyWebSocket("localhost", "8765");
	web_socket.send("requestinggame,"+pythonage_game_name);
	
	//pythonage_consume_nugget("(new-imgd,cardata)");
	//pythonage_consume_nugget("(set-imgd-src,cardata,img/car_side1_4.bmp)");
	
	//setInterval(tick, 50);
}



window.onload = load;

