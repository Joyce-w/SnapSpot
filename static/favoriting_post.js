
const $favBtn = document.getElementById('favBtn')

$('form').on('click', $('svg'), function (e) {

    if (e.target.parentElement.className = "uk-text-muted uk-icon") {
        e.target.parentElement.className="uk-text-warning uk-animation-shake uk-icon"        
    }
    else if(e.target.parentElement.className = "uk-text-warning uk-icon") {
        e.target.parentElement.className="uk-text-muted uk-animation-shake uk-icon" 
    }

})


