from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )
    
    # App
    PROJECT_NAME: str = "Breakdown Assistance Technician/Admin Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://dbadmin:E5z%40cXsBF%4039%40%407x@public-primary-pg-inmumbaizone2-189553-1655477.db.onutho.com/db_dev_liftaway"
    
    # Redis
    # Updated to use Onutho hosted Redis with provided credentials
    # Username: dev_admin_utho
    # Password: gf8B7@@H3MjK59qk@@ (URL-encoded in the connection string)
    REDIS_URL: str = "redis://default:2%40uR%4082msHG%40q%40H8@public-primary-redis-inmumbaizone2-189555-1655760.db.onutho.com:6379/0"
    REDIS_LOCATION_EXPIRE: int = 300
    
    # JWT

    
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Google OAuth
    GOOGLE_CLIENT_ID: str = "400312749619-dvvsaicfuj91f0r03n8j6q2jd1d61g3c.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET: str = "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"
    
    # Apple OAuth
    APPLE_CLIENT_ID: str = ""
    APPLE_TEAM_ID: str = ""
    APPLE_KEY_ID: str = ""
    APPLE_PRIVATE_KEY: str = ""
    
    # Razorpay
    RAZORPAY_KEY_ID: str = ""
    RAZORPAY_KEY_SECRET: str = ""
    
    # Stripe
    
    STRIPE_PUBLISHABLE_KEY: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str


    
    # Platform fee percentage (e.g., 20% of driver earnings)
    PLATFORM_FEE_PERCENT: float = 20.0
    
    # Email SMTP
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "chaitanyakumarreddysomu9010@gmail.com"
    SMTP_PASSWORD: str = "cmbc fpuz vquo qlwe"
    SMTP_FROM_EMAIL: str = "chaitanyakumarreddysomu9010@gmail.com"
    SMTP_FROM_NAME: str = "Road Assistance"
    
    # UTHO S3 Storage
    UTHO_ACCESS_KEY: str = ""
    UTHO_SECRET_KEY: str = ""
    UTHO_BUCKET: str = ""
    UTHO_REGION: str = "ap-south-1"
    UTHO_ENDPOINT: str = ""
    UTHO_BUCKET_URL: str = ""
    
    # Mapbox
    MAPBOX_TOKEN: str = ""
    # WebSocket access keys (set in .env for production)
    DRIVER_WS_KEY: str = "driver-secret"
    CUSTOMER_WS_KEY: str = "customer-secret"
 
    TECHNICIAN_ACCEPT_TIMEOUT_SECONDS: int = 60
    MAX_TECHNICIANS_TO_NOTIFY: int = 5
    
    # UK Map bounds (for validation)
    UK_LAT_MIN: float = 49.9
    UK_LAT_MAX: float = 60.9
    UK_LNG_MIN: float = -8.2
    UK_LNG_MAX: float = 1.8

settings = Settings()


