document.addEventListener('DOMContentLoaded', function() {
    const submit = document.querySelector('#submit');
    const title = document.querySelector('#title_form');
    submit.disable = true;
    if( title.ariaValueMax.length > 0)
    {
        submit.disabled = false;
    }
    else{
        submit.disable = true;
    }

    document.querySelector('form').onsubmit = ()=> {
        submit.disable = true;
        return false;
    }
});