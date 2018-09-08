// ================== pixelmap ===========================
class pythonage_pixelmap{
	
	constructor(object_id, width, height, visible){
		this.object_id = object_id;
		this.render_width = width;
		this.render_height = height;
		this.visible = visible;
		
		// Additional construction
		this.width = 0; // data width
		this.height = 0; // data height
		this.canvas2 = null;
		this.layer = 0;
		this.data = null;
		this.renderable = null;
		this.scale = 1.0;
	}
	
	from_imagedata(imagedata_object_id){
		var temp_canvas = document.createElement('canvas');
		var temp_context = temp_canvas.getContext('2d');
		var img = pythonage_objects[imagedata_object_id].img;
		temp_context.drawImage(img, 0, 0);
		this.data = temp_context.getImageData(0, 0, img.width, img.height);
		this.width = img.width;
		this.height = img.height;
		this.renderable = img;
	}
	
	make_blue_transparent(){
		var write_index = 0;
		var pix = this.data.data;
		var pix_count = this.width * this.height;
		for(var count = 0; count < pix_count; count++){			
			if(
				(pix[write_index + 0] == 0) &&
				(pix[write_index + 1] == 0) &&
				(pix[write_index + 2] == 255)
			){
				pix[write_index + 0] = 0;
				pix[write_index + 1] = 0;
				pix[write_index + 2] = 0;
				pix[write_index + 3] = 0;	
			}
			
			write_index += 4;
		}
		
		this.renderable = this.imagedata_to_image(this.data);
	}
	
	imagedata_to_image(imagedata) {
	    var canvas = document.createElement('canvas');
	    var ctx = canvas.getContext('2d');
	    canvas.width = imagedata.width;
	    canvas.height = imagedata.height;
	    ctx.putImageData(imagedata, 0, 0);

	    var image = new Image();
	    image.src = canvas.toDataURL();
	    return image;
	}
	
	from_string(width, height, oversample, string_data){
		var colour_data = {
				'w': [255,255,255,255],
				'r': [200,50,50,255],
				'g': [50,200,50,255],
				'b': [50,50,200,255],
				'R': [255,0,0,255],
				'G': [0,255,0,255],
				'B': [0,0,255,255],
				'y': [200,200,50,255],
				'Y': [255,255,0,255],
				'p': [253,207,176,255], // Pink
				'#': [0,0,0,255],
				'm': [185,122,87,255], // Light mud
				'M': [119,70,49,255],  // Dark mud
				'o': [255,176,89,255], // Light orange
				'O': [255,127,39,255], // Orange
				' ': [0,0,0,0]
		}
		
		var canvas2 = document.createElement('canvas');
		var context2 = canvas2.getContext('2d');
		var data = context2.createImageData(width * oversample, height * oversample);
		this.width = width * oversample;
		this.height = height * oversample;
		var read_index = 0;
		var write_index = 0;
		for(var y = 0; y < height; y++){
			for(var os1 = 0; os1 < oversample; os1++){
				read_index = y * width;
					for(var x = 0; x < width; x++){
						var to_fill = colour_data[string_data[read_index++]];
						for(var os2 = 0; os2 < oversample; os2++){
							data.data[write_index++] = to_fill[0];
							data.data[write_index++] = to_fill[1];
							data.data[write_index++] = to_fill[2];
							data.data[write_index++] = to_fill[3];
						}
					}
			}
		}
		this.renderable = this.imagedata_to_image(data);	
	}
	
	render(context){
		var sc = this.scale;
		if(this.visible) context.drawImage(this.renderable, 0, 0, this.width, this.height, 0, 0, Math.floor(this.render_width * sc), Math.floor(this.render_height * sc));
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
	
}

function pythonage_command_new_pixelmap_from_imagedata(args){
	
	var object_id = args[1];
	var imagedata_object_id = args[2];
	var width = parseInt(args[3]);
	var height = parseInt(args[4]);
	
	var visible = false;
	if(args[5] == "t") visible = true
	
	var new_pixelmap = new pythonage_pixelmap(object_id, width, height, visible);	
	new_pixelmap.from_imagedata(imagedata_object_id);
	
	pythonage_objects[object_id] = new_pixelmap;
}

function pythonage_command_new_pixelmap_from_string(args){
	
	var object_id = args[1];
	var width = parseInt(args[2]);
	var height = parseInt(args[3]);	
	var data_width = parseInt(args[4]);
	var data_height = parseInt(args[5]);
	var oversample = parseInt(args[6]);
	var string_data = args[7];
	
	var visible = false;
	if(args[8] == "t") visible = true
	
	var new_pixelmap = new pythonage_pixelmap(object_id, width, height, visible);
	new_pixelmap.from_string(data_width, data_height, oversample, string_data);
	
	pythonage_objects[object_id] = new_pixelmap;
}

function pythonage_command_make_blue_transparent(args){
	
	var object_id = args[1];
	var target_pixelmap = pythonage_objects[object_id];
	target_pixelmap.make_blue_transparent();
}

function pythonage_update_pixelmap(args){
	
	var object_id = args[1];
	
	var visible = false;
	if(args[4] == "t") visible = true
	
	var target_pixelmap = pythonage_objects[object_id];
	target_pixelmap.width = parseInt(args[2]);
	target_pixelmap.height = parseInt(args[3]);
	target_pixelmap.visible = visible;	
}