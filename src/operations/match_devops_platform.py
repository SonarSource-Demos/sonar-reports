from logs import log_event


def process_chunk(chunk):
    results = []
    for obj in chunk:
        res = execute(**obj['kwargs'])
        if res is not None:
            results.append([res])
        else:
            results.append([])
    return results


def execute(alm, repository, slug, label, repo_slug, integration_key, output_key, **_):
    results = None
    log_event(level='warning', status='success', process_type='match_platform', payload=dict(alm=alm, repository=repository, slug=slug, label=label, repo_slug=repo_slug, integration_key=integration_key), logger_name='default')
    if alm == 'bitbucketcloud' and repository == label:
        results = {output_key: integration_key}
    elif alm == 'github' and repository == repo_slug:
        results = {output_key: repository}
    elif alm == 'gitlab' and integration_key == str(repository):
        results = {output_key: integration_key}
    elif alm == 'azure' and label == f"{slug} / {repository}":
        results = {output_key: integration_key}
    return results
