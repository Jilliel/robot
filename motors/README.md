# Module principal

## Structure

- Ce module comporte 4 sous-modules:
    - controller: sous-module développé [ici](https://gitlab.telecom-paris.fr/software/dc-motor-driver-hat)
    - corrector: Ce module met à disposition 
        - une classe PID permettant de réaliser des asservissements.
        - une classe Position permettant d'estimer la position grâce aux informations des encodeurs.
    - motors: Ce sous-module utilie les sous-modules précédents afin de permettre le contrôle des moteurs.

## Modules externes

Les modules réutilisés sont:
- Numpy
- Controller (voir README du dépôt)