%for m in request.session.pop_flash('success'):
    <p class="success corners5px">
        ${m}
        <a href="#" class="thisclose"></a>
    </p>
%endfor
%for m in request.session.pop_flash('status'):
    <p class="status corners5px">
        ${m}
        <a href="#" class="thisclose"></a>
    </p>
%endfor
%for m in request.session.pop_flash('error'):
    <p class="error corners5px">
        ${m}
        <a href="#" class="thisclose"></a>
    </p>
%endfor
