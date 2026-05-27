class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        def remove_once(main_list, sub_list):
            for element in sub_list:
                if element in main_list:
                    main_list.remove(element)  # Remove only the first occurrence
            return main_list

        num_of_groups = len(hand) // groupSize

        for _ in range(num_of_groups):
            grouplist = []
            minimum = min(hand)
            for i in range(groupSize):
                if minimum + i in hand:
                    grouplist.append(minimum + i)

                else:
                    return False
            print("The group is :", grouplist)
            hand = remove_once(hand, grouplist)
            print("The remaining number in hand:", hand)
        return True
                