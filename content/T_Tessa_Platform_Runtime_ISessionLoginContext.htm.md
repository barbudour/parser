# ISessionLoginContext - интерфейс
Контекст операции по входу в систему.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionLoginContext
VB __Копировать
     Public Interface ISessionLoginContext
C++ __Копировать
     public interface class ISessionLoginContext
F# __Копировать
     type ISessionLoginContext = interface end
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ISessionLoginContext_ApplicationID.htm)|
Идентификатор приложения, для которого выполняется вход, или null, если
идентификатор не указан.  
---|---  
[ApplicationLicenseType](P_Tessa_Platform_Runtime_ISessionLoginContext_ApplicationLicenseType.htm)|
Тип лицензии, потребляемой при входе.  
[CancellationToken](P_Tessa_Platform_Runtime_ISessionLoginContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[ExpectedLoginType](P_Tessa_Platform_Runtime_ISessionLoginContext_ExpectedLoginType.htm)|
Ожидаемый тип входа или null, если тип входа определяется автоматически.  
[HostIP](P_Tessa_Platform_Runtime_ISessionLoginContext_HostIP.htm)|  IP адрес
компьютера, с которого выполняется вход, или null, если адрес недоступен.  
[HostName](P_Tessa_Platform_Runtime_ISessionLoginContext_HostName.htm)|  DNS-
имя компьютера, с которого выполняется вход, или null, если имя недоступно.  
[Login](P_Tessa_Platform_Runtime_ISessionLoginContext_Login.htm)| Логин
сотрудника.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
