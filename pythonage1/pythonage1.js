var loading_images = 999;
var loaded_images = {};

var has_rendered_car = false;

function image_loaded(name){
	loading_images--;
	log("loaded image" + name );
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
	if(loading_images == 0 && has_rendered_car == false){
		log("trying to render");
		has_rendered_car = true;
		var c = id("my_canvas");
		ctx = c.getContext("2d");
		ctx.save();
		ctx.drawImage(loaded_images["car"], 10, 10, 100, 100);
		ctx.restore();		
	}
}

function load(){
	log("load called");
	img = loadImage("img/car_side1_4.bmp", "car");
	setInterval(tick, 50);
}



window.onload = load;

