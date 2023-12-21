# IAuthenticationRequest - интерфейс
Запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAuthenticationRequest
VB __Копировать
     Public Interface IAuthenticationRequest
C++ __Копировать
     public interface class IAuthenticationRequest
F# __Копировать
     type IAuthenticationRequest = interface end
##  __Свойства
[Info](P_Tessa_Platform_Runtime_IAuthenticationRequest_Info.htm)|
Дополнительная информация для классов-расширений.  
---|---  
[Login](P_Tessa_Platform_Runtime_IAuthenticationRequest_Login.htm)|  Логин
(строковый идентификатор) сотрудника в том виде, в котором он указан в
карточке сотрудника (с точностью до регистра).  
[Password](P_Tessa_Platform_Runtime_IAuthenticationRequest_Password.htm)|
Пароль, введённый сотрудником. Проверка этого пароля запрашивается у сервиса
аутентификации.  
[SecurityOptions](P_Tessa_Platform_Runtime_IAuthenticationRequest_SecurityOptions.htm)|
Настройки безопасности, которые могут влиять на аутентификацию.  
[User](P_Tessa_Platform_Runtime_IAuthenticationRequest_User.htm)| Информация о
пользователе, полученная по логину из справочника сотрудников Tessa.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
