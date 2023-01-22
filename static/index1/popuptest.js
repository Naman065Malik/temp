
// Theme Custom Button
const theme = document.querySelectorAll('.design');
const themeModel = document.querySelector('.customize-theme');
const fontsize = document.querySelectorAll(".choose-size span");
var root = document.querySelector(':root');

const cpallet = document.querySelectorAll(".choose-color span");
const bg1 = document.querySelector(".bg-1");
const bg2 = document.querySelector(".bg-2");
const bg3 = document.querySelector(".bg-3");


// Get the modal
var modal = document.getElementById("myModal");
        
// Get the image and insert it inside the modal - use its "alt" text as a caption
var img123 = document.getElementById("myImg");
var modalImg = document.getElementById("img01");

// Theme Customisation
// open Model


// theme.addEventListener('click', () => {
//     themeModel.style.display = 'grid';
// });
theme.forEach(item => {
    item.addEventListener('click', () => {
    themeModel.style.display = 'grid';
    console.log("hiii")
    });
})
// Close Model
const closethememodel = (e) => {
    if(e.target.classList.contains('customize-theme')){
        themeModel.style.display = 'none';
    }
}
themeModel.addEventListener('click',closethememodel);
// Fonts
const removeselector = () => {
    fontsize.forEach(op => {
        op.classList.remove("active");
    })
}

fontsize.forEach(op => {
    let size;
    
    op.addEventListener("click", () => {
        removeselector();
        op.classList.add("active");

        if(op.classList.contains('font-size-1')){
            size = '10px';
            root.style.setProperty('--sticky-top-left','5.4rem');
            root.style.setProperty('--sticky-top-right','5.4rem');
        }
        if(op.classList.contains('font-size-2')){
            size = '13px';
            root.style.setProperty('--sticky-top-left','5.4rem');
            root.style.setProperty('--sticky-top-right','-7rem');
        }
        if(op.classList.contains('font-size-3')){
            size = '16px';
            root.style.setProperty('--sticky-top-left','-2rem');
            root.style.setProperty('--sticky-top-right','-17rem');
        }
        if(op.classList.contains('font-size-4')){
            size = '19px';
            root.style.setProperty('--sticky-top-left','-5rem');
            root.style.setProperty('--sticky-top-right','-25rem');
        }
        if(op.classList.contains('font-size-5')){
            size = '22px';
            root.style.setProperty('--sticky-top-left','-12rem');
            root.style.setProperty('--sticky-top-right','-35rem');
        }
        // console.log(size);
        document.querySelector('html').style.fontSize = size;
    })    
})

// Color Pallet
const removeselectorcolor = () => {
    cpallet.forEach(op => {
        op.classList.remove("active");
    })
}
cpallet.forEach(op => {
    let color;

    op.addEventListener("click", () => {
        removeselectorcolor();
        
        op.classList.add("active");

        if(op.classList.contains("color-1")){
            color = 252;
        }
        if(op.classList.contains("color-2")){
            color = 52;
        }
        if(op.classList.contains("color-3")){
            color = 352;
        }
        if(op.classList.contains("color-4")){
            color = 152;
        }
        if(op.classList.contains("color-5")){
            color = 202;
        }
        // console.log(color);

        root.style.setProperty("--primary-color-hue", color)
    })
})

// Background

let lightcolorlightness;
let whitecolorlightness;
let darkcolorlightness;

const changeBG = () => {
    root.style.setProperty("--light-color-lightness", lightcolorlightness);
    root.style.setProperty("--white-color-lightness", whitecolorlightness);
    root.style.setProperty("--dark-color-lightness", darkcolorlightness);
}

bg1.addEventListener("click", () => {
    darkcolorlightness = "17%";
    whitecolorlightness = "100%";
    lightcolorlightness = "95%";

    bg1.classList.add("active");
    bg2.classList.remove("active");
    bg3.classList.remove("active");
    changeBG();
    // window.location.reload();
})

bg2.addEventListener("click", () => {
    darkcolorlightness = "95%";
    whitecolorlightness = "20%";
    lightcolorlightness = "15%";

    bg2.classList.add("active");
    bg1.classList.remove("active");
    bg3.classList.remove("active");
    changeBG();
})

bg3.addEventListener("click", () => {
    darkcolorlightness = "95%";
    whitecolorlightness = "10%";
    lightcolorlightness = "0%";

    bg3.classList.add("active");
    bg2.classList.remove("active");
    bg1.classList.remove("active");
    changeBG();
})






var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}







img123.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }
  
  // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() { 
    modal.style.display = "none";
  }