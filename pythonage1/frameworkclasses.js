// Basic classes that can be items or composed in the scene graph
// that are part of the pythonage framework

// ========== Image ==========
// Represents something that can be rendered in the scene graph
class pythonage_image{
	
	constructor(name, album_name, image_data_name, width, height, visible){
		this.name = name;
		this.width = width;
		this.height = height;
		this.visible = visible;
		
		// Additional
		if(typeof(pythonage_albums[album_name]) == 'undefined') pythonage_error("Constructing image " + name + " the album " + album_name + " did not exist")
		var album = pythonage_albums[album_name];
		if(typeof(album[image_data_name]) == 'undefined') pythonage_error("Constructing image " + name + " the imagedata " + image_data_name + " did not exist in album " + album_name)		
		this.img = album[image_data_name].img;
		
		this.parent = null;
		pythonage_image_objects[name] = this; // Add ourselves to image objects
	}
	
	render(context){
		if(this.visible) context.drawImage(this.img, 0, 0, this.width, this.height);
	}
	
	// Detach from our parent if we have one then attach to another node
	attach_to(name){
		if(this.parent != null) this.parent.detatch(this.name); 
		
		if(typeof(pythonage_scene_graph[name]) == 'undefined') pythonage_error("Attaching image " + this.name + " to scene item " + name + "," + name + " did not exist");
		var new_parent = pythonage_scene_graph[name];
		new_parent.attach_image(this.name)
	}
}

//========== Image Data ==========
// Image data that is required to create an image - Tracks the loaded state
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

//========== Translate ==========
// Translate is a scene graph component that applies x,y movement and can have multiple children
class pythonage_translate{
	constructor(name, x, y, visible){
		this.name = name;
		this.x = x;
		this.y = y;
		this.visible = visible;
		
		// Additional
		this.parent = null;
		this.children = []; // Store children as an array so we can control render ordering
		pythonage_scene_graph[name] = this; // Add ourselves to the scene graph
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
	
	attach_scene_graph_item(name){
		if(typeof(pythonage_scene_graph[name]) == 'undefined') pythonage_error("Attaching scene graph item to translate node " + this.name + " the item " + name + " did not exist");
		var node = pythonage_scene_graph[name];
		if(node.parent != null) node.parent.detach(node.name); // If the node is already attached to something then detach it first.
		node.parent = this;
		this.children.push(node);
	}
	
	// Attach an image to this node
	attach_image(name){
		if(typeof(pythonage_image_objects[name]) == 'undefined') pythonage_error("Attaching image to translate node " + this.name + " the image " + name + " did not exist");
		var image = pythonage_image_objects[name];
		image.parent = this;
		this.children.push(image);
	}
	
	// Detach a specific child from this node
	detach_child(name){
		for(var child_index in this.children){
			if(this.children[child_index].name == name){
				this.children[child_index].parent == null;
				this.children.splice(child_index, 1);
				break;
			}
		}		
	}
	
	// Detach from our parent if we have one then attach to another node
	attach_to(name){
		if(this.parent != null) this.parent.detatch(this.name); 
		
		if(typeof(pythonage_scene_graph[name]) == 'undefined') pythonage_error("Attaching translate node " + this.name + " to scene item " + name + "," + name + " did not exist");
		var new_parent = pythonage_scene_graph[name];
		new_parent.attach_scene_item(this.name)
	}
}


//========== Rotate ==========
//Translate is a scene graph component that applies rotation and can have multiple children
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
		pythonage_scene_graph[name] = this; // Add ourselves to the scene graph
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
	
	set_degrees(rotation_in_deg){
		this.rotation = pythonage_deg_to_radians * rotation_in_deg;
	}
	
	set_radians(rotation_in_radians){
		this.rotation = rotation_in_radians;
	}
	
	attach_scene_graph_item(name){
		if(typeof(pythonage_scene_graph[name]) == 'undefined') pythonage_error("Attaching scene graph item to rotation node " + this.name + " the item " + name + " did not exist");
		var node = pythonage_scene_graph[name];
		if(node.parent != null) node.parent.detach(node.name); // If the node is already attached to something then detach it first.
		node.parent = this;
		this.children.push(node);
	}
	
	// Attach an image to this node
	attach_image(name){
		if(typeof(pythonage_image_objects[name]) == 'undefined') pythonage_error("Attaching image to rotation node " + this.name + " the image " + name + " did not exist");
		var image = pythonage_image_objects[name];
		image.parent = this;
		this.children.push(image);
	}
	
	// Detach a specific child from this node
	detach_child(name){
		for(var child_index in this.children){
			if(this.children[child_index].name == name){
				this.children[child_index].parent == null;
				this.children.splice(child_index, 1);
				break;
			}
		}		
	}
	
	// Detach from our parent if we have one then attach to another node
	attach_to(name){
		if(this.parent != null) this.parent.detatch(this.name); 
		
		if(typeof(pythonage_scene_graph[name]) == 'undefined') pythonage_error("Attaching rotation node " + this.name + " to scene item " + name + "," + name + " did not exist");
		var new_parent = pythonage_scene_graph[name];
		new_parent.attach_scene_item(this.name)
	}
}
