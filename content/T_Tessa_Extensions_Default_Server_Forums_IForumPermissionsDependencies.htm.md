# IForumPermissionsDependencies - интерфейс
Объект, содержащий в себе зависимости для
[IForumPermissionsProvider](T_Tessa_Forums_IForumPermissionsProvider.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Forums](N_Tessa_Extensions_Default_Server_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumPermissionsDependencies
VB __Копировать
     Public Interface IForumPermissionsDependencies
C++ __Копировать
     public interface class IForumPermissionsDependencies
F# __Копировать
     type IForumPermissionsDependencies = interface end
##  __Свойства
[DbScope](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_DbScope.htm)|
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
[ForumParticipantProvider](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_ForumParticipantProvider.htm)|
Интерфейс для получения текущего пользователя, как участника топика.  
[KrPermissionsCacheContainer](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_KrPermissionsCacheContainer.htm)|
Контейнер кеша правил доступа.  
[KrPermissionsManager](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_KrPermissionsManager.htm)|
Объект, который выполняет проверку прав доступа  
[KrTokenProvider](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_KrTokenProvider.htm)|
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.  
[Session](P_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies_Session.htm)|
Сессия пользователя.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Forums - пространство
имён](N_Tessa_Extensions_Default_Server_Forums.htm)
