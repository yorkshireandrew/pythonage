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