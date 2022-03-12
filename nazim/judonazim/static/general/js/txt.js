function get_tagged_username(word)
{
   if(word.charAt(0) != '@')
   {
     return '';
   }
   return word.substring(1);
}

function reverseString(str)
{
    return str.split("").reverse().join("");
}
