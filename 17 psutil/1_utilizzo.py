import psutil

# 1. Informazioni sulla CPU
print("=== Informazioni CPU ===")
# Percentuale di utilizzo della CPU (su tutti i core)
cpu_percent = psutil.cpu_percent(interval=1)
print(f"Percentuale di utilizzo CPU: {cpu_percent}%")

# Percentuale di utilizzo per ogni core
cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
print(f"Percentuale di utilizzo per ogni core: {cpu_percent_per_core}")

# Frequenza della CPU
cpu_freq = psutil.cpu_freq()
print(f"Frequenza CPU: {cpu_freq.current:.2f} MHz (Min: {cpu_freq.min:.2f} MHz, Max: {cpu_freq.max:.2f} MHz)")

# 2. Informazioni sulla Memoria
print("\n=== Informazioni Memoria ===")
# Memoria fisica (RAM)
memory = psutil.virtual_memory()
print(memory.total)
print(f"Memoria Totale: {memory.total / (1024 ** 3):.2f} GB")
print(f"Memoria Utilizzata: {memory.used / (1024 ** 3):.2f} GB ({memory.percent}%)")
print(f"Memoria Disponibile: {memory.available / (1024 ** 3):.2f} GB")

# Memoria di swap
swap = psutil.swap_memory()
print(f"Swap Totale: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap Utilizzato: {swap.used / (1024 ** 3):.2f} GB ({swap.percent}%)")

# 3. Informazioni sui Dischi
print("\n=== Informazioni Disco ===")
# Utilizzo del disco per partizione
disk_partitions = psutil.disk_partitions()
for partition in disk_partitions:
    print(f"Partizione: {partition.device}")
    disk_usage = psutil.disk_usage(partition.mountpoint)
    print(f"  Totale: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"  Usato: {disk_usage.used / (1024 ** 3):.2f} GB ({disk_usage.percent}%)")
    print(f"  Libero: {disk_usage.free / (1024 ** 3):.2f} GB")
    print()

# 4. Informazioni sulla Rete
print("\n=== Informazioni Rete ===")
# Statistiche della rete
net_io = psutil.net_io_counters()
print(f"Bytes inviati: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
print(f"Bytes ricevuti: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

# 5. Informazioni sui Processi
print("\n=== Informazioni Processi ===")
# Elenco dei processi attivi
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        print(f"Processo PID: {proc.info['pid']}, Nome: {proc.info['name']}, "
              f"CPU: {proc.info['cpu_percent']}%, Memoria: {proc.info['memory_percent']:.2f}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# 6. Sensori di Temperatura (se supportati)
try:
    print("\n=== Sensori di Temperatura ===")
    temps = psutil.sensors_temperatures()
    if not temps:
        print("Sensori di temperatura non disponibili.")
    else:
        for name, entries in temps.items():
            for entry in entries:
                print(f"{name} - {entry.label or 'N/A'}: {entry.current}°C (Min: {entry.min}°C, Max: {entry.max}°C)")
except AttributeError:
    print("Funzionalità di sensori di temperatura non supportata su questa piattaforma.")
