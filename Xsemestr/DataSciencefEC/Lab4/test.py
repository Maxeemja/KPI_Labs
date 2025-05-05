import matplotlib.pyplot as plt
import numpy as np

# Дані для діаграми
labels = ['Промислові підприємства', 'Транспорт', 'Енергетика',
          'Сільське господарство', 'Побутова діяльність', 'Військова діяльність']
sizes = [33, 23, 18, 13, 8, 5]  # відсоткове співвідношення
colors = ['#FF5733', '#33A8FF', '#FFD933', '#33FF57', '#D933FF', '#FF3380']
explode = (0.05, 0, 0, 0, 0, 0)  # виділення сектора промислових підприємств

# Створення фігури та осей
plt.figure(figsize=(14, 10))

# Створення кругової діаграми
wedges, texts, autotexts = plt.pie(sizes,
                                   explode=explode,
                                   labels=None,  # Прибираємо підписи на самій діаграмі
                                   colors=colors,
                                   autopct='%1.1f%%',
                                   shadow=True,
                                   startangle=90,
                                   textprops={'fontsize': 14})

# Розміщення легенди справа, збільшена та з повними назвами
plt.legend(wedges, labels, title='Джерела екологічного ризику',
           loc='center right',
           bbox_to_anchor=(1.5, 0.5),  # Збільшуємо відступ легенди
           fontsize=14,
           title_fontsize=16)

# Встановлення рівних осей для кругової діаграми
plt.axis('equal')

# Додавання заголовку
plt.title('Розподіл джерел екологічного ризику', fontsize=18, pad=20)

# Стилізація відсотків на графіку
for autotext in autotexts:
    autotext.set_fontsize(13)
    autotext.set_weight('bold')
    autotext.set_color('white')

# Прибираємо анотації з діаграми
# Уже не додаємо блок з annotations

# Додаємо підзаголовок з поясненням
plt.figtext(0.5, 0.01,
           'Відносний внесок різних джерел у загальний екологічний ризик (у відсотках)',
           ha='center',
           fontsize=12)

# Налаштування полів, щоб вся легенда помістилася
plt.tight_layout()

# Збереження діаграми
plt.savefig('ekoryzyk_dzherela_updated.png', dpi=300, bbox_inches='tight')

# Відображення діаграми
plt.show()