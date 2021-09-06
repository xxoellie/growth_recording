def solution(n, lost, reserve) :
   reserve_list = list(set(reserve) - set(lost))
   lost_list = list(set(lost)-set(reserve))
   # 여벌 체육복을 가져온 사람과 도난 당한 사람의 중복을 제거해야 누가 체육복을 빌려줄 수 있는지 파악할 수 있으므로 reserve와 lost에서 겹치는 값들을 제거해서 list에 담아줍니다.

   answer = n - len(lost_list)
   # 구해야하는 값이 총 몇 명의 학생이 수업을 들을 수 있는지이므로 전체 학생수에서 체육복을 도난 당한 학생수의 명수를 제외하여 몇 명의 학생이 1차원적으로 수업을 들을 수 있는지 인원을 파악합니다.

   for i in lost_list :
      if i-1 in reserve_list :
          answer += 1
          reserve_list.remove(i-1)
      elif i+1 in reserve_list :
          answer += 1
          reserve_list.remove(i+1)
   # 체육복은 체격순으로 매겨져 있어 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
   # 그러므로 위에서 도난 당한 사람들의 중복을 제거한 값에서 그 수보다 앞/뒤 번호가 중복을 제거한 여벌 체육복을 가진 사람과 일치하면 수업을 들을 수 있는 사람에 더해주고 이미 체육복을 빌려주었으므로 중복을 제거한 여벌 체육복을 가진 사람에게서 제거해줍니다.

   return answer