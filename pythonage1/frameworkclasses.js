// Basic classes that can be items or composed in the scene graph
// that are part of the pythonage framework

// Image node 
class pythonage_image{
	constructor(name, album_name, image_data_name, width, height){
		this.name = name;
		if(typeof(pythonage_albums[album_name]) == 'undefined') pythonage_error("Constructing image " + name + " the album " + album_name + " did not exist")
		var album = pythonage_albums[album_name];
		if(typeof(album[image_data_name]) == 'undefined') pythonage_error("Constructing image " + name + " the imagedata " + image_data_name + " was not found in album " + album_name)		
		this.img = album[image_data_name].img;
		this.width = width;
		this.height = height;		
	}
	
	render(context){
		context.drawImage(this.img, 0, 0, this.width, this.height);
	}
}

// Imagedata that is required to create an image - Tracks the loaded state
class pythonage_imagedata{
	constructor(name, album_name){
		if(typeof(pythonage_albums[album_name]) == 'undefined') pythonage_error("Constructing imagedata " + name + " the album " + album_name + " did not exist")
		var album = pythonage_albums[album_name];
		this.name = name;
		this.loaded = false;
		this.src = null;
		this.img = null;
		album[name] = this;
	}
	
	// Set the source url of the image either absolute or relative to the root
	// It kicks off the loading of the image
	// remember to use / rather than \
	set_source(src){
		this.src = src;
		this.loaded = false;
		var image = new Image();
		var thisimagedata = this; // capture this (imagedata) reference and pass into the onload function
		image.onload = function(){thisimagedata.loaded = true;}
		image.src = src;
		this.img = image;		
	}
}
