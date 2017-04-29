from hypothesis import given, strategies as st, settings
from splitsy import split_at_string as splity

@given(st.text(), st.text())
@settings(max_examples=1000)
def test_second_split(body, query):
	result = splity(body, query)
	if body == query:
		assert result == []
	assert isinstance(result, list)
	assert len(result) <= 2
	if len(result) == 2:
		assert len(result[0] + result[1]) <= len(body)
		assert result[0] + query + result[1] == body
	if result == []:
		assert body == query 