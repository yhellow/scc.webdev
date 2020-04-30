$(document).ready(function(){
    somefuncName();
})

function somefuncName(){
    $.ajax({
        type: 'GET',
        url: '/apiName',
        data: {},
        success: function(response){
            if(response['result']= 'success'){
                alert(response['result'])
            }
        }
    })
}