function openclose() {
    if ($('#posting-box').css('display') == 'block') {
      $('#posting-box').hide();
      $('#btn-posting-box').text('포스팅 박스 열기')
    } else {
      $('#posting-box').show();
      $('#btn-posting-box').text('포스팅 박스 닫기')
    }
  }

  $(document).ready(function () {
    $('#cards-box').html('');
    listing();
  });

  function listing() {
    $.ajax({
      type: "GET",
      url: "/memo",
      data: {},
      success: function (response) {
        let articles = response['articles'];
        // if (response['result'] == 'success') {
        //   alert(response['msg']);
        for (let i = 0; i < articles.length; i++) {
          let url = articles[i]["url"];
          let comment = articles[i]["comment"];
          let title = articles[i]["title"];
          let image = articles[i]["image"];
          let description = articles[i]["description"];
          make_card(url, comment, title, image, description);
        }
      }
    })
  }

  function make_card(url, comment, title, image, description) {
    let temp_html = '<div class="card">\
      <img class="card-img-top" src="'+image+'" alt="Card image cap">\
      <div class="card-body">\
        <a href="'+ url + '" class="card-title">' + title + '</a>\
        <p class="card-text">'+ description + '</p>\
        <p class="card-text comment">'+comment+'</p>\
      </div>\
    </div>';
    $('#cards-box').append(temp_html);
  }

  function posting() {
    let url = $('#posting-url').val();
    let comment = $('#posting-comment').val();

    $.ajax({
      type: 'POST',
      url: '/memo',
      data: { url_give: url, comment_give: comment },
      success: function (response) {
        if (response['result'] == 'success') {
          alert('포스팅에 성공하였습니다!');
          window.location.reload();
        } else {
          alert('오류!')
        }
      }
    })
  }