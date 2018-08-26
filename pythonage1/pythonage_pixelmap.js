// ================== pixelmap ===========================
class pythonage_pixelmap{
	
	constructor(object_id, x, y, visible){
		this.object_id = object_id;
		this.data = null;
		this.visible = visible;
		this.width = 0;
		this.height = 0;
		this.x = x;
		this.y = y;
		this.canvas2 = null;
		this.layer = 0;
	}
	
	from_imagedata(imagedata_object_id){
		var temp_canvas = document.createElement('canvas');
		var temp_context = temp_canvas.getContext('2d');
		var img = pythonage_objects[imagedata_object_id].img;
		temp_context.drawImage(img, 0, 0);
		this.data = temp_context.getImageData(0, 0, img.width, img.height);
		this.width = img.width;
		this.height = img.height;
		this.canvas2 = temp_canvas;
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
		var temp_context = this.canvas2.getContext('2d');
		temp_context.putImageData(this.data,0,0);
	}
	
	from_string(width, height, scaling, string_data){
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
		var data = context2.createImageData(width * scaling, height * scaling);
		this.width = width * scaling;
		this.height = height * scaling;
		var read_index = 0;
		var write_index = 0;
		for(var y = 0; y < height; y++){
			for(var sc = 0; sc < scaling; sc++){
				read_index = y * width;
				for(var x = 0; x < width; x++){
					var to_fill = colour_data[string_data[read_index++]];
					for(var sc2 = 0; sc2 < scaling; sc2++){
						data.data[write_index++] = to_fill[0];
						data.data[write_index++] = to_fill[1];
						data.data[write_index++] = to_fill[2];
						data.data[write_index++] = to_fill[3];
					}
				}					
			}		
		}
		context2.putImageData(data,0,0);
		this.canvas2 = canvas2;		
	}
	
	render(context){
		if(this.visible) context.drawImage(this.canvas2, this.x, this.y);
	}
	
	renderlayer(context, layer){
		if(this.layer == layer) this.render(context);
	}
	
}