# Merge e gestione dei conflitti

## Unire un branch nel branch corrente
Unisce le modifiche di un altro branch in quello attuale.
```bash
git merge <nome-branch>
```

## Visualizzare i conflitti dopo un merge
Mostra i file che richiedono una risoluzione dei conflitti.
```bash
git status
```

## Aggiungere i file risolti
Aggiunge i file risolti alla staging area dopo un conflitto.
```bash
git add <file-risolto>
```

## Completare il merge
Finalizza il merge con un commit.
```bash
git commit -m "<messaggio>"
```
