document.querySelectorAll(".drag-drop-input").forEach((inputElement) => {
  const dragDropElement = inputElement.closest(".drag-drop");

  dragDropElement.addEventListener("click", (e) => {
    inputElement.click();
  });


  inputElement.addEventListener("change", (e) => {
    if (inputElement.files.length) {
      updatethumbnail(dragDropElement, inputElement.files[0]);
    } 
  });  

  dragDropElement.addEventListener('dragover', (e) => {
    e.preventDefault();
    dragDropElement.classList.add("drag-drop-over");
  });

  ["dragleave", "dragend"].forEach((type) => {
    dragDropElement.addEventListener(type, (e) => {
      dragDropElement.classList.remove("drag-drop-over");
    });

  });

  dragDropElement.addEventListener("drop", e => {
    e.preventDefault();

    if (e.dataTransfer.files.length) {
      inputElement.files = e.dataTransfer.files;
      // updatethumbnail(dragDropElement, e.dataTransfer.files[0]);
    }
  });

  dragDropElement.classList.remove("drag-drop-over");
});









 
function updatethumbnail(dragDropElement, file) {
  let thumbnailElement = dragDropElement.querySelector(".drag-drop-thumb");

  if (file.type=="application/vnd.openxmlformats-officedocument.wordprocessingml.document") {
    const reader = new FileReader();
    console.log("Hello");
    reader.readAsDataURL(file);
    reader.onload = () => {

      if (dragDropElement.querySelector('.drag-drop-tag'))
        dragDropElement.querySelector('.drag-drop-tag').remove();

      if (dragDropElement.querySelector('.drag-drop-img'))
        dragDropElement.querySelector('.drag-drop-img').remove();


      if (!thumbnailElement) {
        thumbnailElement = document.createElement('div');
        thumbnailElement.classList.add("drag-drop-thumb");
        dragDropElement.appendChild(thumbnailElement);
      }

      thumbnailElement.style.backgroundImage = `url('image/docs.png')`;
      thumbnailElement.dataset.label = file.name;
      
    };
  }
  else
    alert("You can only choose doc/docx file. Try uploading doc/docx file")

}

