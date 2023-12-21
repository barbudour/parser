# IAdExtensionContext - интерфейс
Контекст операции, связанной с синхронизацией Active Directory.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAdExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IAdExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IAdExtensionContext : IExtensionContext
F# __Копировать
     type IAdExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[Cancel](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Cancel.htm)|
Отмена сохранения карточки.  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[Card](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Card.htm)|
Информация о карточке.  
[Connection](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Connection.htm)|
Соединение с сервером LDAP  
[Entry](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Entry.htm)|
Ldap объект, источник синхронизации  
[Info](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
[SyncContext](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_SyncContext.htm)|
Контекст синхронизации.  
[UpdateUser](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_UpdateUser.htm)|
Обновлять ли пользователей в указанном подразделении/роли  
[Users](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_Users.htm)|
Список пользователей указанного подразделения  
[ValidationResult](P_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext_ValidationResult.htm)|
Сообщения валидации.  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
