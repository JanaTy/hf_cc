import os
from json import loads
from migrate.versioning.schema import ControlledSchema
from migrate.versioning.script import PythonScript, SqlScript
from migrate.versioning.util import with_engine
from migrate.exceptions import DatabaseNotControlledError
from coding_challenge import container


@with_engine
def get_migration_files(host, repo, **kw):
    engine = kw['engine']
    try:
        schema = ControlledSchema(engine, repo)
    except DatabaseNotControlledError:
        ControlledSchema.create(engine, repo)
        schema = ControlledSchema(engine, repo)
    changeset = schema.changeset()
    scripts = []
    for ver_num, script in changeset.items():
        needs = None
        if isinstance(script, PythonScript):
            needs = (script.module.needs
                     if hasattr(script.module, 'needs')
                     else None)
        elif isinstance(script, SqlScript):
            with open(script.path) as f:
                first_line = f.readline()
                if first_line.startswith('-- needs: '):
                    needs = tuple(
                        map(tuple,
                            loads(first_line
                                  .strip('\n')
                                  .replace('-- needs: ', ''))))
        scripts.append((repo, ver_num, script, needs))
    scripts.sort()
    return scripts


def order_that(changing, metier, src, until=None):
    if not src[metier]:
        return
    ver_num = src[metier][0][1]
    if until and ver_num >= until:
        return
    while src[metier] and (not until or ver_num < (until + 1)):
        repo, ver_num, script, needs = src[metier][0]
        if not needs:
            item = src[metier].pop(0)
            changing.append(item)
        else:
            for need in needs:
                new_metier, new_ver_num = need
                order_that(changing, new_metier, src, until=new_ver_num)
                changing.append(src[metier].pop(0))


def bulk(action):
    metiers = {}
    changing = []

    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'modules',
        'migrations'
    )

    host = container.config['URL_DB']
    metiers['modules'] = get_migration_files(host, path)
    for metier in metiers.keys():
        order_that(changing, metier, metiers)
    run_batch(host, changing)


@with_engine
def run_batch(host, scripts, **kw):
    engine = kw['engine']
    previous = ""
    schema = None
    for repo, ver, script, _ in scripts:
        if repo != previous:
            schema = ControlledSchema(engine, repo)
            previous = repo
        schema.runchange(ver, script, step=1)
