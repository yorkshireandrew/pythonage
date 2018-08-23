var pythonage_input_stream = "";

// actually because web sockets are already tokens we do not need this function
function pythonage_consume_nugget(nugget){
	pythonage_input_stream += nugget;
	fragments = pythonage_input_stream.split("(");
	var frag_length = fragments.length
	var frag_length_minus_one = frag_length-1;
	if(frag_length > 1){
		for(var fragment_index in fragments){
			var frag = fragments[fragment_index];
			if(frag.length == 0) continue;
			
			if(frag.endsWith(")")){
				pythonage_consume(frag.slice(0,-1));
				if(fragment_index == frag_length_minus_one){
					pythonage_input_stream = "";
				}
			}else{
				if(fragment_index == frag_length_minus_one){
					pythonage_input_stream = "(" +frag;
				}
			}
		}
	}
}

function pythonage_consume(commandstring){
	var args = commandstring.split(",");
	
	var command = args[0];
	var number_of_arguments = args.length -1;
	
	switch(command){
			
		case "new-imgd":
			new pythonage_imagedata(args[1], web_socket); // object_id, websocket
			break; // DO NOT FORGET TO BREAK
			
		case "nid":
			new pythonage_imagedata(args[1], web_socket); // object_id, websocket
			break;
		
		case "set-imgd-src":
			pythonage_command_set_image_data_source(args);
			break;
			
		case "sids":
			pythonage_command_set_image_data_source(args);
			break;
			
		case "new-img":
			pythonage_command_new_image(args);
			break;
			
		case "ni":
			pythonage_command_new_image(args);
			break;
			
		case "new-tran":
			pythonage_command_new_translate(args);
			break;
			
		case "nt":
			pythonage_command_new_translate(args);
			break;
			
		case "new-rot":
			pythonage_command_new_rotate(args);
			break;
			
		case "nr":
			pythonage_command_new_rotate(args);
			break;
		
		case "append":
			pythonage_command_append(args);
			break;
			
		case "a":
			pythonage_command_append(args);
			break;
			
		case "append-to":
			pythonage_command_append_to(args);
			break;
			
		case "at":
			pythonage_command_append_to(args);
			break;
			
		case "detach":
			pythonage_command_detach(args);
			break;
			
		case "dt":
			pythonage_command_detach(args);
			break;
			
		case "render":
			pythonage_objects[args[1]].render(canvas_context);
			break;
			
		case "r":
			pythonage_objects[args[1]].render(canvas_context);
			break;
					
		case "query-keys":
			pythonage_query_keys(args)
			break;
		
		case "qk":
			pythonage_query_keys(args)
			break;
			
		case "reset":
			pythonage_command_reset(args);
			break;
			
		case "ui":
			pythonage_command_update_image(args);
			break;
			
		case "ut":
			pythonage_command_update_translate(args);
			break;
			
		case "ur":
			pythonage_command_update_rotate(args);
			break;
			
		case "ns":
			pythonage_command_new_sound(args);
			break;
			
		case "ps":
			pythonage_command_play_sound(args);
			break;
			
		case "npmfid":
			pythonage_command_new_pixelmap_from_imagedata(args);
			break;
			
		case "npmfs":
			pythonage_command_new_pixelmap_from_string(args);
			break;
			
		case "mbt":
			pythonage_command_make_blue_transparent(args);
			break;
			
		case "upm":
			pythonage_command_update_pixelmap(args);
			break;
			
	} // end of switch
}

function pythonage_command_set_image_data_source(args){
	var object_id = args[1];
	var src = args[2];
	
	if(typeof(pythonage_objects[object_id]) == 'undefined'){
		pythonage_error("Executing set-imagedata-source the the imagedata " + object_id + " did not exist");
		return;
	}
	
	var imagedata = pythonage_objects[object_id];
	imagedata.set_source(src);
}

function pythonage_command_new_image(args){ // args = command, object_id, image_data_source_object_id, height, width, visible
	var object_id = args[1];
	var image_data_object_id = args[2]; 
	var width = parseInt(args[3]);
	var height = parseInt(args[4]);
	
	var visible = false;
	if(args[5]=="t" ||args[5]=="true") visible = true;
	
	new pythonage_image(object_id, image_data_object_id, width, height, visible);
	log("new image");
}

function pythonage_command_new_translate(args){
	var object_id = args[1];
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	
	var visible = false;
	if(args[4]=="t" || args[4]=="true") visible = true;
	
	new pythonage_translate(object_id, x, y, visible);
	log("new translate");
}

