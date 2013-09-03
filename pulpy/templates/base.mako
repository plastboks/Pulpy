<html lang="en-US"
<head>
  <title>${request.registry.settings.get('pulpy.title')}</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <link rel="shortcut icon" href="${request.static_url('pulpy:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('pulpy:static/css/normalize.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="${request.static_url('pulpy:static/css/style.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body>
  <div id="wrapper">
    <div id="header">
       <h1>${request.registry.settings.get('pulpy.title')}</h1>
    </div>
    <div id="messages">
      <%include file="pulpy:templates/messages.mako"/>
    </div>
    <div class="sidebar corners5px">
      <%include file="pulpy:templates/sidebar.mako"/>
    </div>
    <div id="content" class="corners5px">
       ${next.body()} 
    </div>
    <div id='footer'>
      <p>${request.registry.settings.get('pulpy.footer')}</p>
    </div>
  </div>
</body>
</html>