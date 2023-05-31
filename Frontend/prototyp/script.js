const searchButton = document.querySelector(".search-button")
const kitchenAcesoriesBtn = document.querySelector(".accessories")
const kitchenAcesories = document.querySelector(".kitchen-accessories")
const accesoriesList = document.querySelector('.kitchen-accessories-list')    
const header = document.querySelector('.header');
const container = document.querySelector(".container")
const rateBox = container.querySelector(".stars")




const showList = () => {
    accesoriesList.style.display = "flex"
    kitchenAcesoriesBtn.classList.add("accessories-button-hover")
}

const hideList = () =>{
    accesoriesList.style.display = "none"
    kitchenAcesoriesBtn.classList.remove("accessories-button-hover")
}
const stickyHeader = () => {
    if (window.pageYOffset > 0) {
        header.classList.add('sticky-header');
        container.style.marginTop = "155px";
    } else {
        header.classList.remove('sticky-header');
        container.style.marginTop = "20px";
    }
}

const addToOrderList = e => {
    if(e.target.classList.contains("fa-solid") && e.target.classList.contains("fa-heart")){
        e.target.classList.remove('fa-solid')
    } else if(e.target.classList.contains("fa-heart")) {
        e.target.classList.add('fa-solid')
    }
}

const rating = e => {
    if (!e.target.classList.contains("fa-star")){
        return
    }
    const rateBox = e.target.closest(".stars")
    let stars = rateBox.querySelectorAll("i")
    let indexOfStar = Array.prototype.indexOf.call(stars, e.target)
    for (let i = 0; i <stars.length; i++){
        if (i <= indexOfStar){
            stars[i].classList.add("fa-solid")
        } else if(stars[i].classList.contains("fa-solid")){
            stars[i].classList.remove("fa-solid")
        }
    }

}


kitchenAcesoriesBtn.addEventListener('mouseover',showList)
kitchenAcesories.addEventListener('mouseleave',hideList)
searchButton.addEventListener('click', () => {console.log("HI")} )
window.addEventListener('scroll', stickyHeader)
container.addEventListener('click', addToOrderList)
container.addEventListener('click', rating)  
