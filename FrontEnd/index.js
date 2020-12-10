function upload(input) {
  var xhttp = new XMLHttpRequest();
  var data = new FormData();
  data.append("file", document.getElementById('file').files[0], "/C:/Users/patil/OneDrive/Documents/ASU/Fall2020/EEE511/Project/API/image_captioning/png/example.png");
  xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 201) {
           var jsonResponse = JSON.parse(this.responseText);
           document.getElementById('caption').innerHTML = jsonResponse.caption;
 
       }
  };
  xhttp.open("POST", "http://127.0.0.1:5000/file-upload", true);
  console.log(data);
  xhttp.send(data);
}

function readURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#blah')
              .attr('src', e.target.result);
      };

      reader.readAsDataURL(input.files[0]);
  }
}