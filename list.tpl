<!DOCTYPE HTML> 
<html lang="ja"> 
<head>
<meta charset="UTF-8">
<title>書籍一覧</title>
</head>
<body> 
<h2>書籍一覧</h2>
<table border=“solid">
<thead> 
<td>タイトル</td>
<td>著者</td>
<td>出版社</td>
<td>購入日</td>
<td>状態</td>
<td>操作</td>
</thead>
<tbody>
%for d in data:
<tr>
<td>{{d["title"]}}</td> 
<td>{{d["author"]}}</td> 
<td>{{d["publisher"]}}</td> 
<td>{{d["acquisitionDate"]}}</td> 
<td>{{d["status"]}}</td>
<td>
<a href="/checkout"><input type="button" value="貸出" /></a>
<!--
<a href="/returned?id={{d["id"]}}"><input type="button" value="返却" /></a>
-->
<a href="/delete?id={{d["id"]}}"><input type="button" value="削除" /></a>
</td>

</tr>
%end
<p>返却期限は{{rd}}です</p>
</tbody>
</table>
<p><a href="/">新規登録</a></p>
</body>
</html>