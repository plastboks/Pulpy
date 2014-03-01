<%inherit file="pulpy:templates/base.mako"/>

<h2 class="title">${title}</h2>
<nav class="upper_toolbar">
    <ul>
        <li><a href="${request.route_url('index')}">All</a></li>
        <li><a href="${request.route_url('note_new')}">New</a></li>
    </ul>
</nav>

${next.body()}
