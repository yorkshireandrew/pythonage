class MyWebSocket{
	
	 constructor(host, port){
         if ("WebSocket" in window) {
        	 
			 var websocket = new WebSocket("ws://" + host + ":" + port + "/");
			 this.opened = false;
			 this.pending_open = [];
			 var self = this
			 
			 websocket.onopen = function(){
				 //log("Websocket onopen")
				 for(var pending_open_index in self.pending_open){
					 websocket.send(self.pending_open[pending_open_index]);
					 //log("sending pending message: " + self.pending_open[pending_open_index]);
				 }
				 self.opened = true;
				//log("Websocket onopen complete")				 
			 };
			 
			 websocket.onmessage = function (evt) { 
	             var received_msg = evt.data;
	             //log("message " + received_msg);
	             pythonage_consume(received_msg);
	         };
	          
	         websocket.onclose = function() { 
                 alert("Connection is closed..."); 
             };
             
             this.websocket = websocket;  
                     
         } else {
             alert("WebSocket NOT supported by your Browser!");
         }				 
	 }
	 
	 send(message){
		 if(this.opened){
			 //log('websocket open and sending message: ' + message)
			 this.websocket.send(message);
		 }else{
			 //log('websocket not ready storing pending message: ' + message)
			 this.pending_open.push(message);
		 }
	 }
}   
