<%inherit file="pulpy:templates/account/base.mako" />

<form action="${request.route_url(action)}" method="POST">
  ${form.csrf_token}

  %for error in form.email.errors:
    <p class=error>${error}</p>
  %endfor
  <p>
    ${form.email.label}<br />
    ${form.email}
  </p>

  %for error in form.datetime_format.errors:
    <p class=error>${error}</p>
  %endfor
  <p>
    ${form.datetime_format.label}<br />
    ${form.datetime_format}
  </p>

  %for error in form.password.errors:
    <p class=error>${error}</p>
  %endfor
  <p>
    ${form.password.label}<br />
    ${form.password}
  </p>

  <p>
    ${form.confirm.label}<br />
    ${form.confirm}
  </p>

  <p class='byline'>
    Created @: ${user.created.date()}
    %if user.updated:
      | updated @ ${user.updated.date()}
    %endif
  </p>

  <p>
    <input type="submit" value="Submit" />
  </p>
</form>
