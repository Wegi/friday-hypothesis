from hypothesis import given, strategies as st

@given(st.lists(st.integers()), st.lists(st.integers()))
def test_sorting_two_lists(xs, ys):
	assert sorted(xs + ys) == sorted(xs) + sorted(ys)