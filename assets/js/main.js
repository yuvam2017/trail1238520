function showSlider(){
    document.getElementById("slider-content").style.left = "0%";
    document.getElementById("close-btn").style.left= "17%";
}

function hideSlider() {
    document.getElementById("slider-content").style.left = "-100%";
    document.getElementById("close-btn").style.left= "-100%";
}
function showDropdown(idElement) {
    var styleidElement = document.getElementById(idElement);
    if (styleidElement.style.display === "none"){
        styleidElement.style.display = "block";
    } else {
        styleidElement.style.display = "none";
    } 
}

