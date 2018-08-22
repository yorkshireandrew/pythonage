// Basic classes that can be items or composed in the scene graph
// that are part of the pythonage framework

// ========== Image ==========
// Represents something that can be rendered in the scene graph
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
			log("Image loaded");
			// Tell the server we have loaded
			if(self.websocket){
				self.websocket.send("il," + self.object_id)
			}
		}
		image.src = src;
		this.img = image;		
	}
}

//========== Translate ==========
// Translate is a scene graph component that applies x,y movement and can have multiple children
class pythonage_translate{
	constructor(object_id, x, y, visible){
		this.object_id = object_id;
		this.x = x;
		this.y = y;
		this.visible = visible;
		
		// Additional construction
		this.parent = null;
		this.children = []; // Store children as an array so we can control render ordering
		pythonage_objects[object_id] = this; // Add ourselves
	}
		
	render(context){
		if(this.visible){
			context.save();
			context.translate(this.x, this.y);
			for(var child_index in this.children){
				this.children[child_index].render(context);
			}
			context.restore();
		}
	}
	
	append(object_id){
		if(typeof(pythonage_objects[object_id]) == 'undefined') pythonage_error("Calling append on translate node " + this.name + " the object to append " + object_id + " did not exist");
		var node = pythonage_objects[object_id];
		
		if(node.parent != null) node.parent.detach(node.object_id); // If the node is already attached to something then detach it first.
		node.parent = this;
		this.children.push(node);
	}
	
	// Detach a child from this node
	detach(object_id){
		for(var child_index in this.children){
			if(this.children[child_index].object_id == object_id){
				this.children[child_index].parent == null;
				this.children.splice(child_index, 1);
				break;
			}
		}		
	}
}


//========== Rotate ==========
// Rotate is a scene graph component that applies rotation and can have multiple children
var pythonage_deg_to_radians = Math.PI/180.0;
var pythonage_radians_to_deg = 180.0/Math.PI;

class pythonage_rotate{
	
	constructor(name, rotation_in_deg, visible){
		this.name = name;
		this.rotation = pythonage_deg_to_radians * rotation_in_deg;
		this.visible = visible;

		// Additional
		this.parent = null;
		this.children = []; // Store children as an array so we can control render ordering
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	render(context){
		if(this.visible){
			context.save();
			context.rotate(this.rotation);
			for(var child_index in this.children){
				this.children[child_index].render(context);
			}
			context.restore();
		}
	}
	
	set_degrees(rotation_in_deg){
		this.rotation = pythonage_deg_to_radians * rotation_in_deg;
	}
	
	set_radians(rotation_in_radians){
		this.rotation = rotation_in_radians;
	}
	
	append(object_id){
		if(typeof(pythonage_objects[object_id]) == 'undefined') pythonage_error("Calling append on translate node " + this.name + " the object to append " + object_id + " did not exist");
		var node = pythonage_objects[object_id];
		
		if(node.parent != null) node.parent.detach(node.object_id); // If the node is already attached to something then detach it first.
		node.parent = this;
		this.children.push(node);
	}
	
	// Detach a child from this node
	detach(object_id){
		for(var child_index in this.children){
			if(this.children[child_index].object_id == object_id){
				this.children[child_index].parent == null;
				this.children.splice(child_index, 1);
				break;
			}
		}		
	}
}
