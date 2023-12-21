# IAuthenticationResponse - интерфейс
Ответ на запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAuthenticationResponse
VB __Копировать
     Public Interface IAuthenticationResponse
C++ __Копировать
     public interface class IAuthenticationResponse
F# __Копировать
     type IAuthenticationResponse = interface end
##  __Свойства
[ErrorMessage](P_Tessa_Platform_Runtime_IAuthenticationResponse_ErrorMessage.htm)|
Текстовое описание возникшей ошибки или null, если ошибка не возникла или с
ошибкой не связано текстовое описание (оно будет предоставлено автоматически).
Точка в конце сообщения ставится автоматически.  
---|---  
[Exception](P_Tessa_Platform_Runtime_IAuthenticationResponse_Exception.htm)|
Возникшее исключение или null, если ошибка не возникла или ошибка не связана с
исключением.  
[ExceptionCode](P_Tessa_Platform_Runtime_IAuthenticationResponse_ExceptionCode.htm)|
Код ошибки для исключения [SessionException] или
[SessionExceptionCode.Unknown], если ошибка не возникла или код ошибки не
предоставляется.  
[Info](P_Tessa_Platform_Runtime_IAuthenticationResponse_Info.htm)|
Дополнительная информация для классов-расширений.  
[Success](P_Tessa_Platform_Runtime_IAuthenticationResponse_Success.htm)|
Признак того, что аутентификация прошла успешно.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
