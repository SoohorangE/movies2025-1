let MovieObject = {
    init: function() {

    },

    getall: function() {
        $.ajax({
            // 실행 코드
            type: "GET",
            url: "http://localhost:8000/all",
        }).done(function(response) {
            // 성공
            movielist = response.result

            // topdiv = document.getElementById("div")
            // topdiv.style = "column-count:5"
            // document.body.appendChild(topdiv)

            topdiv = document.getElementById("alldiv")

            movielist.forEach(movie => {

                cmovie = document.createElement("div")
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function() {
                    // location.href 현재창에서 열기
                    // window.open 새창으로 열기
                    window.open(movie.url)
                }

                mimg.onmouseover = function(){
                    mimg.style.cursor = "pointer"
                }

                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            })
        }).fail(function(error) {
            // 실패
            console.log(error)
        })
    }
}

MovieObject.init();
MovieObject.getall();