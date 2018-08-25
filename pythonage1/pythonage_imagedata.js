//========== Image Data ==========
// Image data that is required to create an image - tracks its loaded state
class pythonage_imagedata{
	
	constructor(object_id, websocket){
		this.object_id = object_id;
		this.websocket = websocket;
		
		// Additional construction
		this.loaded = false;
		this.src = null;
		this.img = null;
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	// Set the source url of the image either absolute or relative to the root
	// It kicks off the loading of the image
	// remember to use / rather than \
	
	set_source(src){
		this.src = src;
		this.loaded = false;
		var image = new Image();
		var self = this; // capture a reference to ourselves to pass into onload function. A javascript quirk worth learning.
		
		image.onload = function(){
			// Tell ourselves we have loaded
			self.loaded = true;
			// Tell the server we have loaded
			if(self.websocket) self.websocket.send("il," + self.object_id)
		}
		
		image.src = src;
		this.img = image;		
	}
}