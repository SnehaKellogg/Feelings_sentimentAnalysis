$(document).ready(function () {
  $("#sideplaceholder").load("/sidebar");
  });
 
      
$(document).ready(function () {
  $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

});

