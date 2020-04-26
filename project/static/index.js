let trending = [];

$(document).ready(function(){
    showtrending();      
});

function gamesearch(){
    let search = $('.searchtext').val();
    if (search == ''){
        alert('Please type game name')
    }
    let steamurl = 'https://store.steampowered.com/search/?term='+search;
    
    window.open(steamurl, 'blank');
};

function showtrending(){
    $.ajax({
        type: "GET",
        url: "/home",
        data: {},
        success: function(response){
            if(response["result"]=="success"){
                trending = response["trending"];

                trending.forEach(function (data, index) {
                    $(`<div class="carousel-item ${index === 0 ? 'active': ''}"><img class="d-block img-fluid" src="${data['image']}"></div>`).appendTo('.carousel-inner')
                    $(`<li data-target="#carouselExampleControls" data-slide-to="${index}" ${index === 0 ? 'class="active"' : ''}></li>`).appendTo('.carousel-indicators')
                });

                $('.trending .title').text(trending[0]['title']);
                $('.discounted').text(trending[0]['price']);
                $('.user-tags').text(trending[0]['tag']);
                // $('.') for tags
                $('.game-url').attr("href", trending[0]['url']);
                $('.gamereview').text(trending[0]['review']);

                $('.description').text(trending[0]['desc']);
            }
        }
    });
};

function getTrending() {
    const indicators = $('.carousel-indicators li');
    indicators.each(function(index) {
        if ($(this).hasClass('active')) {
            let currentIndex;
            if (index === 2) {
                currentIndex = 0;
            } else {
                currentIndex = index + 1;
            }
            $('.game-url').attr("href", trending[currentIndex]['url']);

            $('.trending .title').text(trending[currentIndex]['title']);
            $('.description').text(trending[currentIndex]['desc']);
            $('.gamereview').text(trending[currentIndex]['review']);
            $('.discounted').text(trending[currentIndex]['price']);
            $('.user-tags').text(trending[currentIndex]['tag']);
        }
    });
}


function random(){
    $.ajax({
        type: 'GET',
        url: '/random',
        data: {},
        success: function(response){
            if (response['result']== 'success'){
                // 부트스트랩 $('.alert').alert() 사용?
                let temp_html = ``
                $('.alert').alert(temp.html)
            }
        }
    })
};

    // $.ajax({
    //     type: 'POST',
    //     url: '/search',
    //     data: {
    //         'search_give': search
    //     },
    //     success: function(response){
    //         if (response['result']== 'success'){
    //             // 바로 스팀서치페이지로 가는 방법
    //             // change alert message to go to steampage for 'search'
    //             alert(response["search"]);
    //             window.location.reload();
    //         }
    //     }
    // })


    // $('.leadtitle').text(response["title"]);
    //             $('.d-block').attr('src',response["image"])