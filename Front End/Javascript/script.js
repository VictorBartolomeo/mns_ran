function evenementOver(e){
    e.srcElement.classList.add("Test")
}
const articles=document.querySelectorAll("body>article");

for(let art of articles){
    art.addEventListener("mouseover", evenementOver);
}

