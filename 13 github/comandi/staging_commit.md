# Staging e commit

## Aggiungere file alla staging area
Aggiunge un file specifico alla staging area.
```bash
git add <nome-file>
```

## Aggiungere tutti i file
Aggiunge alla staging area tutti i file modificati.
```bash
git add .
```

## Verificare lo stato dei file
Mostra lo stato attuale della working directory e della staging area.
```bash
git status
```

## Rinominare un file
Rinomina un file tracciato da Git.
```bash
git mv <nome-vecchio> <nome-nuovo>
```

## Rimuovere un file dal repository
Elimina un file sia dal repository che dal filesystem.
```bash
git rm <nome-file>
```

## Creare un commit
Registra le modifiche nella cronologia del repository.
```bash
git commit -m "Messaggio del commit"
```

## Visualizzare la cronologia dei commit
Mostra i commit precedenti del repository.
```bash
git log
```

## Visualizzare la cronologia in forma compatta
Mostra i commit con una visualizzazione condensata.
```bash
git log --oneline
```
