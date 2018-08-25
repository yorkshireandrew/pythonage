class pythonage_text{
	
	constructor(object_id, x, y, font, style, text, visible){
		this.object_id = object_id;
		this.x = x;
		this.y = y;
		this.font = font;
		this.style = style;
		this.text = text;
		this.visible = visible;
		log('constructed text')
	}
	
	render(context){
		log('constructed text0')
		if(this.visible){
			log('constructed text1')
			context.font = this.font;
			log('constructed text2')
			context.fillStyle = this.style;
			log('constructed text3')
			context.fillText(this.text, this.x, this.y);
			log('constructed text4')
		}
	}	
}