# Integration Test

This test validates the function after it's deployed and running, checking all layers of communication that comes first (Route53, EBL, API Gateway).

Run commands below in project root folder:

```bash
$ pipenv install --dev
$ pipenv shell
$ pytest -k integration
```
