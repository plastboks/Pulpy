/**
 * @filename: commons.js
 * 
 * @date: 2013-09-17
 *
 * @version: 0.0.1
 *
 * @description: common javascript. 
 *
 */

jQuery(function($){

  $(document).on('click', '.thisclose', function(){
      $(this).parent('p').remove();
  });

});
