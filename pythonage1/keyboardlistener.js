class keyboard_listener{
	constructor(){
		this.pressed = {};
		
		document.onkeydown = function(evt) {
			evt = evt || window.event;
			var cc = evt.keyCode;
			
			switch(cc){
			
			case 37:
				this.pressed["left"] = true;
				break;
			
			case 38:
				this.pressed["up"] = true;
				break;
			
			case 39:
				this.pressed["right"] = true;
				break;
			
			case 40:
				this.pressed["down"] = true;
				break;
			
			case 32:
				this.pressed["space"] = true;
				break;
				
			case 8:
				this.pressed["backspace"] = true;
				break;
			
			case 13:
				this.pressed["enter"] = true;
				break;
				
			// numbers
			
			case 48+0:
				this.pressed["0"] = true;
				break;

			case 48+1:
				this.pressed["1"] = true;
				break;

			case 48+2:
				this.pressed["2"] = true;
				break;

			case 48+3:
				this.pressed["3"] = true;
				break;

			case 48+4:
				this.pressed["4"] = true;
				break;

			case 48+5:
				this.pressed["5"] = true;
				break;

			case 48+6:
				this.pressed["6"] = true;
				break;

			case 48+7:
				this.pressed["7"] = true;
				break;

			case 48+8:
				this.pressed["8"] = true;
				break;

			case 48+9:
				this.pressed["9"] = true;
				break;
				
			// Letters	
			
			case 64+1:
				this.pressed["a"] = true;
				break;

			case 64+2:
				this.pressed["b"] = true;
				break;

			case 64+3:
				this.pressed["c"] = true;
				break;

			case 64+4:
				this.pressed["d"] = true;
				break;

			case 64+5:
				this.pressed["e"] = true;
				break;

			case 64+6:
				this.pressed["f"] = true;
				break;

			case 64+7:
				this.pressed["g"] = true;
				break;

			case 64+8:
				this.pressed["h"] = true;
				break;

			case 64+9:
				this.pressed["i"] = true;
				break;

			case 64+10:
				this.pressed["j"] = true;
				break;

			case 64+11:
				this.pressed["k"] = true;
				break;

			case 64+12:
				this.pressed["l"] = true;
				break;

			case 64+13:
				this.pressed["m"] = true;
				break;

			case 64+14:
				this.pressed["n"] = true;
				break;

			case 64+15:
				this.pressed["o"] = true;
				break;

			case 64+16:
				this.pressed["p"] = true;
				break;

			case 64+17:
				this.pressed["q"] = true;
				break;

			case 64+18:
				this.pressed["r"] = true;
				break;

			case 64+19:
				this.pressed["s"] = true;
				break;

			case 64+20:
				this.pressed["t"] = true;
				break;

			case 64+21:
				this.pressed["u"] = true;
				break;

			case 64+22:
				this.pressed["v"] = true;
				break;

			case 64+23:
				this.pressed["w"] = true;
				break;

			case 64+24:
				this.pressed["x"] = true;
				break;

			case 64+25:
				this.pressed["y"] = true;
				break;

			case 64+26:
				this.pressed["z"] = true;
				break;
			}

			return false;
		};
		
		document.onkeyup = function(evt) {
			evt = evt || window.event;
			var cc = evt.keyCode;
			
			switch(cc){
			
			case 37:
				this.pressed["left"] = false;
				break;
			
			case 38:
				this.pressed["up"] = false;
				break;
			
			case 39:
				this.pressed["right"] = false;
				break;
			
			case 40:
				this.pressed["down"] = false;
				break;
			
			case 32:
				this.pressed["space"] = false;
				break;
				
			case 8:
				this.pressed["backspace"] = false;
				break;
			
			case 13:
				this.pressed["enter"] = false;
				break;
				
			// numbers
			
			case 48+0:
				this.pressed["0"] = false;
				break;

			case 48+1:
				this.pressed["1"] = false;
				break;

			case 48+2:
				this.pressed["2"] = false;
				break;

			case 48+3:
				this.pressed["3"] = false;
				break;

			case 48+4:
				this.pressed["4"] = false;
				break;

			case 48+5:
				this.pressed["5"] = false;
				break;

			case 48+6:
				this.pressed["6"] = false;
				break;

			case 48+7:
				this.pressed["7"] = false;
				break;

			case 48+8:
				this.pressed["8"] = false;
				break;

			case 48+9:
				this.pressed["9"] = false;
				break;
				
			// Letters	
			
			case 64+1:
				this.pressed["a"] = false;
				break;

			case 64+2:
				this.pressed["b"] = false;
				break;

			case 64+3:
				this.pressed["c"] = false;
				break;

			case 64+4:
				this.pressed["d"] = false;
				break;

			case 64+5:
				this.pressed["e"] = false;
				break;

			case 64+6:
				this.pressed["f"] = false;
				break;

			case 64+7:
				this.pressed["g"] = false;
				break;

			case 64+8:
				this.pressed["h"] = false;
				break;

			case 64+9:
				this.pressed["i"] = false;
				break;

			case 64+10:
				this.pressed["j"] = false;
				break;

			case 64+11:
				this.pressed["k"] = false;
				break;

			case 64+12:
				this.pressed["l"] = false;
				break;

			case 64+13:
				this.pressed["m"] = false;
				break;

			case 64+14:
				this.pressed["n"] = false;
				break;

			case 64+15:
				this.pressed["o"] = false;
				break;

			case 64+16:
				this.pressed["p"] = false;
				break;

			case 64+17:
				this.pressed["q"] = false;
				break;

			case 64+18:
				this.pressed["r"] = false;
				break;

			case 64+19:
				this.pressed["s"] = false;
				break;

			case 64+20:
				this.pressed["t"] = false;
				break;

			case 64+21:
				this.pressed["u"] = false;
				break;

			case 64+22:
				this.pressed["v"] = false;
				break;

			case 64+23:
				this.pressed["w"] = false;
				break;

			case 64+24:
				this.pressed["x"] = false;
				break;

			case 64+25:
				this.pressed["y"] = false;
				break;

			case 64+26:
				this.pressed["z"] = false;
				break;
			}

			return false;
		};	
	}
	
	query(to_check){
		response = "";
		for(var index in to_check){
			// undefined == false evaluates to false
			if(this.pressed[to_check[index]] == false){
				response += to_check[index];
				response += ",";
				response += "0";
				response += ",";
			}else{
				response += to_check[index];
				response += ",";
				response += "1";
				response += ",";				
			}
		}
		response = response.slice(0,-1); // remove trailing comma
		return response;
	}	
}