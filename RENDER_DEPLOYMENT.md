# Deploying Yale Trading Platform on Render

This guide explains how to deploy the Yale Trading Platform on Render.com, including both the web application and PostgreSQL database.

## Prerequisites

1. A [Render account](https://render.com)
2. Your code committed to a GitHub repository

## Deployment Steps

### Option 1: Blueprint Deployment (Recommended)

The easiest way to deploy is using Render's Blueprint feature:

1. Log in to your Render dashboard
2. Click on the "New" button and select "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file and create both:
   - A PostgreSQL database
   - A web service running your Flask application

### Option 2: Manual Deployment

If you prefer to set up services individually:

#### PostgreSQL Database

1. In your Render dashboard, click "New" and select "PostgreSQL"
2. Configure your database:
   - Name: `ytsp-db` (or your preferred name)
   - Database: `ytsp`
   - User: `ytsp_server`
   - Select the region closest to your users
   - Choose a plan (Free tier is available)
3. Click "Create Database"
4. Save the connection details provided

#### Web Service

1. In your Render dashboard, click "New" and select "Web Service"
2. Connect your GitHub repository
3. Configure your web service:
   - Name: `yale-trading-platform` (or your preferred name)
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
4. Add environment variables:
   - `SECRET_KEY`: (generate a secure random string)
   - `DATABASE_URL`: (use the connection string from your Render PostgreSQL database)
   - `FLASK_APP`: `run.py`
5. Click "Create Web Service"

## Database Migrations

After deployment, you may need to run database migrations:

1. Go to your web service in the Render dashboard
2. Click on "Shell"
3. Run: `flask db upgrade`

## Troubleshooting

- **Connection Issues**: Ensure your `DATABASE_URL` is correctly formatted. Render uses `postgres://` in connection strings, but SQLAlchemy requires `postgresql://`.
- **Application Errors**: Check logs in your Render dashboard for detailed error information.
- **Database Migrations**: If your application fails to start due to missing tables, run migrations manually.

## Local Development

For local development with the Render PostgreSQL database:

1. Add your Render database connection string to your local `.env` file
2. Make sure to replace `postgres://` with `postgresql://` if using SQLAlchemy

## Resources

- [Render Python Deployment Docs](https://render.com/docs/deploy-flask)
- [Render PostgreSQL Docs](https://render.com/docs/databases) 