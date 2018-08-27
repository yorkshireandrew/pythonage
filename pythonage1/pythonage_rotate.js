//========== Rotate ==========
// Rotate is a scene graph component that applies rotation and can have multiple children
var pythonage_deg_to_radians = Math.PI/180.0;
var pythonage_radians_to_deg = 180.0/Math.PI;

class pythonage_rotate{
	
	constructor(object_id, rotation_in_deg, visible){
		this.object_id = object_id;
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
	
	renderlayer(context, layer){
		if(this.visible){
			context.save();
			context.rotate(this.rotation);
			for(var child_index in this.children){
				this.children[child_index].renderlayer(context, layer);
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

function pythonage_command_new_rotate(args){
	
	var object_id = args[1];
	var deg = parseFloat(args[2]);
	
	var visible = false;
	if(args[3] == "t") visible = true;
	
	new pythonage_rotate(object_id, deg, visible);	
}

function pythonage_command_update_rotate(args){
	
	var object_id = args[1];
	var new_angle = parseFloat(args[2]);
	
	var visible = false;
	if(args[3] == "t") visible = true;
	
	rotate = pythonage_objects[object_id];
	rotate.rotation = pythonage_deg_to_radians * new_angle
	rotate.visible = visible
}