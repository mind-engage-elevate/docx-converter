var myData = localStorage['objectToPass'];
localStorage.removeItem( 'objectToPass' );

var y=JSON.parse(myData);
var z=y['Destination File Path'];
var img_src="../backend/output_files/" + z;

// Changing the file name for the download option
$('#dwnld_link').attr('href', img_src) ;
href=img_src;

var img=$('<iframe id="image_id" height="450" width="100%" style="border:none;">');
img.attr('src', img_src);
img.appendTo('#result');

