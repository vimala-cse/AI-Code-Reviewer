import reflex as rx

config = rx.Config(
    app_name="AI_Code_Reviewer",
    db_url="postgresql://neondb_owner:npg_GRVNi9rvK3Ha@ep-wispy-cell-anw9d6vd-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)