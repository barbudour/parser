# IAdSyncContext - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAdSyncContext
VB __Копировать
     Public Interface IAdSyncContext
C++ __Копировать
     public interface class IAdSyncContext
F# __Копировать
     type IAdSyncContext = interface end
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную операцию.  
---|---  
[DbScope](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на
клиенте и не равно null на сервере.  
[DnList](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_DnList.htm)|
Список всех узлов, которые необходимо синхронизировать.  
[IsUserGroupListLoaded](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_IsUserGroupListLoaded.htm)|
Загружена ли группа синхронизации пользователей.  
[LdapContext](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_LdapContext.htm)|
Контекст взаимодействия с сервером LDAP/AD по текущим открытым соединениям.  
[OperationId](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_OperationId.htm)|
ID операции синхронизации.  
[OURootsID](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_OURootsID.htm)|
ID Корней синхронизации.  
[OURootsSRID](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_OURootsSRID.htm)|
ID Корней синхронизации для статических ролей.  
[SearchProvider](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_SearchProvider.htm)|
Объект, обеспечивающий взаимодействие с API поиска объектов в AD/LDAP.  
[Settings](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_Settings.htm)|
Информация о настройках синхронизации  
[StartDate](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_StartDate.htm)|
Дата запуска операции синхронизации.  
[UnitProvider](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_UnitProvider.htm)|
Объект, обеспечивающий взаимодействие с API синхронизации объектов AD/LDAP.  
[UserGroupList](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_UserGroupList.htm)|
Список пользователей в группе синхронизации.  
[ValidationResult](P_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_ValidationResult.htm)|
Сообщения валидации.  
##  __Методы
[AddGroupToCache](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_AddGroupToCache.htm)|
Добавление новой группы в список кешируемых.  
---|---  
[AddUserToCache](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_AddUserToCache.htm)|
Добавление нового пользователя в список кешируемых.  
[GetCachedGroup](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_GetCachedGroup.htm)|
Получает состав закэшированной группы или null если группа не найдена  
[IsDnEnabled](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_IsDnEnabled.htm)|
Проверяет необходимо ли синхронизировать указанный DN.  
[IsSyncData](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_IsSyncData.htm)|
Проверяет необходимо ли синхронизировать подразделение.  
[IsSyncStaticRoles](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_IsSyncStaticRoles.htm)|
Проверяет необходимо ли синхронизировать статическую роль.  
[IsUserInCache](M_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext_IsUserInCache.htm)|
Проверяет был ли уже обновлен указанный пользователь.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
