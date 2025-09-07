# Comandi Git principali

### Configurare il nome utente
Imposta il nome che verrà associato ai tuoi commit.
```bash
git config --global user.name "Il Tuo Nome"
```

### Configurare l'email
Imposta l'email che verrà associata ai tuoi commit.
```bash
git config --global user.email "tuaemail@esempio.com"
```

### Clonare un repository esistente
Scarica una copia locale di un repository remoto.
```bash
git clone <url-repository>
```

### Inizializzare un nuovo repository
Crea un nuovo repository Git nella directory corrente.
```bash
git init
```

### Aggiungere file tracciati (staging area)
Aggiunge un file specifico alla staging area.
```bash
git add <nome-file>
```

### Oppure aggiungere tutti i file
Aggiunge alla staging area tutti i file modificati.
```bash
git add .
```

### Verificare lo stato dei file
Mostra lo stato attuale della working directory e della staging area.
```bash
git status
```

### Rimuovere un file dal repository
Elimina un file sia dal repository che dal filesystem.
```bash
git rm <nome-file>
```

### Rinominare un file
Rinomina un file tracciato da Git.
```bash
git mv <nome-vecchio> <nome-nuovo>
```

### Creare un commit
Registra le modifiche nella cronologia del repository.
```bash
git commit -m "Messaggio del commit"
```

### Visualizzare la cronologia dei commit
Mostra i commit precedenti del repository.
```bash
git log
```

### Mostrare i commit con una visualizzazione compatta
Visualizza la cronologia in forma condensata.
```bash
git log --oneline
```

### Creare un nuovo branch
Crea un nuovo branch senza spostarsi.
```bash
git branch <nome-branch>
```

### Cambiare branch
Passa a un branch esistente.
```bash
git checkout <nome-branch>
```

### Creare e passare a un nuovo branch
Crea un branch e vi si sposta immediatamente.
```bash
git checkout -b <nome-branch>
```

### Eliminare un branch
Rimuove un branch locale.
```bash
git branch -d <nome-branch>
```

### Aggiungere un repository remoto
Collega il repository locale a uno remoto.
```bash
git remote add origin <url-repository>
```

### Verificare i repository remoti
Elenca i repository remoti configurati.
```bash
git remote -v
```

### Scaricare gli aggiornamenti dal repository remoto
Recupera e integra le modifiche dal remoto.
```bash
git pull
```

### Caricare le modifiche sul repository remoto
Invia le modifiche al branch remoto.
```bash
git push origin <nome-branch>
```

### Impostare il branch di default per push
Definisce il branch remoto di default per i push futuri.
```bash
git push --set-upstream origin <nome-branch>
```

### Unire un branch nel branch corrente
Unisce le modifiche di un altro branch in quello attuale.
```bash
git merge <nome-branch>
```

### Visualizzare i conflitti dopo un merge
Mostra i file che richiedono una risoluzione dei conflitti.
```bash
git status
```

### Risolvere i conflitti e aggiungere i file risolti
Aggiunge i file risolti alla staging area dopo un conflitto.
```bash
git add <file-risolto>
```

### Completare il merge dopo la risoluzione dei conflitti
Finalizza il merge con un commit.
```bash
git commit
```
