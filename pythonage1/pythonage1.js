var loading_images = 999;
var loaded_images = {};

var has_rendered_car = false;

// Maps of names to items for acquiring resources, 
// Image objects and scene graph objects are in different associative arrays to reduce name collisions
var pythonage_albums = {};
var pythonage_image_objects = {}; 
var pythonage_scene_graph = {}
var canvas_context = null;
var key_listener = null;

function image_loaded(name){
	loading_images--;
	log("loaded image" + name );
}

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

function loadImage(url, name){
	loading_images++;
	if(loading_images == 1000) loading_images = 1;
	var image = new Image();
	image.src = url;
	image.onload = function(){log("foo");image_loaded(name);};
	loaded_images[name] = image;
	log("started to load image " + name );
}

function tick(){
	if(pythonage_album_pending_loads("testalbum") == 0 && has_rendered_car == false){
		log("trying to render");
		has_rendered_car = true;
		pythonage_consume_nugget("(new-img,mycar,testalbum,carimgdata,100,100,true)");
		pythonage_consume_nugget("(new-tran,carposition,0,0,true)");
		pythonage_consume_nugget("(attach-img,carposition,mycar)");
		pythonage_consume_nugget("(render,carposition)");
	}
}

function load(){
	log("load called");
	key_listener = new keyboard_listener();
	var c = id("my_canvas");
	canvas_context = c.getContext("2d");
	setInterval(tick, 50);
	
	pythonage_consume_nugget("(new-album,testalbum)");
	pythonage_consume_nugget("(new-imgd,carimgdata,testalbum)");
	pythonage_consume_nugget("(set-imgd-src,testalbum,carimgdata,img/car_side1_4.bmp)");
}



window.onload = load;

