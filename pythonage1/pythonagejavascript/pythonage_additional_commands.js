// Commands the parser can call on which are not related to a specific object type

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

function pythonage_command_set_render_completed_notification(args){
	
	if(args[1] == "t")
	{
		pythonage_notify_render_completed = true;
	}
	else
	{
		pythonage_notify_render_completed = false;
	}
	
}

function pythonage_command_set_layer(args){
	var object_id = args[1];
	var layer = parseInt(args[2]);
	pythonage_objects[object_id].layer = layer;
}

function pythonage_command_log(args){
	var to_log = args[1].split("{{comma}}").join(",");
	log(to_log);
}

function pythonage_command_update_scale(args){
	var object_id = args[1];
	var scale = parseFloat(args[2]);
	pythonage_objects[object_id].scale = scale;
}