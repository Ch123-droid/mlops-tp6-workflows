from flow_mlops import reentrainement

if __name__ == '__main__':
    # Crée le déploiement "hebdomadaire" puis attend les exécutions à lancer.
    # Laisser ce terminal ouvert ; Ctrl + C pour arrêter.
    reentrainement.serve(
        name='hebdomadaire',
        cron='0 6 * * 1'
    )
