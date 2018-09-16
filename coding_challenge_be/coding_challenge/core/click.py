import click


class CodingChallengeCli:

    def start(self):
        pass

    def end(self):
        pass


@click.group(help='groupe de commande relative au coding challenge')
def cli():
    cc_cli = CodingChallengeCli()
    cc_cli.start()


@cli.command()
@click.option('--debug', is_flag=True, help='active le mode debug')
def server(debug=False, **_):
    """lance le serveur en mode debug/prod"""

    from coding_challenge import bootstrap
    from coding_challenge.coding_challenge_manager import ConfigManager

    bootstrap(ConfigManager())

    from coding_challenge.api.app import AppKernel
    AppKernel.start_server(debug=debug)


@cli.command()
@click.option('--do', default='upgrade', help="commande de migration")
@click.option('--env', default='prod',
              help="spécifie l'environement d'execution de la commande")
def migrate(do, env='prod'):
    """Commande pour lancer les migrations en BDD."""

    from coding_challenge import bootstrap
    from coding_challenge.coding_challenge_manager import (
        DebugConfig,
        ConfigManager
    )

    if env == 'prod':
        bootstrap(ConfigManager())
    if env == 'dev':
        bootstrap(DebugConfig())

    from coding_challenge.core import migration

    migration.bulk(do)


@cli.command()
@click.option('--coverage', is_flag=True, help="build tests coverage.")
def test(coverage=False):
    """Commande pour lancer facilement les tests avec des options d'exécution
    plus complètes, utiliser directement pytest."""

    import os

    directory = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.chdir(directory)
    print("working directory: %s" % directory)
    if coverage:
        os.system(
            ('pytest coding_challenge -v --cov=coding_challenge' 
             ' --cov-report html:cover --cov-branch'
             ' --cov-config ./.coveragerc').format(directory))
    else:
        os.system('pytest -v coding_challenge')