function pythonage_command_new_rotate(args){
	var object_id = args[1];
	var deg = parseFloat(args[2]);
	
	var visible = false;
	if(args[3]=="t" || args[3]=="true") visible = true;
	
	new pythonage_rotate(object_id, deg, visible);	
}

function pythonage_command_append(args){
	var object_being_appended_id = args[1];
	var object_to_append_to_id = args[2];
	
	if(typeof(pythonage_objects[object_to_append_to_id]) == 'undefined'){
		pythonage_error("Executing append the object to append to " + object_to_append_to_id + " did not exist");
		return;
	}
	var object_to_append_to = pythonage_objects[object_to_append_to_id];
	
	object_to_append_to.append(object_being_appended_id);	
}

function pythonage_command_detach(args){
	var object_to_detach_id = args[1];
	var object_to_detach_from_id = args[2];	
	
	if(typeof(pythonage_objects[object_to_detach_id]) == 'undefined'){
		pythonage_error("Executing detach the item to be detached" + object_to_detach_id + " did not exist");
		return;
	}
	
	if(typeof(pythonage_objects[object_to_detach_from_id]) == 'undefined'){
		pythonage_error("Executing detach the item to detach from " + object_to_detach_from_id + " did not exist");
		return;
	}
	object_to_detach_from = pythonage_objects[object_to_detach_from_id];

	object_to_detach_from.detach(object_to_detach_id)
}
	
function pythonage_query_keys(args){
	var result = key_listener.query(args.slice(1)); // remove command before asking
	var query_keys_response = "qk," + result;
	web_socket.send(query_keys_response);		
}

function pythonage_command_reset(args){
	var pythonage_objects = {}
}

function pythonage_command_update_image(args){
	var object_id = args[1];
	
	var visible = false;
	if(args[2] == "t" || args[2] == "true") visible = true;
	
	image = pythonage_objects[object_id];
	image.visible = visible
}

function pythonage_command_update_translate(args){
	var object_id = parseInt(args[1]);
	var new_x = parseInt(args[2]);
	var new_y = parseInt(args[3]);
	
	var visible = false;
	if(args[4] == "t" || args[4] == "true") visible = true;
	
	translate = pythonage_objects[object_id];
	translate.x = new_x
	translate.y = new_y
	translate.visible = visible
}

function pythonage_command_update_rotate(args){
	var object_id = args[1];
	var new_angle = parseFloat(args[2]);
	
	var visible = false;
	if(args[3] == "t" || args[3] == "true") visible = true;
	
	rotate = pythonage_objects[object_id];
	rotate.rotation = pythonage_deg_to_radians * new_angle
	rotate.visible = visible
}

function pythonage_command_new_sound(args){
	var object_id = args[1];
	var src = args[2];
	
	new pythonage_sound(object_id, web_socket, src);
}

function pythonage_command_play_sound(args){
	var object_id = args[1];
	pythonage_objects[object_id].play();
}

function pythonage_command_new_pixelmap_from_imagedata(args){
	log("pythonage_command_new_pixelmap");
	var object_id = args[1];
	var imagedata_object_id = args[2];
	var x = parseInt(args[3]);
	var y = parseInt(args[4]);
	
	var visible = false;
	if(args[5] == "t" || args[5] == "true") visible = true
	var new_pixelmap = new pixelmap(object_id, x, y, visible);	
	new_pixelmap.from_imagedata(imagedata_object_id);
	
	pythonage_objects[object_id] = new_pixelmap;
}

function pythonage_command_new_pixelmap_from_string(args){
	var object_id = args[1];
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	var width = parseInt(args[4]);
	var height = parseInt(args[5]);
	var scaling = parseInt(args[6]);
	var string_data = args[7];
	
	var visible = false;
	if(args[8] == "t" || args[8] == "true") visible = true
	var new_pixelmap = new pixelmap(object_id, x, y, visible);
	log("got here")
	new_pixelmap.from_string(width, height, scaling, string_data);
	
	pythonage_objects[object_id] = new_pixelmap;
}

function pythonage_command_make_blue_transparent(args){
	var object_id = args[1];
	var target_pixelmap = pythonage_objects[object_id];
	target_pixelmap.make_blue_transparent();
}

function pythonage_update_pixelmap(args){
	var object_id = args[1];
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	
	var visible = false;
	if(args[4] == "t" || args[4] == "true") visible = true
	
	var target_pixelmap = pythonage_objects[object_id];
	
	target_pixelmap.x = x;
	target_pixelmap.y = y;
	target_pixelmap.visible = visible;	
}