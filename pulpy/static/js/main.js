/**
 * @filename: main.js
 * 
 * @date: 2013-09-17
 *
 * @version: 0.0.1
 *
 * @description: main bootloader script
 *
 */

require.config({
  paths: {
      'ace': 'lib/ace'
  }
});

require(["jquery-2.0.3.min"], function(util) {});
require(["underscore-1.5.2.min"], function(util) {});

require(["commons"], function(util){});

require(["ace/ace"], function(ace) {
    var textfield = $('#body');
    if(textfield.length) {
      var data = textfield.val();
      textfield.hide();
      textfield.after('<div id="aceeditor"></div>')
    }
    var editor = ace.edit('aceeditor');

    editor.setTheme('ace/theme/github');
    //editor.getSession().setMode('ace/mode/javascript');
    editor.getSession().setValue(textfield.val());
    editor.getSession().setTabSize(4);
    editor.getSession().setUseSoftTabs(true);
    editor.getSession().on('change', function(){
        textfield.val(editor.getSession().getValue());
    });
});
