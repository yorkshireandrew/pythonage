
// Query the loaded state of an album, Returns 999 if the album is empty
function pythonage_album_pending_loads(album_name){
	if(typeof(pythonage_albums[album_name]) == 'undefined') pythonage_error("When querying if an album has loaded the album " + album_name + " did not exist")
	var album = pythonage_albums[album_name];
	if(Object.keys(album).length == 0) return 999; // Paradox
	var count = 0;
	for(var image_data in album){
		if(image_data.loaded == false)count++;
	}
	return count;	
}

//Query the number of images in an album, Returns 999 if the album is empty
function pythonage_album_image_count(album_name){
	if(typeof(pythonage_albums[album_name]) == 'undefined') pythonage_error("When querying if an album has loaded the album " + album_name + " did not exist")
	var album = pythonage_albums[album_name];
	if(Object.keys(album).length == 0) return 999; // Paradox
	return Object.keys(album).length;
}