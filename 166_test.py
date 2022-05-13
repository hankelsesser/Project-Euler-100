def compute(n):
	ans = 0
	digits = tuple(range(n))
	for b in digits:
		for c in digits:
			for d in digits:
				for e in digits:
					for i in digits:
						m = b + c + d - e - i
						if m < 0 or m > (n-1): continue
						for k in digits:
							f = b + c + d*2 - e - i - k
							if f < 0 or f > (n-1): continue
							for a in digits:
								for g in digits:
									o = a + b + d - g - k
									if o < 0 or o > (n-1): continue
									j = a + b + c - g - m
									if j < 0 or j > (n-1): continue
									l = a + b + c + d - i - j - k
									if l < 0 or l > (n-1): continue
									h = a + b + c + d - e - f - g
									if h < 0 or h > (n-1): continue
									n = a + c + d - f - j
									if n < 0 or n > (n-1): continue
									p = a + b + c - h - l
									if p < 0 or p > (n-1): continue
									ans += 1
	return str(ans)


if __name__ == "__main__":
	print(compute(10))