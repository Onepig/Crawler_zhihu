from zhihu import *

##start_question_url="http://www.zhihu.com/question/23831121"

##question=Question(start_question_url)
##
##title=question.get_title()
##print title
##
##detail=question.get_detail()
##print detail
##
##answer_num=question.get_answers_num()
##print answer_num
##
##followers=question.get_followers_num()
##print followers
##
##topics=question.get_topics()
##print topics
##
##answers=question.get_all_answers()
##for answer in answers:
##    print answer.to_txt()

'''
topic_url="http://www.zhihu.com/topic/19550547"


topic=Topic(topic_url)

print topic.get_name()

print "\nFather topics:"
fathertopics=topic.get_fatherTopic()
for fathertopic in fathertopics:
    print fathertopic.get_name()

print "\nChildren topics:"
childrentopics=topic.get_childrenTopic()

for child_topic in childrentopics:
    print child_topic.get_name()

#questions=topic.get_all_questions()

#for question in questions:
#   print question.get_title()
'''
'''
print topic.get_followers_num()

followers=topic.get_all_topic_followers()
for follower in followers:
    print follower.get_user_id()
'''
user_url="http://www.zhihu.com/people/bo-cai-28-7"
user=User(user_url)
for follower in user.get_followers():
	print follower.get_user_id()


