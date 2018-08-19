class MyWebSocket{
	
	 constructor(host, port){
         if ("WebSocket" in window) {
        	 
			 var websocket = new WebSocket("ws://" + host + ":" + port + "/");
			 this.identity = "new";
			 this.opened = false;
			 this.pending_open = [];
			 var self = this
			 
			 websocket.onopen = function(){
				 websocket.send("connection," + self.identity);
				 for(pending_open_index in self.pending_open){
					 websocket.send(self.pending_open[pending_open_index]);
				 }
				 self.opened = true;			 
			 };
			 
			 websocket.onmessage = function (evt) { 
	             var received_msg = evt.data;
	             log("message " + received_msg);
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
			 this.websocket.send(message);
		 }else{
			 this.pending_open.push(message);
		 }
	 }
}   
