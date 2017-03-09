#!/usr/bin/env python3

import click
import requests

# ./01-github_issues-bot.py tokenn.py rules.py --repo https://api.github.com/repos/muffins90/python-kurz-knihovny --label other


@click.command()
@click.argument('token',  type=click.File('r'))
@click.option('--repo', prompt='Repo name', help='Repo name.')
@click.argument('rules', type=click.File('r'))
@click.option('--time', prompt='Time', help='Time issue.')
@click.option('--label', prompt='Default label', help='Default label.')
def hello(token, repo, rules, time, label):
    """Simple program that greets NAME for a total of COUNT times."""
    token = token.read();
    rulesLabel = {};
    for rule in rules:
        rule = rule.strip().split(';');
        rulesLabel.update({rule[0]: rule[1]});
    
    session = requests.Session();
    resp = session.headers = {'Authorization': 'token ' + token.strip(), 'User-agent': 'Python'};
    resp = session.get(repo + '/issues');
    print(resp);
    for issue in resp.json():
        for key, value in rulesLabel.items():
            if key in issue['title']:
                resp = session.post(repo + '/issues/' + str(issue['number']) + '/labels', value);
                print(resp.text);

if __name__ == '__main__':
    hello()

