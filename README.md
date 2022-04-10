# servarr role

[![CI](https://github.com/coaxial/servarr/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/servarr/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/servarr

## Purpose

Installs Sonarr, Radarr, NZBGet, Transmission and optionally configures NGINX
to serve their UIs at http://<your-server>/<app-name>.

Individual roles for each app available at https://galaxy.ansible.com/coaxial/<app-name>

## Variables and their defaults

| variable name       | default value | description                                             |
| ------------------- | ------------- | ------------------------------------------------------- |
| `servarr_use_nginx` | `yes`         | Whether to install and configure nginx for all services |

## Know issues

Because of an [issue](https://github.com/nginxinc/ansible-role-nginx/issues/507) in the nginxinc.nginx role, it will run the nginx tasks for each application.

Since the tasks are idempotent, it won't do any damage other than wasting time.

Once the issue is resolved, the nginx role should run only once.
