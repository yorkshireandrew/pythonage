class keyboard_listener{
	constructor(){
		this.pressed = {};
		var self = this
		
		document.onkeydown = function(evt) {
			evt = evt || window.event;
			var cc = evt.keyCode;
			
			switch(cc){
			
			case 37:
				self.pressed["left"] = true;
				break;
			
			case 38:
				self.pressed["up"] = true;
				break;
			
			case 39:
				self.pressed["right"] = true;
				break;
			
			case 40:
				self.pressed["down"] = true;
				break;
			
			case 32:
				self.pressed["space"] = true;
				break;
				
			case 8:
				self.pressed["backspace"] = true;
				break;
			
			case 13:
				self.pressed["enter"] = true;
				break;
				
			// numbers
			
			case 48+0:
				self.pressed["0"] = true;
				break;

			case 48+1:
				self.pressed["1"] = true;
				break;

			case 48+2:
				self.pressed["2"] = true;
				break;

			case 48+3:
				self.pressed["3"] = true;
				break;

			case 48+4:
				self.pressed["4"] = true;
				break;

			case 48+5:
				self.pressed["5"] = true;
				break;

			case 48+6:
				self.pressed["6"] = true;
				break;

			case 48+7:
				self.pressed["7"] = true;
				break;

			case 48+8:
				self.pressed["8"] = true;
				break;

			case 48+9:
				self.pressed["9"] = true;
				break;
				
			// Letters	
			
			case 64+1:
				self.pressed["a"] = true;
				break;

			case 64+2:
				self.pressed["b"] = true;
				break;

			case 64+3:
				self.pressed["c"] = true;
				break;

			case 64+4:
				self.pressed["d"] = true;
				break;

			case 64+5:
				self.pressed["e"] = true;
				break;

			case 64+6:
				self.pressed["f"] = true;
				break;

			case 64+7:
				self.pressed["g"] = true;
				break;

			case 64+8:
				self.pressed["h"] = true;
				break;

			case 64+9:
				self.pressed["i"] = true;
				break;

			case 64+10:
				self.pressed["j"] = true;
				break;

			case 64+11:
				self.pressed["k"] = true;
				break;

			case 64+12:
				self.pressed["l"] = true;
				break;

			case 64+13:
				self.pressed["m"] = true;
				break;

			case 64+14:
				self.pressed["n"] = true;
				break;

			case 64+15:
				self.pressed["o"] = true;
				break;

			case 64+16:
				self.pressed["p"] = true;
				break;

			case 64+17:
				self.pressed["q"] = true;
				break;

			case 64+18:
				self.pressed["r"] = true;
				break;

			case 64+19:
				self.pressed["s"] = true;
				break;

			case 64+20:
				self.pressed["t"] = true;
				break;

			case 64+21:
				self.pressed["u"] = true;
				break;

			case 64+22:
				self.pressed["v"] = true;
				break;

			case 64+23:
				self.pressed["w"] = true;
				break;

			case 64+24:
				self.pressed["x"] = true;
				break;

			case 64+25:
				self.pressed["y"] = true;
				break;

			case 64+26:
				self.pressed["z"] = true;
				break;
			}

			return false;
		};
		
		document.onkeyup = function(evt) {
			evt = evt || window.event;
			var cc = evt.keyCode;
			
			switch(cc){
			
			case 37:
				self.pressed["left"] = false;
				break;
			
			case 38:
				self.pressed["up"] = false;
				break;
			
			case 39:
				self.pressed["right"] = false;
				break;
			
			case 40:
				self.pressed["down"] = false;
				break;
			
			case 32:
				self.pressed["space"] = false;
				break;
				
			case 8:
				self.pressed["backspace"] = false;
				break;
			
			case 13:
				self.pressed["enter"] = false;
				break;
				
			// numbers
			
			case 48+0:
				self.pressed["0"] = false;
				break;

			case 48+1:
				self.pressed["1"] = false;
				break;

			case 48+2:
				self.pressed["2"] = false;
				break;

			case 48+3:
				self.pressed["3"] = false;
				break;

			case 48+4:
				self.pressed["4"] = false;
				break;

			case 48+5:
				self.pressed["5"] = false;
				break;

			case 48+6:
				self.pressed["6"] = false;
				break;

			case 48+7:
				self.pressed["7"] = false;
				break;

			case 48+8:
				self.pressed["8"] = false;
				break;

			case 48+9:
				self.pressed["9"] = false;
				break;
				
			// Letters	
			
			case 64+1:
				self.pressed["a"] = false;
				break;

			case 64+2:
				self.pressed["b"] = false;
				break;

			case 64+3:
				self.pressed["c"] = false;
				break;

			case 64+4:
				self.pressed["d"] = false;
				break;

			case 64+5:
				self.pressed["e"] = false;
				break;

			case 64+6:
				self.pressed["f"] = false;
				break;

			case 64+7:
				self.pressed["g"] = false;
				break;

			case 64+8:
				self.pressed["h"] = false;
				break;

			case 64+9:
				self.pressed["i"] = false;
				break;

			case 64+10:
				self.pressed["j"] = false;
				break;

			case 64+11:
				self.pressed["k"] = false;
				break;

			case 64+12:
				self.pressed["l"] = false;
				break;

			case 64+13:
				self.pressed["m"] = false;
				break;

			case 64+14:
				self.pressed["n"] = false;
				break;

			case 64+15:
				self.pressed["o"] = false;
				break;

			case 64+16:
				self.pressed["p"] = false;
				break;

			case 64+17:
				self.pressed["q"] = false;
				break;

			case 64+18:
				self.pressed["r"] = false;
				break;

			case 64+19:
				self.pressed["s"] = false;
				break;

			case 64+20:
				self.pressed["t"] = false;
				break;

			case 64+21:
				self.pressed["u"] = false;
				break;

			case 64+22:
				self.pressed["v"] = false;
				break;

			case 64+23:
				self.pressed["w"] = false;
				break;

			case 64+24:
				self.pressed["x"] = false;
				break;

			case 64+25:
				self.pressed["y"] = false;
				break;

			case 64+26:
				self.pressed["z"] = false;
				break;
			}

			return false;
		};	
	}
	
	query(to_check){
		var response = "";
		for(var index in to_check){
			var key = to_check[index]

			if(this.pressed[key] == false || typeof(this.pressed[key]) == 'undefined'){
				response += key;
				response += ",";
				response += "0";
				response += ",";
			}
			else
			{
				response += key;
				response += ",";
				response += "1";
				response += ",";									
			}
		}
		response = response.slice(0,-1); // remove trailing comma
		return response;
	}	
}