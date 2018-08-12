class MyWebSocket{
	
	 constructor(host,port){
         if ("WebSocket" in window) {
        	 
			 var websocket = new WebSocket("ws://" + host + ":" + port + "/");
			 this.identity = "new";
			 
			 websocket.onopen = function(){websocket.send("connection," + this.identity);};
			 
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
		 this.websocket.send(message);
	 }
}   
