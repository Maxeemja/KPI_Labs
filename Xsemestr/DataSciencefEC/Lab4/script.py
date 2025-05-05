import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.graph_objects as go


class CurrencyRateForecast:
    def __init__(self, currency_pair='EURUSD=X', days_to_predict=7):
        self.currency_pair = currency_pair
        self.days_to_predict = days_to_predict

    def fetch_historical_data(self):
        """Отримання історичних даних курсу валют"""
        try:
            # Завантаження даних без мультиіндексу
            data = yf.download(self.currency_pair, period='2y')

            # Перетворення MultiIndex на звичайний DataFrame
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            return data
        except Exception as e:
            print(f"Помилка отримання даних: {e}")
            return None

    def prepare_features(self, data):
        """Підготовка ознак для прогнозування"""
        # Друк наявних стовпців для діагностики
        print("Наявні стовпці:", list(data.columns))

        # Створення копії для уникнення модифікації оригіналу
        df = data.copy()

        # Створення ознак
        df['Price_Shift_1'] = df['Close'].shift(1)
        df['Price_Shift_7'] = df['Close'].shift(7)
        df['Volume_Mean_7'] = df['Volume'].rolling(window=7).mean()
        df['Price_Change'] = df['Close'].pct_change()

        # Видалення рядків з NaN
        df.dropna(inplace=True)

        return df

    def train_model(self, data):
        """Навчання моделі прогнозування"""
        features = ['Price_Shift_1', 'Price_Shift_7', 'Volume_Mean_7', 'Price_Change']

        # Підготовка вхідних та цільових даних
        X = data[features]
        y = data['Close'].shift(-self.days_to_predict)

        # Видалення NaN
        clean_data = pd.concat([X, y], axis=1).dropna()
        X = clean_data[features]
        y = clean_data['Close']

        # Перевірка наявності достатньої кількості даних
        if len(X) < 10:
            raise ValueError("Недостатньо даних для навчання моделі")

        # Розділення на тренувальну та тестову вибірки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Масштабування ознак
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Навчання моделі
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)

        # Оцінка якості моделі
        y_pred = model.predict(X_test_scaled)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        print(f"Середня абсолютна похибка: {mae}")
        print(f"Середньоквадратична похибка: {mse}")

        return model, scaler, features

    def predict_future_rate(self, model, scaler, data, features):
        """Прогнозування курсу на наступний тиждень"""
        # Використання останніх доступних даних
        last_data = data.tail(1)

        # Перевірка наявності ознак
        X_predict = last_data[features].values
        X_predict_scaled = scaler.transform(X_predict)

        predicted_rate = model.predict(X_predict_scaled)[0]
        return predicted_rate

    def visualize_results(self, data, predicted_rate):
        """OLAP-візуалізація результатів"""
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Історичний курс'))

        # Додавання прогнозованої точки
        last_date = data.index[-1]
        predicted_date = last_date + pd.Timedelta(days=self.days_to_predict)
        fig.add_trace(go.Scatter(
            x=[last_date, predicted_date],
            y=[data['Close'].iloc[-1], predicted_rate],
            mode='markers+lines',
            name='Прогноз',
            line=dict(color='red', dash='dot')
        ))

        fig.update_layout(
            title=f'Прогноз курсу {self.currency_pair}',
            xaxis_title='Дата',
            yaxis_title='Курс'
        )

        fig.show()


def main():
    # Список валютних пар для аналізу
    currency_pairs = ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X']

    for pair in currency_pairs:
        print(f"\nАналіз валютної пари: {pair}")
        forecast = CurrencyRateForecast(currency_pair=pair, days_to_predict=7)

        try:
            # Отримання та підготовка даних
            historical_data = forecast.fetch_historical_data()

            if historical_data is not None:
                prepared_data = forecast.prepare_features(historical_data)

                # Навчання моделі
                model, scaler, feature_columns = forecast.train_model(prepared_data)

                # Прогнозування
                predicted_rate = forecast.predict_future_rate(model, scaler, prepared_data, feature_columns)
                print(f"Прогнозований курс на наступний тиждень: {predicted_rate}")

                # Візуалізація
                forecast.visualize_results(historical_data, predicted_rate)

        except Exception as e:
            print(f"Помилка для {pair}: {e}")


if __name__ == "__main__":
    main()