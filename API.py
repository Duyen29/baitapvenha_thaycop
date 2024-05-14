from fastapi import FastAPI
import httpx

# Tạo một ứng dụng FastAPI
app = FastAPI()

# Khóa API của OpenWeatherMap
OPENWEATHERMAP_API_KEY = "c1bb9a7622d4af5a0d0341c081ed9fe2"

# Định nghĩa một endpoint GET tại "/weather"
@app.get("/weather")
async def get_weather():
    city = "BACKAN"  # Thành phố cần lấy thông tin thời tiết
    # URL API để lấy dữ liệu thời tiết
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"

    # Sử dụng httpx để tạo một client bất đồng bộ
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)  # Gửi yêu cầu GET tới API
        if response.status_code == 200:
            weather_data = response.json()  # Lấy dữ liệu thời tiết dưới dạng JSON
            return weather_data  # Trả về dữ liệu thời tiết
        else:
            return {"error": "Failed to fetch weather data"}  # Trả về thông báo lỗi nếu yêu cầu thất bại

# Chạy ứng dụng FastAPI bằng uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


