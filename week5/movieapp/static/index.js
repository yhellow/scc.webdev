$(document).ready(function() {
    // index.html 로드가 완료되면 자동으로 show_star() 함수를 호출합니다.
    show_star();
  });

    function show_star(){
          $.ajax({
              type: 'GET',
              url:  '/api/list',
              data: {},
              success: function (response) {
                        if (response['result'] == 'success') {
            let data = response['data'];
            console.log(data);

            for(let i = 0; i < data.length; i++) {
              let name = data[i]["name"];
              let recent = data[i]["recent"];
              let image_url = data[i]["img_url"];
              let like = data[i]["like"];
              let url = data[i]["url"];

              let html = `
                <div class="card">
                  <div class="card-content">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-48x48">
                          <img
                            src="${image_url}"
                            alt="Placeholder image"
                          />
                        </figure>
                      </div>
                      <div class="media-content">
                        <a href="${url}" target="_blank" class="star-name title is-4">${name} (좋아요: ${like})</a>
                        <p class="subtitle is-6">${recent}</p>
                      </div>
                    </div>
                  </div>
                  <footer class="card-footer">
                    <a href="#" onclick="like_star('${name}')" class="card-footer-item has-text-info">
                      위로!
                      <span class="icon">
                        <i class="fas fa-thumbs-up"></i>
                      </span>
                    </a>
                    <a href="#" onclick="delete_star('${name}')" class="card-footer-item has-text-danger">
                      삭제
                      <span class="icon">
                        <i class="fas fa-ban"></i>
                      </span>
                    </a>
                  </footer>
                </div>
              `;
            
              $('#star-box').append(html);
            }
                        }
              }
          });
        }
        
  function like_star(name){
      $.ajax({
          type: 'POST',
          url:  '/api/like',
          data: {
            "name_give": name
          },
          success: function (response) {
              if (response['result'] == 'success') {
                                    $('#star-box').empty();
                show_star();
              }
          }
      });
  }

  function delete_star(name){
      $.ajax({
          type: 'POST',
          url:  '/api/delete',
          data: {
            "name_give": name
          },
          success: function (response) {
              if (response['result'] == 'success') {
                $('#star-box').empty();
                show_star();
              }
          }
      });
  }