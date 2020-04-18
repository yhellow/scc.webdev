let num = 1;
// 1번 문제
// 기사 저장 버튼을 누를 때마다 1씩 증가해서 alert 
// let num=1; num이라는 변수를 hey라는 함수 밖에 선언해주어야함
function hey() {

    alert(num);
    num = num + 1;
}
// getArticle 함수 
// 간단 코멘트에 치는 내용이 콘솔에 뜨도록 연결
function getArticle() {
    // let value = $('#input_article').val();
    // let value2 = $('#input_comment').val();
    // console.log(value2);
    // alert(value);
    // // 버튼을 누르면 주소가 뜸
    // $("#input_article").val("naver.com")
    // 입력한 값을 저장하고 지워줌
    let value = $('#input_article').val();
    console.log(value);
    $('#input_article').val('');
}
// 버튼 클릭으로 블락 보여주고 숨기기 줄임
function toggleBox() {
    // $('#post-box').hide();
    // .text 함수로 기존 글을 오버라이드
    let box = $('#post-box');
    if (box.is(":visible") === true) {
        box.hide();
        $('#post_button').text("포스팅박스 열기");
        console.log(box.css('display'));
        // box.css({ color: 'red' });
    } else {
        box.show();
        $('#post_button').text("포스팅박스 닫기");
        console.log(box.css('display'));
    }
}
//             let temp_html = '<div class="card">\
//       <img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">\
//       <div class="card-body">\
//         <h5 class="card-title">예를 들면 이렇게 카드가 나옵니다!!</h5>\
//         <p class="card-text">여기에 기사 내용이 들어가겠죠</p>\
//         <p class="card-text comment">여기엔 코멘트가 들어갑니다</p>\
//       </div>\
//     </div>\
//   </div>';
//             //   append 함수는 뒤에 계속 더해줌
//             $('#cards-box').append(temp_html);
//         }
function addCard() {
    let article = $('#input_article').val();
    let comment = $('#input_comment').val();
    let temp_html = `<div class="card">
              <img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">${article}</h5>
                <p class="card-text">여기에 기사 내용이 들어가겠죠</p>
                <p class="card-text comment">${comment}</p>
              </div>
            </div>
          </div>`;
    $('#cards-box').append(temp_html);
}