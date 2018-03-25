// '.tbl-content' consumed little space for vertical scrollbar, scrollbar width depend on browser/os/platfrom. Here calculate the scollbar width .
$(window).on("load resize ", function() {
  var scrollWidth = $('.table100-head').width() - $('.table100-head table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
}).resize();
