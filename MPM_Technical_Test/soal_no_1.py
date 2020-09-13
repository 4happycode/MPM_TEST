# python_3

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dot","dog","lot","log"]
print(wordList)
print(beginWord, endWord)


from collections import defaultdict
class Solution(object):
	def __init__(self):
		self.length = 0
		self.all_combo_dict = defaultdict(list)

	def visitWordNode(self, queue, visited, others_visited):
		current_word, level = queue.popleft()
		for i in range(self.length):
			# Intermediate words for current word
			intermediate_word = current_word[:i] + "*" + current_word[i+1:]

			for word in self.all_combo_dict[intermediate_word]:
				if word in others_visited:
					# print(self.all_combo_dict)
					print(word)
					# print(queue)
					return level + others_visited[word]
					
				if word not in visited:
					visited[word] = level + 1
					queue.append((word, level + 1))
					
		# print(self.all_combo_dict)
		return None

	def ladderLength(self, beginWord, endWord, wordList):

		if endWord not in wordList or not endWord or not beginWord or not wordList:
			return 0

		self.length = len(beginWord)

		for word in wordList:
			for i in range(self.length):
				self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


		import collections
		queue_begin = collections.deque([(beginWord, 1)])
		queue_end = collections.deque([(endWord, 1)])

		
		visited_begin = {beginWord: 1}
		visited_end = {endWord: 1}
		ans = None

		while queue_begin and queue_end:

			ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
			if ans:
				print(self.visitWordNode)
				print(word)
				return ans

			ans = self.visitWordNode(queue_end, visited_end, visited_begin)
			if ans:
				print(self.visitWordNode)
				print(word)
				return ans

		print(word)
		print(self.all_combo_dict)
		return 0


s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))