def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            return i
