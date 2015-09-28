$(function(){

	$.getJSON('tophacks.js',function(data){
		$('#topcontainer').append('<div class="row">');
		$.each(data,function(i,value){
			$('#topcontainer').append('<div class="span12 center" style = "padding: 0px 10px;">\
          <a href="#team'+value.team+'" data-toggle="modal">\
          <div class="larger view view-first">\
              <img src="images/hacks/team'+value.team+'.jpg" />\
              <div class="mask larger">\
                  <h2>'+value.title+'</h2><br>\
              </div>\
          </div> \
        </a>\
        </div>\
        <!-- Modal Start -->\
<div id="team'+value.team+'" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\
  <div class="modal-header">\
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\
    <h3 id="myModalLabel">'+value.title+'</h3>\
  </div>\
  <div class="modal-body">\
  <div class="text-center">\
    <p><img src="images/hacks/team'+value.team+'.jpg" />\
    </div><div class="text-left">\
      <strong>Description:</strong><br>\
    '+value.description+'<br>\
    <strong>Technical Details:</strong><br>\
    '+value.details+'\
      </p>\
      </div>\
  </div>\
  <div class="modal-footer">\
    <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>\
  </div>\
</div>');
		});
		$('#topcontainer').append('</div>');
	});

	$.getJSON('hacks.js',function(data){
		$.each(data,function(i,value){
			$('#maincontainer').append('<div class="span8 center" style = "padding: 0px 10px;">\
          <a href="#team'+value.team+'" data-toggle="modal">\
          <div class="view view-first">\
              <img src="images/hacks/team'+value.team+'.jpg" />\
              <div class="mask">\
                  <h2>'+value.title+'</h2><br>\
              </div>\
          </div> \
        </a>\
        </div>\
        <!-- Modal Start -->\
<div id="team'+value.team+'" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\
  <div class="modal-header">\
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\
    <h3 id="myModalLabel">'+value.title+'</h3>\
  </div>\
  <div class="modal-body"><div class="text-center">\
    <p><img src="images/hacks/team'+value.team+'.jpg" />\
    </div><div class="text-left">\
      <strong>Description:</strong><br>\
    '+value.description+'<br>\
      </p>\
      </div>\
  </div>\
  <div class="modal-footer">\
    <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>\
  </div>\
</div>');
		});
	});
})