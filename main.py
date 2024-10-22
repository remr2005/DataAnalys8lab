from dsmltf import build_tree_id3, classify

def main():
    # Задание про собеседование
    # dataset
    inputs_1 = [
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Mid', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Go', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Mid', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Go', 'tweets': 'yes', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Junior', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'JavaScript', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'JavaScript', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'JavaScript', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Ruby', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Ruby', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'Ruby', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Go', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Go', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Senior', 'lang': 'PHP', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Mid', 'lang': 'PHP', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Junior', 'lang': 'PHP', 'tweets': 'yes', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Junior', 'lang': 'Java', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'C++', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'C++', 'tweets': 'yes', 'phd': 'no'}, True),
    ]
    # наш алгоритм
    tree = build_tree_id3(inputs_1)
    print(classify(tree,{'level':'Senior', 'lang':'Java', 'tweets':'no',
        'phd':'no'}))
    students_data = [
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090301", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090304", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "100503", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, True),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090301", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, False),
        ({"program": "090304", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "100503", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "no", "teacher_feedback": "good"}, True),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True)
    ]
    tree_2 = build_tree_id3(students_data)
    print(classify(tree_2,{"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "good"}))
    # И это все? Серьезно?
if __name__ == "__main__":
    main()
