function setCommentText(id, type)
{
	element = document.getElementById(id);

	if (type == 'bold')
	{
		start = '[b]';
		end = '[/b]';
	}

	else if (type == 'italic')
	{
		start = '[i]';
		end = '[/i]';
	}

	else if (type == 'underline')
	{
		start = '[u]';
		end = '[/u]';
	}

	if (document.selection)
	{
		element.focus();
		sel = document.selection.createRange();
		sel.text = start + sel.text + end;
	}

	else if (element.selectionStart || element.selectionStart == '0')
	{
		element.focus();
		var startPos = element.selectionStart;
		var endPos = element.selectionEnd;
		element.value = element.value.substring(0, startPos) + start + element.value.substring(startPos, endPos) + end + element.value.substring(endPos, element.value.length);
	}

	else
	{
		element.value += start + end;
	}
}