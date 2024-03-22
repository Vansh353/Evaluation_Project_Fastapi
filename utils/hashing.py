from passlib.context import CryptContext

# Initialize Passlib's CryptContext with bcrypt scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes the provided password using bcrypt.
    """
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies the provided plain password against the hashed password using bcrypt.
    """
    return pwd_context.verify(plain_password, hashed_password)
