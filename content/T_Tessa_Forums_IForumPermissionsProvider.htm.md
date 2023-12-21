# IForumPermissionsProvider - интерфейс
Объект, предоставляющий права доступа в соответствии с активной системой прав.
Например, для типового решения выполняет проверки на основании правил доступа
и токена KrToken.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumPermissionsProvider
VB __Копировать
     Public Interface IForumPermissionsProvider
C++ __Копировать
     public interface class IForumPermissionsProvider
F# __Копировать
     type IForumPermissionsProvider = interface end
##  __Методы
[CheckAddTopicPermissionAsync](M_Tessa_Forums_IForumPermissionsProvider_CheckAddTopicPermissionAsync.htm)|
Проверяет право текущего пользователя на добавление топиков в обсуждения по
указанной карточке. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
---|---  
[CheckEditMessagesPermissionAsync](M_Tessa_Forums_IForumPermissionsProvider_CheckEditMessagesPermissionAsync.htm)|
Проверяет право текущего пользователя на редактирование сообщений в заданном
топике. Возвращает признак того, что запрошенные права успешно получены, и
результат валидации с сообщениями об ошибках и предупреждениями.  
[CheckSuperModeratorPermissionAsync](M_Tessa_Forums_IForumPermissionsProvider_CheckSuperModeratorPermissionAsync.htm)|
Проверяет право текущего пользователя на доступ к обсуждениям в режиме
супермодератора. Возвращает признак того, что запрошенные права успешно
получены, и результат валидации с сообщениями об ошибках и предупреждениями.  
[GetAvailableTopicsAsync](M_Tessa_Forums_IForumPermissionsProvider_GetAvailableTopicsAsync.htm)|
Получает коллекцию доступных для пользователя топиков в карточке.  
[GetEditPermissionsInfoAsync](M_Tessa_Forums_IForumPermissionsProvider_GetEditPermissionsInfoAsync.htm)|
Проверяет наличие прав на редактирование сообщений у пользователя в заданном
топике и создает токен с рассчитанными правами.  
[ResolveUserPermissionsAsync](M_Tessa_Forums_IForumPermissionsProvider_ResolveUserPermissionsAsync.htm)|
Получает права доступа текущего пользователя к топику.  
## __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
