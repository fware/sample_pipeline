# A Naive recursive Python implementation of LCS problem

class word_match:
	def __init__(self, word1, word2, len1, len2):
		self.word1 = word1
		self.word2 = word2
		self.len1 = len1
		self.len2 = len2
		self.char_equal_count = 0
		self.count_change = 0
		self.match_word = ""

	def build_word(self, value):
		if value not in self.match_word:
			self.count_change += 1
			self.match_word = self.match_word + value
			if self.match_word in self.word2:
				return True
			else:
				return False
			return False


	def lcs(self, X, Y, m, n):
		if m == 0 or n == 0:
			return 0
		elif X[m-1] == Y[n-1]:
			self.char_equal_count += 1
			if self.build_word(X[m-1]):
				return 0
			return 1 + self.lcs(X, Y, m-1, n-1)
		else:
			return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m-1, n))


# Driver code
if __name__ == '__main__':
	m_match = ""
	S1 = "horse"
	S2 = "ros"
	print(f"Compare:") 
	print(f"\t {S1}")
	print(f"\t {S2}\n")
	m = word_match(S1, S2, len(S1), len(S2))
	print("Length of LCS is", m.lcs(S1, S2, len(S1), len(S2)))
	print(f"Match the word \"{m.match_word}\" in {m.count_change} steps.")
	print(f"Character equal check count: {m.char_equal_count}")
