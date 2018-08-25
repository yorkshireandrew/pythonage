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
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	render(context){
		if(this.visible) context.drawImage(this.img, 0, 0, this.width, this.height);
	}
}