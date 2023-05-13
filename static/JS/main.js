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

let input = document.getElementById("input-img")

input.addEventListener("change", (e)=>{
    document.querySelector(".upload-style").style.display = "none"
})