#Average duration
others_courses_min = 2.5
others_courses_max = 7
others_courses_average = 4
dalto_course = 1.5

#Unedited video length
unedited_video_average = 5
unedited_video_dalto = 3.5


#Differences in duration
difference_with_min =100 - round(dalto_course / others_courses_min * 100,2)
difference_with_max =100 - round(dalto_course / others_courses_max *100,2)
difference_with_average =100 - round(dalto_course / others_courses_average * 100,2)

#Calculating the percentage of video removed
percentage_video_removed =100 - round(others_courses_average / unedited_video_average * 100,2)
percentage_video_removed_dalto = 100 - round(dalto_course / unedited_video_dalto * 100,2)


#Showing duration differences
print('----------------------------')
print('Daltos course lasts: ')
print(f'-{difference_with_min} % less than the fastest one')
print(f'-{difference_with_max} % less than the slow one')
print(f'-{difference_with_average} % less than the average')
print('----------------------------')

#Showing the percentage of video removed
print(f'An average course removes {percentage_video_removed}% of video')
print(f'Daltos course removes {percentage_video_removed_dalto}% of video')
print('----------------------------')

#Showing differences if the courses lasted 10 hours
print(f'Watching 10 hours of a dalto course equals {round(others_courses_average /dalto_course * 10,2)} hours of other courses')
print(f'Viewing 10 hours of other courses equals {round(dalto_course /others_courses_average * 10,2)} hours of a dalto course')
print('----------------------------')
