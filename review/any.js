$(document).ready(function(){
    saving();
})

function saving(){
    $.ajax({
        type: 'GET',
        url: '/apiName',
        data: {},
        success: function(response){
            if(response['resutl']== 'success'){
                alert(response['result'])
            }
        }
    })
}