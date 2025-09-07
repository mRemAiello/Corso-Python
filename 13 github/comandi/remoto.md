# Remoto

## Aggiungere un repository remoto
Collega il repository locale a uno remoto.
```bash
git remote add origin <url-repository>
```

## Verificare i repository remoti
Elenca i repository remoti configurati.
```bash
git remote -v
```

## Scaricare gli aggiornamenti dal remoto
Recupera e integra le modifiche dal remoto.
```bash
git pull
```

## Caricare le modifiche sul remoto
Invia le modifiche al branch remoto.
```bash
git push origin <nome-branch>
```

## Impostare il branch di default per i push
Definisce il branch remoto di default per i push futuri.
```bash
git push --set-upstream origin <nome-branch>
```
