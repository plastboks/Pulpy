<%inherit file="pulpy:templates/base.mako"/>

<h1>${title}</h1>
<div class="upper_toolbar">
  <ul>
    <li><a href="${request.route_url('index')}">All</a></li>
  </ul>
</div>

${next.body()}