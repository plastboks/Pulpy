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
        ${form.body.label}
        ${form.body}
        %if revision:
            <span class="notice">${"You are viewing an older revision than the current" if int(revision) != note.revisions[-1].id else ""}</span>
        %endif
    </p>

    %if revisions and revision:
        <section class='revisions'>
            <p>Revisions</p>
            <ul>
            %for r in revisions:
                <li class="${'current' if int(revision) == int(r.id) else 'archived'}" >
                    <a href="${request.route_url(action, id=id, _query={'revision': r.id})}">${r.created.strftime(request.session.get('dateformat'))}</a>
                </li>
            %endfor
            </ul>
        </section>
    %endif

    %if action is 'note_edit':
        <p class='byline'>
            Created by: ${note.user.email} @ ${note.created.strftime(request.session.get('dateformat'))}
            %if note.updated:
                | updated @ ${note.updated.strftime(request.session.get('dateformat'))}
            %endif
        </p>
    %endif

    <p>
        <input type="submit" value="Submit" />
    </p>
</form>
