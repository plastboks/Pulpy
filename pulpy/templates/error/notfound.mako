<html lang="en-US"
<head>
    <title>Pulpy</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
    <link rel="shortcut icon" href="${request.static_url('pulpy:static/favicon.ico')}" />
    <link rel="stylesheet" href="${request.static_url('pulpy:static/css/normalize.css')}" type="text/css" media="screen" charset="utf-8" />
    <link rel="stylesheet" href="${request.static_url('pulpy:static/css/notfound.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body>
<body>
    <section id="notfound">
        <h1>${title}</h1>
        <p>${message}</p>
        <p class="home"><span><a href="${request.route_url('index')}">Home</a></span><p>
    </section>
</body>
