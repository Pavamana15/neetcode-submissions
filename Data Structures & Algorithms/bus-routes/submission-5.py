class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        from collections import defaultdict, deque
        
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        
        queue = deque([(source, 0)])   # (current_stop, buses_taken)
        visited_stops = set([source])
        visited_buses = set()
        
        while queue:
            stop, buses = queue.popleft()
            
            for bus in stop_to_routes[stop]:
                if bus in visited_buses:
                    continue
                
                visited_buses.add(bus)
                
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1
                    
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        
        return -1