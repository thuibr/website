# tomhuibregtse.com
This is my personal website. It is deployed to tomhuibregtse.com.

## TODOs

### Deployment
- [X] Deploy to fly.io
- [ ] Fly volume for SQLite Database
- [ ] Fly MinIO backup https://fly.io/docs/app-guides/minio/
- [X] Point tomhuibregtse.com to fly.io
- [ ] Setup automated deploys
  - [ ] Merging into `main` automatically deploys the website
  - [ ] Find a tool for this

### CI/Security
- [ ] Enable Dependabot updates
- [ ] Enable security scan
- [ ] Enable GitGuardian
- [ ] Integrate Sentry
- [ ] Disable the Admin page

### Django
- [ ] Top-level templates directory, or in proj/
- [ ] django-environ
  - [ ] Example of local development in ".env.local"
  - [ ] Example of production in ".env.prod"
  - [ ] .env files are in .gitignore
  - [ ] Contains SECRET_KEY
  - [ ] Contains DEBUG
- [ ] djlint
- [ ] django-sesame
- [ ] Pico CSS
- [ ] Homepage has link to blog and link to recipes

