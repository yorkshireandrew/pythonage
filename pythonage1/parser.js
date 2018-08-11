var pythonage_input_stream = "";

function pythonage_consume(nugget){
	pythonage_input_stream += nugget;
	fragments = pythonage_input_stream.split("(");
	var frag_length = fragments.length
	var frag_length_minus_one = frag_length-1;
	if(frag_length > 1){
		for(var fragment_index in fragments){
			var frag = fragments[fragment_index];
			if(frag.length == 0) continue;
			
			if(frag.endsWith(")")){
				pythonage_continue_parse(frag.slice(0,-1));
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

function pythonage_continue_parse(commandstring){
	var args = commandstring.split(",");
	
	var command = args[0];
	var number_of_arguments = args.length -1;
	
	switch(command){
	
		case "new-album":
			if(number_of_arguments == 1){pythonage_add_album(args[1]);}
			break;
			
		case "na":
			if(number_of_arguments == 1){pythonage_add_album(args[1]);}
			break;
			
		case "new-imgd":
			if(number_of_arguments == 2){new pythonage_imagedata(args[1],args[2]);}
			break;
			
		case "nid":
			if(number_of_arguments == 2){new pythonage_imagedata(args[1],args[2]);}
			break;
		
		case "set-imgd-src":
			if(number_of_arguments == 3){pythonage_command_set_image_data_source(args);}
			break;
			
		case "sids":
			if(number_of_arguments == 3){pythonage_command_set_image_data_source(args);}
			break;
			
		case "new-img":
			if(number_of_arguments == 6){pythonage_command_new_image(args);}
			break;
			
		case "ni":
			if(number_of_arguments == 6){pythonage_command_new_image(args);}
			break;
			
		case "new-tran":
			if(number_of_arguments == 4){pythonage_command_new_translate(args);}
			break;
			
		case "nt":
			if(number_of_arguments == 4){pythonage_command_new_translate(args);}
			break;
			
		case "new-rot":
			if(number_of_arguments == 4){pythonage_command_new_rotate(args);}
			break;
			
		case "nr":
			if(number_of_arguments == 3){pythonage_command_new_rotate(args);}
			break;
		
		case "attach-img":
			if(number_of_arguments == 2){pythonage_command_attach_image(args);}
			break;
			
		case "ai":
			if(number_of_arguments == 2){pythonage_command_attach_image(args);}
			break;
			
		case "attach-sgi":
			if(number_of_arguments == 2){pythonage_command_attach_scene_graph_item(args);}
			break;
			
		case "asgi":
			if(number_of_arguments == 2){pythonage_command_attach_scene_graph_item(args);}
			break;
			
		case "attach-to":
			if(number_of_arguments == 2){pythonage_command_attach_to(args);}
			break;
			
		case "at":
			if(number_of_arguments == 2){pythonage_command_attach_to(args);}
			break;
			
		case "render":
			if(number_of_arguments == 1){pythonage_scene_graph[args[1]].render(canvas_context);}
			break;
			
		case "r":
			if(number_of_arguments == 1){pythonage_scene_graph[targetname]}
			break;
			
	} // end of switch
}

function pythonage_command_set_image_data_source(args){
	var album_name = args[1];
	if(typeof(pythonage_albums[album_name]) == 'undefined'){
		pythonage_error("Executing set-imagedata-source the album " + album_name + " did not exist");
		return;
	}
	var album = pythonage_albums[album_name];
	var image_data_name = args[2];
	if(typeof(album[image_data_name]) == 'undefined'){
		pythonage_error("Executing set-imagedata-source the the imagedata " + image_data_name + " did not exist in album " + album_name);
		return;
	}
	var imagedata = album[image_data_name];
	imagedata.set_source(args[3]);
}

function pythonage_command_new_image(args){
	var width = parseInt(args[4]);
	var height = parseInt(args[5]);
	var visible = false;
	if(args[6]=="t" ||args[6]=="true") visible = true;		
	new pythonage_image(args[1],args[2],args[3], width, height, visible);
	log("new image");
}

function pythonage_command_new_translate(args){ 
	var x = parseInt(args[2]);
	var y = parseInt(args[3]);
	var visible = false;
	if(args[4]=="t" || args[4]=="true") visible = true;		
	new pythonage_translate(args[1],x,y, visible);
	log("new translate");
}

function pythonage_command_new_rotate(args){ 
	var deg = parseFloat(args[2]);
	var visible = false;
	if(args[3]=="t" || args[3]=="true") visible = true;		
	new pythonage_rotate(args[1],deg, visible);	
}

function pythonage_command_attach_image(args){
	var targetname = args[1];
	if(typeof(pythonage_scene_graph[targetname]) == 'undefined'){
		pythonage_error("Executing attach-image the the target scene graph item " + targetname + " did not exist");
		return;
	}
	var target = pythonage_scene_graph[targetname];
	target.attach_image(args[2])	
}

function pythonage_command_attach_scene_graph_item(args){
	var targetname = args[1];
	if(typeof(pythonage_scene_graph[targetname]) == 'undefined'){
		pythonage_error("Executing attach-scene-graph-item the target scene graph item " + targetname + " did not exist");
		return;
	}
	var target = pythonage_scene_graph[targetname];
	target.attach_scene_graph_item(args[2])	
}

function pythonage_command_attach_to(args){
	var targetname = args[1];
	if(typeof(pythonage_scene_graph[targetname]) == 'undefined'){
		pythonage_error("Executing attach-to the scene graph item to be moved" + targetname + " did not exist");
		return;
	}
	var target = pythonage_scene_graph[targetname];
	target.attach_scene_graph_item(args[2])	
}

