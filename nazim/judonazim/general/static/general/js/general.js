function is_elem_exists(selector)
{
  var count_items = $(selector).length;
  if(count_items <= 0)
  {
    return false;
  }
  return true;
}


function is_elem_displayed(selector)
{
    var elem = $(selector);
    var displayed_status = $(elem).css('display');
    if(displayed_status == 'none')
    {
      return false;
    }
    return true;
}

function fadeInImg(id_name)
{
  $('#' + id_name).css('opacity', '1');
}
