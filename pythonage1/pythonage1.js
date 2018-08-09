function loadImage(url){
	var image = new Image();
	image.src = url;
	image.onload = image_loaded;
	log("loadimage called");
	return image;
}

function load(){
	log("load called");
	img = loadImage("img\car_side1_4.bmp");
}

window.onload = load;

