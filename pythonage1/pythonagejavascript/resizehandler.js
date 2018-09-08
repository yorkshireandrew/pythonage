var TARGET_ASPECT = 2.0;
var ASPECT_TOL = 0.1;
var BORDERING = 0.1;
var TOP_BORDERING = 0.05;

var resized = function(){
	var wh = window.innerHeight;
	var ww = window.innerWidth;
	var asp = ww/wh;
	var canv_top = 0;
	var canv_left = 0;
	var canv_w = 0;
	var canv_h = 0;
	if(asp >= TARGET_ASPECT){
		if(asp > (TARGET_ASPECT + ASPECT_TOL)){asp = TARGET_ASPECT + ASPECT_TOL;}
		border = asp * canv_h * BORDERING;
		canv_h = wh * (1.0-BORDERING);
		canv_w = Math.floor(asp * canv_h - border);
		canv_left = Math.floor((ww - canv_w + border)/2);
		canv_top = Math.floor(canv_h * TOP_BORDERING);
	}
	else{
		if(asp < (TARGET_ASPECT - ASPECT_TOL)){asp = TARGET_ASPECT - ASPECT_TOL;}
		canv_w = ww;
		border = canv_w * BORDERING;
		canv_left = border / 2
		canv_w = canv_w * (1.0 - BORDERING);
		canv_h = Math.floor(canv_w/asp);
		canv_top = Math.floor(canv_h * TOP_BORDERING);

		//canv_top = Math.floor((wh - canv_h)/2);		
	}
	var canvas = document.getElementById('my_canvas');
    canvas.style.position = "absolute";
    canvas.style.width = canv_w + "px";
    canvas.style.height = canv_h + "px";
    canvas.style.left = canv_left + "px";
    canvas.style.top = canv_top + "px";
	
	var log_el = document.getElementById('log');
    log_el.style.position = "absolute";
	log_top = (canv_top + canv_h + 20)
    log_el.style.top = ""+log_top+ "px";
};

// Do not forget to call resized after page load too
window.onresize = function(event) {resized();};