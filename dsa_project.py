import heapq
import tkinter as tk
from tkinter import messagebox

def dijkstra(graph, start):
    # there is no known path from starting node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

def calculate_shortest_path():
    start_node = start_entry.get()
    if start_node not in graph:
        messagebox.showinfo("Info", "Select from the list.")
        return
    
    distances = dijkstra(graph, start_node)
    result_text.delete(1.0, tk.END)
    
    for node, distance in distances.items():
        result_text.insert(tk.END, f"{node}: {distance}\n")

def select_city(city):
    start_entry.delete(0,tk.END)
    start_entry.insert(tk.END,city)

# Example graph
graph = {
    'Karachi': {'Lahore': 15, 'Islamabad': 10, 'Peshawar':23},
    'Lahore': {'Karachi': 15, 'Islamabad': 6, 'Quetta': 3, 'Peshawar':18},
    'Islamabad': {'Karachi': 10, 'Lahore': 6, 'Quetta': 8, 'Peshawar':12},
    'Quetta': {'Lahore': 3, 'Islamabad': 8, 'Peshawar':24},
    'Peshawar': {'Karachi': 23, 'Islamabad': 12,'Lahore':18,'Quetta': 24}
}

# Create GUI window
window = tk.Tk()
window.title("Shortest Route")
window.geometry("500x400")
window.configure(background = '#EE82EE')

# Create input and output widgets
start_label = tk.Label(window, text="Your Location:",fg = "#FFA07A")
start_label.pack(pady=20)
start_entry = tk.Entry(window)
start_entry.pack(pady=20)

calculate_button = tk.Button(window, text="Calculate", command=calculate_shortest_path,fg = "#B22222")
calculate_button.pack(pady=20)

result_label = tk.Label(window, text="Shortest Distances in kilo meters:",fg = "#FFA07A")
result_label.pack(pady=20)
result_text = tk.Text(window, height=6, width=20)


result_text.pack(pady=20)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
cities_menu=tk.Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label='Cities',menu=cities_menu)
for city in graph.keys():
    cities_menu.add_command(label=city,command=lambda c=city:select_city(c))
    
# Start the GUI event loop
window.mainloop()
