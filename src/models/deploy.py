import joblib
from pathlib import Path
from datetime import datetime

class ModelDeployer:
    def __init__(self, artifacts_dir: str = "models"):
        self.artifacts_dir = Path(artifacts_dir)
        self.production_dir = self.artifacts_dir / "production"
        self.production_dir.mkdir(parents=True, exist_ok=True)
    
    def save_model_artifacts(self, model, preprocessor, feature_engineer, metadata: dict):
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        version = f"v_{timestamp}"
        
        artifacts = {
            'model': model,
            'preprocessor': preprocessor,
            'feature_engineer': feature_engineer,
            'version': version,
            'metadata': metadata
        }
        
        artifact_path = self.production_dir / "model_latest.pkl"
        joblib.dump(artifacts, artifact_path)
        
        return artifact_path
