<%inherit file="pulpy:templates/note/base.mako" />
<div class='body'>${body | n}</div>

<div class='byline lower_toolbar'>
  <p>
    Created by: ${note.user.email} @ ${note.created.date()}
    %if note.updated:
      | updated @ ${note.updated.date()}
    %endif
    | <a href="${request.route_url('note_edit', id=note.id)}">Edit</a>
  </p>
</div>

