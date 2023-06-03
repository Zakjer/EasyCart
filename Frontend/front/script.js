const minusBtn = document.querySelector('.fa-minus')
const plusBtn = document.querySelector('.fa-plus')
const amount  = document.querySelector('.amount-input')

const increaseAmount = () => {
    amount.value = Number(amount.value) + 1
}

const decreaseAmount = () => {
    if (Number(amount.value) > 1){
        amount.value = Number(amount.value) - 1
    }
}

minusBtn.addEventListener('click', decreaseAmount)
plusBtn.addEventListener('click', increaseAmount)