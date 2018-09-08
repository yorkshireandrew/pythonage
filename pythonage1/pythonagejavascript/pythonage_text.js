class pythonage_text{
	
	constructor(object_id, x, y, font, style, text, visible){
		this.object_id = object_id;
		this.x = x;
		this.y = y;
		this.font = font;
		this.style = style;
		this.text = text;
		this.visible = visible;
		this.layer = 0;
	}
	
	render(context){
		if(this.visible){
			context.font = this.font;
			context.fillStyle = this.style;
			context.fillText(this.text, this.x, this.y);
		}
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
}

function pythonage_command_new_text(args){
	
	var object_id = args[1];
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	var font = args[4];
	var style = args[5];
	var text = args[6];

	var visible = false;
	if(args[7] == "t") visible = true
	var unescaped_text = text.split("{{comma}}").join(",");
	new_text = new pythonage_text(object_id, x, y, font, style, unescaped_text, visible);	
	pythonage_objects[object_id] = new_text;	
}

function pythonage_command_update_text(args){
	
	var object_id = args[1];
	var text = args[2]
	
	var visible = false;
	if(args[3] == "t") visible = true
	
	text_object = pythonage_objects[object_id];
	var unescaped_text = text.split("{{comma}}").join(",");
	text_object.text = unescaped_text;
	text_object.visible = visible;
}