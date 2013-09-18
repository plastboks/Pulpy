<%inherit file="pulpy:templates/base.mako"/>

<h1 class="title">${title}</h1>
<div class="upper_toolbar">
  <ul>
    <li><a href="${request.route_url('index')}">All</a></li>
    <li><a href="${request.route_url('note_new')}">New</a></li>
  </ul>
</div>

${next.body()}
