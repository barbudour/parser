# KrClientForumPermissionsProvider - класс
Объект, определяющий доступ к обсуждениями на основании правил доступа типовой
системы прав. Реализация для использования на клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Forums](N_Tessa_Extensions_Default_Client_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrClientForumPermissionsProvider : ForumPermissionsProvider
VB __Копировать
     Public Class KrClientForumPermissionsProvider
    	Inherits ForumPermissionsProvider
C++ __Копировать
     public ref class KrClientForumPermissionsProvider : public ForumPermissionsProvider
F# __Копировать
     type KrClientForumPermissionsProvider = 
        class
            inherit ForumPermissionsProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ForumPermissionsProvider](T_Tessa_Forums_ForumPermissionsProvider.htm) __ KrClientForumPermissionsProvider
##  __Конструкторы
[KrClientForumPermissionsProvider](M_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider__ctor.htm)|
Инициализирует новый экземпляр класса KrClientForumPermissionsProvider  
---|---  
##  __Методы
[CheckAddTopicPermissionAsync](M_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider_CheckAddTopicPermissionAsync.htm)|
Проверяет право текущего пользователя на добавление топиков в обсуждения по
указанной карточке. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
(Переопределяет [ForumPermissionsProvider.CheckAddTopicPermissionAsync(Guid,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Forums_ForumPermissionsProvider_CheckAddTopicPermissionAsync.htm))  
---|---  
[CheckEditMessagesPermissionAsync](M_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider_CheckEditMessagesPermissionAsync.htm)|
Проверяет право текущего пользователя на редактирование сообщений в заданном
топике. Возвращает признак того, что запрошенные права успешно получены, и
результат валидации с сообщениями об ошибках и предупреждениями.  
(Переопределяет
[ForumPermissionsProvider.CheckEditMessagesPermissionAsync(Guid,
Nullable<Guid>, Boolean, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Forums_ForumPermissionsProvider_CheckEditMessagesPermissionAsync.htm))  
[CheckSuperModeratorPermissionAsync](M_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider_CheckSuperModeratorPermissionAsync.htm)|
Проверяет право текущего пользователя на доступ к обсуждениям в режиме
супермодератора. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
(Переопределяет
[ForumPermissionsProvider.CheckSuperModeratorPermissionAsync(Guid,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Forums_ForumPermissionsProvider_CheckSuperModeratorPermissionAsync.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAvailableTopicsAsync](M_Tessa_Forums_ForumPermissionsProvider_GetAvailableTopicsAsync.htm)|
Получает коллекцию доступных для пользователя топиков в карточке.  
(Унаследован от
[ForumPermissionsProvider](T_Tessa_Forums_ForumPermissionsProvider.htm))  
[GetEditPermissionsInfoAsync](M_Tessa_Forums_ForumPermissionsProvider_GetEditPermissionsInfoAsync.htm)|
Проверяет наличие прав на редактирование сообщений у пользователя в заданном
топике и создает токен с рассчитанными правами.  
(Унаследован от
[ForumPermissionsProvider](T_Tessa_Forums_ForumPermissionsProvider.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[ResolveUserPermissionsAsync](M_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider_ResolveUserPermissionsAsync.htm)|
Получает права доступа текущего пользователя к топику.  
(Переопределяет [ForumPermissionsProvider.ResolveUserPermissionsAsync(Guid,
Nullable<Guid>, Boolean, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Forums_ForumPermissionsProvider_ResolveUserPermissionsAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
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
[Tessa.Extensions.Default.Client.Forums - пространство
имён](N_Tessa_Extensions_Default_Client_Forums.htm)
