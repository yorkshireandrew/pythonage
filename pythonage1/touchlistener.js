class pythonage_touch_listener{
	
	constructor(websocket, canvas){
		this.canvas_internal_width = 1000; // Change these if you alter the canvas size
		this.canvas_internal_height = 500;
		
		this.websocket = websocket;
		this.canvas = canvas;
		var self = this;
		
		canvas.addEventListener("touchstart", 
		function(event){
			self.handle_touch(event)
		}, false);
		
		
		canvas.addEventListener("click", 
		function(event){
			self.handle_click(event)
		}, false);
	}
	
	handle_touch(event){
		var rect = this.canvas.getBoundingClientRect();
		var xCoordinate = event.touches[0].clientX - rect.left;
		var yCoordinate = event.touches[0].clientY - rect.top;
		
		xCoordinate = Math.floor(this.canvas_internal_width * xCoordinate / rect.width)
		yCoordinate = Math.floor(this.canvas_internal_height * yCoordinate / rect.height)
		this.websocket.send('cl,' + xCoordinate + ',' + yCoordinate);
	}
	
	handle_click(event){
		var rect = this.canvas.getBoundingClientRect();
		var xCoordinate = event.clientX - rect.left;
		var yCoordinate = event.clientY - rect.top;
		xCoordinate = Math.floor(this.canvas_internal_width * xCoordinate / rect.width)
		yCoordinate = Math.floor(this.canvas_internal_height * yCoordinate / rect.height)
		this.websocket.send('cl,' + xCoordinate + ',' + yCoordinate);
	}
}