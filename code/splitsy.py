def split_at_string(body, query):
"""Split the input-string at the position of the query-string.
  Nearly the same as clojure.string/split. Not based on a regex, but instead
  based on a string to match strings containing literals, which could be
  special-characters in a regex.

  Examples:
  split_at_string("barfoo?baz", "foo?") => ["bar", "baz"]

  split_at_string("abc", "def") => ["abc"]

  split_at_string("0", "0") => []
"""
	