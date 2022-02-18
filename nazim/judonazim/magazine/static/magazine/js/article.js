

$('#btn-follow').click(function(){

  var caller_type = 'post';
  // id of post
  var id = $('#post_pk').val();

  //now unfollow option is visible and fllow is hidden
  $(this).siblings('#btn-unfollow').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(caller_type, id, flag = 'follow');
});


$('#btn-unfollow').click(function(){

  var caller_type = 'post';
  // id of post
  var id = $('#post_pk').val();

  //now follow option is visible and unfllow is hidden
  $(this).siblings('#btn-follow').show();
  $(this).hide();

  //function inside article.html page, call ajax
  f_follow(caller_type, id, flag = 'unfollow');
});
