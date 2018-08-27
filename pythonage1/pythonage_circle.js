class pythonage_circle{
	
	constructor(object_id, radius, style, visible){
		this.object_id = object_id;
		this.radius = radius;
		this.style = style;
		this.visible = visible;
		this.layer = 0;
		this.scale = 1.0;
	}
	
	render(context){
		if(this.visible){
			var sc = this.scale;
			context.beginPath();
			context.strokeStyle = this.style;
			context.arc(0, 0, this.radius * this.scale, 0, 2*Math.PI, false)
			context.fillStyle = this.style;
			context.fill();
			context.lineWidth = 1;
			context.stroke();
		}
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
}

function pythonage_command_new_circle(args){
	var object_id = args[1];
	var radius = parseInt(args[2]);
	var style = args[3];
	
	var visible = false;
	if(args[4] == "t") visible = true
	
	var new_circle = new pythonage_circle(object_id, radius, style, visible);
	pythonage_objects[object_id] = new_circle;
}

function pythonage_command_update_circle(args){
	var object_id = args[1];
	var radius = parseInt(args[2]);
	var style = args[3];
	
	var visible = false;
	if(args[4] == "t") visible = true;
	
	var circle = pythonage_objects[object_id];
	circle.radius = radius;
	circle.style = style;
	circle.visible = visible;
}