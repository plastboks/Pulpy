<%inherit file="pulpy:templates/note/base.mako" />

<form action="${request.route_url(action, id=id)}" method="POST">
  ${form.csrf_token}
  %if action == 'note_edit':
    ${form.id()}
  %endif

  %for error in form.title.errors:
    <p class=error>${error}</p>
  %endfor
  <p>
    ${form.title.label}<br />
    ${form.title}
  </p>

  %for error in form.body.errors:
    <p class=error>${error}</p>
  %endfor
  <p>
    ${form.body.label}<br />
    ${form.body}
  </p>

  %if revisions:
    <div class='revisions'>
    <p>Older revisions</p>
    <ul>
      %for r in revisions:
        <li><a href="${request.route_url(action, id=id, _query={'revision': r.id})}">${r.created}</a></li>
      %endfor
    </ul>
    </div>
  %endif

  %if action is 'note_edit':
    <p class='byline'>
      Created by: ${note.user.email} @ ${note.created.date()}
      %if note.updated:
        | updated @ ${note.updated.date()}
      %endif
    </p>
  %endif

  <p>
    <input type="submit" value="Submit" />
  </p>
</form>