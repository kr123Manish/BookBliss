function search(){
        let filter = document.getElementById('my-input').value.toUpperCase();
        let x = document.getElementsByClassName('Box-filter');
        for (var i = 0; i < x.length; i++) {

          let a = x[i].children[0];
          
          let b = a.children[1];

          let book_name = b.children[1];
            // console.log(book_name.children[1]);
          if (book_name.children[1]) {
              let textvalue = book_name.textContent || book_name.innerHTML;
              // console.log(textvalue);
              if (textvalue.toUpperCase().indexOf(filter) > -1) {
                  x[i].style.display = "";
              } else {
                  x[i].style.display = "none";
              }
          }
      }
        
}
    