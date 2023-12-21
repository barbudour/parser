# IAuthenticationServiceProvider - интерфейс
Контейнер сервисов, предоставляющий доступ к сервисам в зависимости от типа
входа пользователя
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAuthenticationServiceProvider
VB __Копировать
     Public Interface IAuthenticationServiceProvider
C++ __Копировать
     public interface class IAuthenticationServiceProvider
F# __Копировать
     type IAuthenticationServiceProvider = interface end
##  __Методы
[TryGetService](M_Tessa_Platform_Runtime_IAuthenticationServiceProvider_TryGetService.htm)|
Возвращает сервис, выполняющий аутентификацию для заданного типа входа, или
null, если сервис недоступен.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
