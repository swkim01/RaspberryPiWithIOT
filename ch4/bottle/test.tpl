<h2>
% name = person
{{name}}'s Friends
</h2>
<ul>
  % for name in friends:
    <li>{{name}}</li>
  % end
</ul>
