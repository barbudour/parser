# IServerSecurityProvider - интерфейс
Объект, предоставляющий доступ к настройкам безопасности сервера
[IServerSecurityOptions](T_Tessa_Platform_Runtime_IServerSecurityOptions.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServerSecurityProvider
VB __Копировать
     Public Interface IServerSecurityProvider
C++ __Копировать
     public interface class IServerSecurityProvider
F# __Копировать
     type IServerSecurityProvider = interface end
##  __Методы
[GetSecurityOptionsAsync](M_Tessa_Platform_Runtime_IServerSecurityProvider_GetSecurityOptionsAsync.htm)|
Возвращает настройки безопасности для экземпляра сервера с заданным именем.
Возвращает настройки по умолчанию, если сервер не найден (это может быть при
первичной установке системы). Не возвращает null.  
---|---  
[Invalidate](M_Tessa_Platform_Runtime_IServerSecurityProvider_Invalidate.htm)|
Сбрасывает настройки безопасности для указанного экземпляра сервера.  
[InvalidateAll](M_Tessa_Platform_Runtime_IServerSecurityProvider_InvalidateAll.htm)|
Сбрасывает настройки безопасности для всех экземпляров серверов.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
