// ========== Image ==========
// Represents an image that can be rendered in the scene graph. It will need loaded imagedata to work
class pythonage_image{
	
	constructor(object_id, imagedata_object_id, width, height, visible){
		this.object_id = object_id;
		this.width = width;
		this.height = height;
		this.visible = visible;
		
		// Additional construction
		if(typeof(pythonage_objects[imagedata_object_id]) == 'undefined') pythonage_error("Constructing image " + object_id + " the imagedata " + imagedata_object_id + " did not exist")		
		this.img = pythonage_objects[imagedata_object_id].img;
		
		this.parent = null;
		this.layer = 0;
		this.scale = 1.0;
		
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	render(context){
		var sc = this.scale;
		if(this.visible) context.drawImage(this.img, 0, 0, this.width * sc, this.height * sc);
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
}

function pythonage_command_new_image(args){
	
	var object_id = args[1];
	var image_data_object_id = args[2]; 
	var width = parseInt(args[3]);
	var height = parseInt(args[4]);
	
	var visible = false;
	if(args[5] == "t") visible = true;
	
	new pythonage_image(object_id, image_data_object_id, width, height, visible);
}

function pythonage_command_update_image(args){
	
	var object_id = args[1];
	
	var visible = false;
	if(args[4] == "t") visible = true;
	
	image = pythonage_objects[object_id];
	image.width = parseInt(args[2]);
	image.height = parseInt(args[3]);
	image.visible = visible
}