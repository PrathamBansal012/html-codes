prob_st=0.2
prob_st_pos=0.2*0.85
prob_nst_pos=0.8*0.02
prob_positive=prob_st_pos+prob_nst_pos
probs_pos_given_st=0.85
prob_result=(prob_st*probs_pos_given_st)/prob_positive
print("probability",
round((prob_result),3))