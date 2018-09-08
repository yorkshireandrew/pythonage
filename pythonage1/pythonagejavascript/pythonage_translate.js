//========== Translate ==========
// Translate is a scene graph component that applies x,y movement and can have multiple children
class pythonage_translate{
	constructor(object_id, x, y, visible){
		this.object_id = object_id;
		this.x = x;
		this.y = y;
		this.visible = visible;
		this.scale = 1.0;
		
		// Additional construction
		this.parent = null;
		this.children = []; // Store children as an array so we can control render ordering
		pythonage_objects[object_id] = this; // Add ourselves
	}
		
	render(context){
		if(this.visible){
			context.save();
			context.translate(this.x * this.scale, this.y * this.scale);
			for(var child_index in this.children){
				this.children[child_index].render(context);
			}
			context.restore();
		}
	}
	
	renderlayer(context, layer){
		if(this.visible){
			context.save();
			context.translate(this.x * this.scale, this.y * this.scale);
			for(var child_index in this.children){
				this.children[child_index].renderlayer(context, layer);
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

function pythonage_command_new_translate(args){
	
	var object_id = args[1];
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	
	var visible = false;
	if(args[4] == "t") visible = true;
	
	new pythonage_translate(object_id, x, y, visible);
}

function pythonage_command_update_translate(args){
	
	var object_id = parseInt(args[1]);
	var new_x = parseInt(args[2]);
	var new_y = parseInt(args[3]);
	
	var visible = false;
	if(args[4] == "t") visible = true;
	
	translate = pythonage_objects[object_id];
	translate.x = new_x
	translate.y = new_y
	translate.visible = visible
}