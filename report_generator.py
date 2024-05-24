from transformers import HubModel

# Replace with your desired refresh interval (in seconds)
REFRESH_INTERVAL = 3600  # 1 hour

def get_top_downloads():
  hub = HubModel()
  models = hub.list_models()
  models.sort(key=lambda model: model["downloads"], reverse=True)
  return models[:10]

def generate_report():
  top_downloads = get_top_downloads()
  print(f"Top 10 Downloaded Models (Last Hour):")
  for model in top_downloads:
    print(f"\t- {model['id']}")

if __name__ == "__main__":
  generate_report()
  exit()
