def corp_flight_bookings(bookings: list[list[int]], n: int) -> list[int]:
    """
    Args:
        booking: matrix of seats taken between first and last booking
        n: numbers of booking
    Returns:
        answer: numbers of seats taken by each booking
        Time Complecity O(n^2)
        Space Complecity O(n)

    2nd. Method
    Time Complexity O(n)
    Space Complexity O(n)
    we can use running sum of taken seat from each booking.
        If you want to add element in the next index put that value in current index
        If you don't want to add element in the next index put negative value in next index
        example: logically------------------------------------------how we implement
             bookings = [[1,2,10],[2,3,20],[2,5,25]]                -----------------
            [10,10,0,0,0]                                           [10,0,-10, 0, 0]
            [0,20,20,0,0]                                           [0, 20, 0,-20,0]
            [0,25,25,25,25]                                         [0, 25, 0, 0, 0]
            + ----------------                                  index [1  2   3    4   5]
            ==[10,55,45,25,25] this is equivalent to -> running sum of [10,45,-10, -20, 0]

    """
    answer = [0] * n
    # total_booking = {}
    # for i in bookings:
    #     for j in range(i[0], i[1] + 1):
    #         if total_booking.get(j, 0):
    #             total_booking[j] += i[-1]
    #         else:
    #             total_booking[j] = i[-1]
    # for i in total_booking:
    #     answer.append(total_booking[i])
    # return answer

    for first_i, last_i, seat_i in bookings:
        answer[first_i - 1] += seat_i
        if last_i < n:
            answer[last_i] -= seat_i
    for i in range(1, len(answer)):
        answer[i] += answer[i - 1]

    return answer
bookings, n = [[1,2,10],[2,3,20],[2,5,25]] , 5
print(corp_flight_bookings(bookings, n))
