# ForumPermissionsProvider - класс
Объект, предоставляющий права доступа в соответствии с активной системой прав.
Например, для типового решения выполняет проверки на основании правил доступа
и токена KrToken.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ForumPermissionsProvider : IForumPermissionsProvider
VB __Копировать
     Public Class ForumPermissionsProvider
    	Implements IForumPermissionsProvider
C++ __Копировать
     public ref class ForumPermissionsProvider : IForumPermissionsProvider
F# __Копировать
     type ForumPermissionsProvider = 
        class
            interface IForumPermissionsProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ForumPermissionsProvider
Derived
[Tessa.Extensions.Default.Client.Forums.KrClientForumPermissionsProvider](T_Tessa_Extensions_Default_Client_Forums_KrClientForumPermissionsProvider.htm)
[Tessa.Extensions.Default.Server.Forums.KrForumPermissionsProvider](T_Tessa_Extensions_Default_Server_Forums_KrForumPermissionsProvider.htm)
Implements
    [IForumPermissionsProvider](T_Tessa_Forums_IForumPermissionsProvider.htm)
##  __Заметки
В этой реализации все действия разрешены и все права присутствуют.
## __Конструкторы
[ForumPermissionsProvider](M_Tessa_Forums_ForumPermissionsProvider__ctor.htm)|
Инициализирует новый экземпляр класса ForumPermissionsProvider  
---|---  
##  __Методы
[CheckAddTopicPermissionAsync](M_Tessa_Forums_ForumPermissionsProvider_CheckAddTopicPermissionAsync.htm)|
Проверяет право текущего пользователя на добавление топиков в обсуждения по
указанной карточке. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
---|---  
[CheckEditMessagesPermissionAsync](M_Tessa_Forums_ForumPermissionsProvider_CheckEditMessagesPermissionAsync.htm)|
Проверяет право текущего пользователя на редактирование сообщений в заданном
топике. Возвращает признак того, что запрошенные права успешно получены, и
результат валидации с сообщениями об ошибках и предупреждениями.  
[CheckSuperModeratorPermissionAsync](M_Tessa_Forums_ForumPermissionsProvider_CheckSuperModeratorPermissionAsync.htm)|
Проверяет право текущего пользователя на доступ к обсуждениям в режиме
супермодератора. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
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
[GetEditPermissionsInfoAsync](M_Tessa_Forums_ForumPermissionsProvider_GetEditPermissionsInfoAsync.htm)|
Проверяет наличие прав на редактирование сообщений у пользователя в заданном
топике и создает токен с рассчитанными правами.  
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
[ResolveUserPermissionsAsync](M_Tessa_Forums_ForumPermissionsProvider_ResolveUserPermissionsAsync.htm)|
Получает права доступа текущего пользователя к топику.  
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
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
