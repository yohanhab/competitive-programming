def dominoPiling(m,n):
        answer = 0

        if m %2 == 0:
            answer += (n)*(m/2)
        else:
            if n %2 == 0:
                answer += (n)*((m -1) /2) + (n/2)
            else:
                answer += (n)*((m -1) /2) + ((n -1)/2)
        return int(answer)
