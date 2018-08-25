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
	}
	
	render(context){
		if(this.visible){
			context.beginPath();
			context.strokeStyle = this.style;
			context.lineWidth = this.width;
			context.moveTo(this.x1, this.y1);
			context.lineTo(this.x2, this.y2);
			context.stroke();
		}
	}	
}