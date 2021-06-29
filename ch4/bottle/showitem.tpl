<html>
<head>
</head>
<body>
<div class="container" style="padding-top:20px;">
<table class="table table-bordered">
<tr>
  <th>Id</th>
  <th>Name</th>
  <th>Birthday</th>
  <th>Gender</th>
</tr>
% for item in items:
    <tr>
    % for column in item:
      <td>{{column}}</td>
    % end
    </tr>
% end
</table>
</div>
</body>
</html>
