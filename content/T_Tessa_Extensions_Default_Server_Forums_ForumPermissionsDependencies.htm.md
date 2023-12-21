# ForumPermissionsDependencies - класс
Объект, содержащий в себе зависимости для
[IForumPermissionsProvider](T_Tessa_Forums_IForumPermissionsProvider.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Forums](N_Tessa_Extensions_Default_Server_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class ForumPermissionsDependencies : IForumPermissionsDependencies, 
    	IEquatable<ForumPermissionsDependencies>
VB __Копировать
     Public Class ForumPermissionsDependencies
    	Implements IForumPermissionsDependencies, IEquatable(Of ForumPermissionsDependencies)
C++ __Копировать
     public ref class ForumPermissionsDependencies : IForumPermissionsDependencies, 
    	IEquatable<ForumPermissionsDependencies^>
F# __Копировать
     type ForumPermissionsDependencies = 
        class
            interface IForumPermissionsDependencies
            interface IEquatable<ForumPermissionsDependencies>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ForumPermissionsDependencies
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ForumPermissionsDependencies>, [IForumPermissionsDependencies](T_Tessa_Extensions_Default_Server_Forums_IForumPermissionsDependencies.htm)
##  __Конструкторы
[ForumPermissionsDependencies](M_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies__ctor.htm)|
Объект, содержащий в себе зависимости для
[IForumPermissionsProvider](T_Tessa_Forums_IForumPermissionsProvider.htm)  
---|---  
##  __Свойства
[DbScope](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_DbScope.htm)|
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
[ForumParticipantProvider](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_ForumParticipantProvider.htm)|
Интерфейс для получения текущего пользователя, как участника топика.  
[KrPermissionsCacheContainer](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_KrPermissionsCacheContainer.htm)|
Контейнер кеша правил доступа.  
[KrPermissionsManager](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_KrPermissionsManager.htm)|
Объект, который выполняет проверку прав доступа  
[KrTokenProvider](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_KrTokenProvider.htm)|
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.  
[Session](P_Tessa_Extensions_Default_Server_Forums_ForumPermissionsDependencies_Session.htm)|
Сессия пользователя.  
## __Методы
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Forums - пространство
имён](N_Tessa_Extensions_Default_Server_Forums.htm)
