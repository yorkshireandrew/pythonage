var loading_images = 999;
var loaded_images = {};

var has_rendered_car = false;

// Maps of names to items for aquiring resources
var pythonage_albums = {};
var pythonage_imagedatas = {};


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
	log(message);
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
		var pimg = new pythonage_image("mycar","testalbum","car", 100, 100);
		var c = id("my_canvas");
		ctx = c.getContext("2d");
		ctx.save();
		pimg.render(ctx);
		ctx.restore();		
	}
}

function load(){
	log("load called");
	pythonage_add_album("testalbum");
	var imgdata = new pythonage_imagedata("car", "testalbum");
	imgdata.set_source("img/car_side1_4.bmp");
	setInterval(tick, 50);
}



window.onload = load;

