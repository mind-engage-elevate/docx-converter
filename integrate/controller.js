$(document).ready(function () {
    $('#before_upload').show()
    $('#loading_page').hide()
    $('#sub_btn').click(function (event) {
        event.preventDefault();
        if(check()==false)
            errorresponse("Please select a docx file and required format...");
        else
        {
            $('#loading_page').show()
            $('#before_upload').hide()
            callapi();
        }
    });

    function check()
    {  
        var pdf=document.getElementById('PDF');
        var xml=document.getElementById('XML');
        var txt=document.getElementById('TXT');
        var file_length=document.form.upload_file.value.length;
        if((pdf.checked == true || xml.checked == true || txt.checked == true) && file_length!=0)
            return true;
        else 
         return false; 
    }

    function callapi() 
    {                  
        var form = $('#fileUploadForm')[0];
        var dataarr=$('form').serializeArray();
        var data = new FormData(form);
        // console.log(hello'); 
        var ajxreq=$.ajax({ 
            type: "POST",
            enctype: 'multipart/form-data',
            url: "http://127.0.0.1:8000/upload-file",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
        });
        
        ajxreq.success( function (data) {
                data=JSON.stringify(data);  
                if(data=="Found some error")
                  {
                    $('#before_upload').show();
                    $('#loading_page').hide();
                    errorresponse("Error converting document...");
                    return;
                  }  
                $('#before_upload').show();
                $('#loading_page').hide();
               
                localStorage.setItem( 'objectToPass', data );
                window.location="last.html"; 
                return true;
        });
        ajxreq.error( function (e) {
                errorresponse("Error converting document...");
                return false;
        })
    }
    return false;
});
   
function errorresponse(message){
    document.getElementById('msg').innerHTML= message;
    var modal=document.getElementById('modal')
    modal.style.display = "block";
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }

    return;
}
