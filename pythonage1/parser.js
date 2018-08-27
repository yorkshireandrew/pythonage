var pythonage_input_stream = "";
var pythonage_notify_render_completed = false;

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
			if(pythonage_notify_render_completed) 	web_socket.send('rc');	
			break;
			
		case "r":
			pythonage_objects[args[1]].render(canvas_context);
			if(pythonage_notify_render_completed) 	web_socket.send('rc');	
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
			
		case "nl":
			pythonage_command_new_line(args);
			break
			
		case "ul":
			pythonage_command_update_line(args);
			break;
			
		case "ntxt":
			pythonage_command_new_text(args)
			break;
			
		case "utxt":
			pythonage_command_update_text(args)
			break;
			
		case "srcn":
			pythonage_command_set_render_completed_notification(args);
			break;
			
		case "sl":
			pythonage_command_set_layer(args);
			break;
			
		case "rl":
			var target = pythonage_objects[args[1]];
			target.renderlayer(canvas_context, 0);
			target.renderlayer(canvas_context, 1);
			target.renderlayer(canvas_context, 2);
			target.renderlayer(canvas_context, 3);
			target.renderlayer(canvas_context, 4);
			if(pythonage_notify_render_completed) 	web_socket.send('rc');	
			break;
			
		case "log":
			pythonage_command_log(args);
			break;
			
		case "usc":
			pythonage_command_update_scale(args);
			break;
			
		case "nc":
			pythonage_command_new_circle(args);
			break;
			
		case "uc":
			pythonage_command_update_circle(args);
			break;
					
	} // end of switch - do not forget to break
}



