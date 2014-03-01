<html lang="en-US"
<head>
  <title>${request.registry.settings.get('pulpy.title')}</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <link rel="shortcut icon" href="${request.static_url('pulpy:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('pulpy:static/css/normalize.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="${request.static_url('pulpy:static/css/style.css')}" type="text/css" media="screen" charset="utf-8" />
  <script data-main="${request.static_url('pulpy:static/js/main')}" src="${request.static_url('pulpy:static/js/require-2.1.8.min.js')}"></script>
</head>
<body>
    <section id="wrapper">
        <header>
            <h1>${request.registry.settings.get('pulpy.title')}</h1>
        </header>
        <section id="messages">
            <%include file="pulpy:templates/messages.mako"/>
        </section>
        <nav class="sidebar corners5px">
            <%include file="pulpy:templates/sidebar.mako"/>
        </nav>
        <section id="content" class="corners5px">
            ${next.body()} 
        </section>
        <footer>
            <p>${request.registry.settings.get('pulpy.footer')}</p>
        </footer>
    </section>
</body>
</html>
