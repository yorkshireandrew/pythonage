class pythonage_text{
	
	constructor(object_id, x, y, font, style, text, visible){
		this.object_id = object_id;
		this.x = x;
		this.y = y;
		this.font = font;
		this.style = style;
		this.text = text;
		this.visible = visible;
	}
	
	render(context){
		if(this.visible){
			context.font = this.font;
			context.fillStyle = this.style;
			context.fillText(this.text, this.x, this.y);
		}
	}	
}