class pythonage_rectangle{
	
	constructor(object_id, width, height, style, visible){
		this.object_id = object_id;
		this.width = width;
		this.height = height;
		this.style = style;
		this.visible = visible;
		this.layer = 0;
		this.scale = 1.0;
	}
	
	render(context){
		if(this.visible){
			var sc = this.scale;
			context.fillStyle = this.style;
			context.fillRect(0, 0, this.width * sc, this.height * sc);
		}
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
}

function pythonage_command_new_rectangle(args){
	var object_id = args[1];
	var width = parseInt(args[2]);
	var height = parseInt(args[3]);
	var style = args[4];
	
	var visible = false;
	if(args[5] == "t") visible = true
	
	var new_rectangle = new pythonage_rectangle(object_id, width, height, style, visible);
	pythonage_objects[object_id] = new_rectangle;
}

function pythonage_command_update_rectangle(args){
	var object_id = args[1];
	var width = parseInt(args[2]);
	var height = parseInt(args[3]);
	var style = args[4];
	
	var visible = false;
	if(args[5] == "t") visible = true;
	
	var rect = pythonage_objects[object_id];
	rect.width = width;
	rect.height = height;
	rect.style = style;
	rect.visible = visible;
}