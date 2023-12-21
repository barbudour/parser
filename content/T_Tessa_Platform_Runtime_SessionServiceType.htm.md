# SessionServiceType - перечисление
Тип сессии, который определяется типом веб-приложения: для desktop- или для
web-клиентов, или веб-сервис неизвестен.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SessionServiceType
VB __Копировать
     Public Enumeration SessionServiceType
C++ __Копировать
     public enum class SessionServiceType
F# __Копировать
     type SessionServiceType
##  __Члены
Unknown| 0|  Тип сервиса неизвестен. Обычно это означает, что сессия открыта
при прямом взаимодействии с базой данных. Это могут быть плагины Chronos,
интеграционные веб-сервисы с собственной авторизацией и другие веб-приложения.  
---|---|---  
DesktopClient| 1|  Сессия открыта для Windows-клиента. Это могут быть
приложения TessaAdmin, TessaClient, консольный tadmin, интеграционный веб-
сервис и др.  
WebClient| 2|  Сессия открыта для Web-клиента. Это или Web-клиент Tessa, или
интеграция через Web API.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
