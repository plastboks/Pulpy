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
