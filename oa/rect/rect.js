document.addEventListener('DOMContentLoaded', fn, false);

function fn(){
  var items = document.getElementsByTagName("div");
  for( item in items){
    console.log(item);
  }

  document.getElementById("div3").addEventListener(
    "click",
    function (event){
      event.stopPropagation();
      alert(this.id);
    }
  );
  document.getElementById("div2").addEventListener(
    "click",
    function (event){
      event.stopPropagation();
      alert(this.id);
    }
  );
  document.getElementById("div1").addEventListener(
    "click",
    function (event){
      event.stopPropagation();
      alert(this.id);
    }
  );
}
