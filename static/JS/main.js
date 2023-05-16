function getCursor(event) {
    let x = event.clientX;
    let y = event.clientY;
    const infoElement = document.getElementById('purple-const');
    infoElement.style.top = (y - 400) + "px";
    infoElement.style.left = (x - 400) + "px";
}

document.addEventListener("mousemove", getCursor)

let modeSelection = document.getElementsByClassName("mode")

document.addEventListener("click", (e)=>{
    if(e.target.classList.contains("mode")){
        for(i=0;i<modeSelection.length;i++){
            modeSelection[i].classList.remove("active-mode")
        }
        e.target.classList.add("active-mode")
    }
})


upload = document.getElementById("upload");
inputImg = document.getElementById("input");
outputImg = document.getElementById("output");

upload.addEventListener('change' , (e) => {
    console.log(e)
    const reader = new FileReader();
    reader.onload = (e) => {
    if (e.target){
        //upload image
        let img = document.createElement("img");
        img.style.height= 'inherit';
        img.id = "img";
        img.src = e.target.result;
        //clean previous image
        inputImg.innerHTML = " ";
        //add  image 
        inputImg.appendChild(img); 
    }
    };
    //read&send the img
    img_send =  e.target.files[0];
    reader.readAsDataURL(img_send);
    imgToFlask("input_img",img_send,"input_img","/input") 
    });


function imgToFlask(name , data ,filename , route){
    var xhr=new XMLHttpRequest();
    var fd=new FormData();
    fd.append(name,data ,filename);
    xhr.onreadystatechange = function() {
        if (xhr.status == 200) {
            var timestamp = new Date().getTime();
            console.log(xhr.responseText)
            document.getElementById('detected').innerHTML = "Number of detected faces:"+ JSON.parse(xhr.responseText)[0]
            +"&nbsp; &nbsp; &nbsp;"+"Recognized:"+JSON.parse(xhr.responseText)[1];
            output = document.createElement('img')
            output.style.height= 'inherit';
            output.src = "./static/Imgs/output_img.jpg" +'?t=' + timestamp;
            outputImg.innerHTML = " ";
            outputImg.appendChild(output); 
        }
        }; 
    xhr.open("POST",route,true);
    xhr.send(fd);
    console.log(fd)
};
function checkIfImageExists(url, callback) {
    const img = new Image();
    img.src = url;
    
    if (img.complete) {
        callback(true);
    } else {
        img.onload = () => {
        callback(true);
    };
        img.onerror = () => {
        callback(false);
        };
    }
};