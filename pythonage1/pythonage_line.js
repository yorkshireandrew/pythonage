class pythonage_line{
	
	constructor(object_id, x1, y1, x2, y2, style, width, visible){
		this.object_id = object_id;
		this.x1 = x1;
		this.y1 = y1;
		this.x2 = x2;
		this.y2 = y2;
		this.style = style;
		this.width = width;
		this.visible = visible;
		this.layer = 0;
		this.scale = 1.0;
	}
	
	render(context){
		if(this.visible){
			var sc = this.scale;
			context.beginPath();
			context.strokeStyle = this.style;
			context.lineWidth = Math.floor(this.width * sc);
			context.moveTo(this.x1 * sc, this.y1 * sc);
			context.lineTo(this.x2 * sc, this.y2 * sc);
			context.stroke();
		}
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
}

function pythonage_command_new_line(args){
	
	var object_id = args[1];
	var x1 = parseInt(args[2]);
	var y1 = parseInt(args[3]);
	var x2 = parseInt(args[4]);
	var y2 = parseInt(args[5]);
	var style = args[6];
	var width = parseInt(args[7]);
	
	var visible = false;
	if(args[8] == "t") visible = true
	
	new_line = new pythonage_line(object_id, x1, y1, x2, y2, style, width, visible);	
	pythonage_objects[object_id] = new_line;	
}

function pythonage_command_update_line(args){
	
	var object_id = args[1];
	var x1 = parseInt(args[2]);
	var y1 = parseInt(args[3]);
	var x2 = parseInt(args[4]);
	var y2 = parseInt(args[5]);
	var style = args[6];
	var width = parseInt(args[7]);
	
	var visible = false;
	if(args[8] == "t") visible = true
	
	line = pythonage_objects[object_id];
	line.x1 = x1;
	line.y1 = y1;
	line.x2 = x2;
	line.y2 = y2;
	line.style = style;
	line.width = width;
	line.visible = visible;
}