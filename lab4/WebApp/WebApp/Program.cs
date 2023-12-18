using SignalRApp;   // пространство имен класса ChatHub
 
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();      // подключаем сервисы SignalR

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapHub<ChatHub>("/chat");   // ChatHub будет обрабатывать запросы по пути /chat

app.Run();