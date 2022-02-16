import matplotlib.pyplot  as plt
import seaborn as sns
import joblib
import typing
feature_importance = pd.DataFrame()
feature_importance['feature'] = feature_names

model_files: List[str] = sorted(glob(f'{model_path}-*.model'))
for fold, model_file in enumerate(model_files):
    feature_importance[f'fold{fold}'] = joblib.load(model_file).feature_importances_

feature_importance['importance'] = feature_importance[[f'fold{fold}' for fold in range(len(model_files))]].mean(
    axis=1
)
feature_importance = feature_importance.sort_values(by='importance', ascending=False).reset_index(0, True)
feature_importance.to_csv(visualize_path / f'feature_importance.csv', index=False)

plt.figure(figsize=(32, 128))
sns.barplot(data=feature_importance, x='importance', y='feature')
plt.title(f'Feature Importance over {len(model_files)} folds')
plt.savefig(visualize_path / 'feature_importance.png')