# ControllerActivationMode - перечисление
Способ активации контроллера, т.е. его создание и освобождение.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ControllerActivationMode
VB __Копировать
     Public Enumeration ControllerActivationMode
C++ __Копировать
     public enum class ControllerActivationMode
F# __Копировать
     type ControllerActivationMode
##  __Члены
Unity| 0|  Выполняется Resolve из контейнера Unity для текущего экземпляра
сервера. Это значение по умолчанию. Для освобождение выполняется метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose), если он имеется у контроллера.  
---|---|---  
AspNetCore| 1|  Выполняется создание контроллера с зависимостями из DI-
контейнера ASP.NET Core способом, используемым по умолчанию в приложениях
ASP.NET Core. Для освобождения также используется способ по умолчанию, обычно
это выполняет метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose), если он имеется у контроллера (но это зависит от
реализации по умолчанию). Контроллер может быть не зарегистрирован в DI-
контейнере.  
ServiceBased| 2|  Выполняется Resolve для DI-контейнера ASP.NET Core,
аналогично поведению в активаторе
[ServiceBasedControllerActivator](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllers.servicebasedcontrolleractivator).
Для освобождение выполняется метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose), если он имеется у контроллера. Контроллеры должны быть
зарегистрированы в DI-контейнере ASP.NET Core. Используйте в отдельных веб-
приложениях, где регистрация контроллеров в DI-контейнере возможна.  
## __См. также
#### Ссылки
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
