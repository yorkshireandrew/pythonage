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
pythonage_log_length = 0;

// add to on screen log
function log(text){
	var lognode = id("log");
	lognode.style.display = 'block';
	
	var loglist = id("log_list");
	var div = document.createElement("div");
	div.innerHTML = text;
	loglist.appendChild(div);
	
	if(pythonage_log_length > 100) loglist.removeChild(loglist.firstChild);
	pythonage_log_length++;
}

// clear on screen log
function clearlog(){
	var s = id("log_list");
	while (s.firstChild) {
	    s.removeChild(s.firstChild);
	}
	pythonage_log_length = 0;
	var lognode = id("log");
	lognode.style.display = 'none';
}

// error function - so you can hook in more error handling
function pythonage_error(message){
	//log(message);
}

function load(){
	if(key_listener == null) key_listener = new keyboard_listener();
	
	var c = id("my_canvas");
	canvas_context = c.getContext("2d");
	
	if(web_socket == null){
		web_socket = new MyWebSocket("localhost", "8765");
		web_socket.send("requestinggame,"+pythonage_game_name);
	}
	
	if(touch_listener == null) touch_listener = new pythonage_touch_listener(web_socket, c);
	resized();
}

window.onload = load;

