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
		log('rendering image')
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

// ============================= sound ================

class pythonage_sound{
	constructor(object_id, websocket, src){
		this.object_id = object_id;
		this.websocket = websocket;
		
		// Additional construction
		this.loaded = false;
		this.src = null;
		this.img = null;
		
		self = this
		var audio = new Audio();
		audio.src = src;
		audio.addEventListener("canplaythrough", 
		function(){
			// We do not want to send the server a message on every canplaythrough
			if(!self.loaded){
				self.loaded = true;
				if(self.websocket){self.websocket.send("il," + self.object_id)}	// Tell the server we have loaded			
			}
		}
		, false);
		this.audio = audio
		
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	play(){
		if(this.loaded) this.audio.play();
	}
}

// ================== pixelmap ===========================
class pixelmap{
	constructor(object_id, x, y, visible){
		this.object_id = object_id;
		this.data = null;
		this.visible = visible;
		this.width = 0;
		this.height = 0;
		this.x = x;
		this.y = y;
	}
	
	from_imagedata(imagedata_object_id){
		var temp_canvas = document.createElement('canvas');
		var temp_context = temp_canvas.getContext('2d');
		var img = pythonage_objects[imagedata_object_id].img;
		temp_context.drawImage(img, 0, 0);
		this.data = temp_context.getImageData(0, 0, img.width, img.height);
		this.width = img.width;
		this.height = img.height;
	}
	
	make_blue_transparent(){
		var write_index = 0;
		var pix = this.data.data;
		var pix_count = this.width * this.height;
		for(var count = 0; count < pix_count; count++){			
			if(
				(pix[write_index + 0] == 0) &&
				(pix[write_index + 1] == 0) &&
				(pix[write_index + 2] == 255)
			){
				pix[write_index + 0] = 0;
				pix[write_index + 1] = 0;
				pix[write_index + 2] = 0;
				pix[write_index + 3] = 0;	
			}
			
			write_index += 4;
		}
		this.data.data = pix;
	}
	
	from_string(width, height, scaling, string_data){
		log(width)
		log(height)
		log(scaling)
		log('stringdata:' + string_data);
		var colour_data = {
				'w': [255,255,255,255],
				'r': [200,50,50,255],
				'g': [50,200,50,255],
				'b': [50,50,200,255],
				'R': [255,0,0,255],
				'G': [0,255,0,255],
				'B': [0,0,255,255],
				'y': [200,200,50,255],
				'Y': [255,255,0,255],
				'p': [253,207,176,255],
				' ': [0,0,0,0]
		}
		
		var canvas = document.createElement('canvas');
		var context = canvas.getContext('2d');
		var data = context.createImageData(width * scaling, height * scaling);
		this.width = width * scaling;
		this.height = height * scaling;
		var read_index = 0;
		var write_index = 0;
		for(var y = 0; y < height; y++){
			for(var sc = 0; sc < scaling; sc++){
				read_index = y * width;
				for(var x = 0; x < width; x++){
					log(read_index);
					log(string_data[read_index]);
					var to_fill = colour_data[string_data[read_index++]];
					log(to_fill);
					for(var sc2 = 0; sc2 < scaling; sc2++){
						data.data[write_index++] = to_fill[0];
						data.data[write_index++] = to_fill[1];
						data.data[write_index++] = to_fill[2];
						data.data[write_index++] = to_fill[3];
					}
				}					
			}		
		}
		this.data = data
	}
	
	render(context){
		log("rendering pixelmap");
		if(this.visible) context.putImageData(this.data, this.x, this.y);
		log("rendered pixelmap");
	}
	
}
