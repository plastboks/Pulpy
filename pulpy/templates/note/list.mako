<%inherit file="pulpy:templates/note/base.mako"/>

%if paginator.items:
  <div class='tablelist'>
    <table id='notes'>
      <thead>
        <th>Title</th>
      </thead>
      <tbody>
        %for item in paginator.items:
          <tr>
            <td>${item.title}</td>
            <td class='actions'>
              <a href="${request.route_url('note_edit', id=item.id)}">
                <img src='${request.static_url("pulpy:static/icons/page_white_edit.png")}' title='Edit' alt='Edit' />
              </a>
            </td>
          </tr>
        %endfor
      </tbody>
    </table>
  </div>
  <div class='pager'>
    ${paginator.pager()}
  </div>
%else:
  <p>No notes found.</p>
%endif
