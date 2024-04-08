# tomhuibregtse.com
This is my personal website. It is deployed to tomhuibregtse.com.

## TODOs

### Deployment
- [X] Deploy to fly.io
- [X] Fly volume for SQLite Database
- [ ] Fly MinIO backup https://fly.io/docs/app-guides/minio/
- [X] Point tomhuibregtse.com to fly.io
- [ ] Setup automated deploys
  - [ ] Merging into `main` automatically deploys the website
  - [ ] Find a tool for this

### CI/Security
- [X] Enable Dependabot updates
- [X] Enable security scan
- [ ] Enable GitGuardian
- [X] Integrate Sentry
- [ ] Precommit hook

### Django
- [X] Top-level templates directory, or in proj/
- [X] django-environ
  - [X] .env files are in .gitignore
  - [X] Contains SECRET_KEY
  - [X] Contains DEBUG
- [X] djlint
- [X] black
- [X] django-sesame
- [ ] Pico CSS
- [ ] HTMX
- [ ] Homepage has link to blog and link to recipes
- [X] "You are logged in as" on all pages
- [X] STATIC_ROOT
