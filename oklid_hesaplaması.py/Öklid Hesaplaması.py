import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaları tanımlama
points = [(1, 2), (4, 6), (7, 8), (3, 5)]

# Mesafeleri saklamak için liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çifti iki kez hesaplamamak için i + 1'den başlıyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)
