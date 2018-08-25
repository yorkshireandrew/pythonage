// ============================= sound ================

class pythonage_sound{
	constructor(object_id, websocket, src){
		this.object_id = object_id;
		this.websocket = websocket;
		
		// Additional construction
		this.loaded = false;
		this.src = null;
		this.img = null;
		
		self = this
		var audio = new Audio();
		audio.src = src;
		audio.addEventListener("canplaythrough", 
		function(){
			// We do not want to send the server a message on every canplaythrough
			if(!self.loaded){
				self.loaded = true;
				if(self.websocket){self.websocket.send("il," + self.object_id)}	// Tell the server we have loaded			
			}
		}
		, false);
		this.audio = audio
		
		pythonage_objects[object_id] = this; // Add ourselves
	}
	
	play(){
		if(this.loaded) this.audio.play();
	}
}