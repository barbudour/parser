# ForumProviderStrategy - класс
##  __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumProviderStrategy : PlainMessageFiller, 
    	IForumProviderStrategy, IForumProvider
VB __Копировать
     Public NotInheritable Class ForumProviderStrategy
    	Inherits PlainMessageFiller
    	Implements IForumProviderStrategy, IForumProvider
C++ __Копировать
     public ref class ForumProviderStrategy sealed : public PlainMessageFiller, 
    	IForumProviderStrategy, IForumProvider
F# __Копировать
     [<SealedAttribute>]
    type ForumProviderStrategy = 
        class
            inherit PlainMessageFiller
            interface IForumProviderStrategy
            interface IForumProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PlainMessageFiller](T_Tessa_Forums_PlainMessageFiller.htm) __ ForumProviderStrategy
Implements
    [IForumProvider](T_Tessa_Forums_IForumProvider.htm), [IForumProviderStrategy](T_Tessa_Forums_IForumProviderStrategy.htm)
##  __Конструкторы
[ForumProviderStrategy](M_Tessa_Forums_ForumProviderStrategy__ctor.htm)|
Инициализирует новый экземпляр класса ForumProviderStrategy  
---|---  
##  __Методы
[AddParticipantsAsync](M_Tessa_Forums_ForumProviderStrategy_AddParticipantsAsync.htm)|
Добавляет участников в топик.  
---|---  
[AddRolesAsync](M_Tessa_Forums_ForumProviderStrategy_AddRolesAsync.htm)|
Добавляет роли участников в топик.  
[AddTopicAsync](M_Tessa_Forums_ForumProviderStrategy_AddTopicAsync.htm)|
Создаёт топик.  
[ArchiveTopicAsync](M_Tessa_Forums_ForumProviderStrategy_ArchiveTopicAsync.htm)|
Выполняет архивирование или разархивирование топика.  
[CheckPermissionByFileAsync](M_Tessa_Forums_ForumProviderStrategy_CheckPermissionByFileAsync.htm)|
Проверяет возможность загрузить файл у пользователя в сессии.  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMessagesAsync](M_Tessa_Forums_ForumProviderStrategy_GetMessagesAsync.htm)|
Загружает сообщения топика.  
[GetPlainMessage](M_Tessa_Forums_PlainMessageFiller_GetPlainMessage.htm)|
Функция для получения внутренего текста сообщения из тела сообщеня с html.  
(Унаследован от [PlainMessageFiller](T_Tessa_Forums_PlainMessageFiller.htm))  
[GetSatelliteIDAsync](M_Tessa_Forums_ForumProviderStrategy_GetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для обсуждений.  
[GetSatelliteIDByTopicAsync](M_Tessa_Forums_ForumProviderStrategy_GetSatelliteIDByTopicAsync.htm)|
Возвращает идентификаторы карточки-сателлита обсуждений и основной карточки по
идентификатору топика. Не выполняет проверки доступа для текущего сотрудника.  
[GetTopicAsync](M_Tessa_Forums_ForumProviderStrategy_GetTopicAsync.htm)|
Возвращает информацию по указанному топику.  
[GetTopicIDListByCardIDAsync](M_Tessa_Forums_ForumProviderStrategy_GetTopicIDListByCardIDAsync.htm)|
Возвращает идентификаторы всех топиков в указанной карточке. Не выполняет
проверки доступа для текущего сотрудника.  
[GetTopicsWithMessagesAsync](M_Tessa_Forums_ForumProviderStrategy_GetTopicsWithMessagesAsync.htm)|
Возвращает список топиков с последними сообщениями в каждом из них.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasUnreadMessagesAsync](M_Tessa_Forums_ForumProviderStrategy_HasUnreadMessagesAsync.htm)|
Возвращает признак того, что в указанном топике присутствуют непрочитанные
сообщения для текущего пользователя.
Возвращает HasUnreadMessages = false, если либо все сообщения прочитаны, либо
топик отсутствует.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveParticipantsAsync](M_Tessa_Forums_ForumProviderStrategy_RemoveParticipantsAsync.htm)|
Удаляет участников топика.  
[RemoveRolesAsync](M_Tessa_Forums_ForumProviderStrategy_RemoveRolesAsync.htm)|
Удаляет роли участников из топика.  
[SendMessageAsync](M_Tessa_Forums_ForumProviderStrategy_SendMessageAsync.htm)|
Отправляет сообщение в топике.  
[SetForumSettingsAsync](M_Tessa_Forums_ForumProviderStrategy_SetForumSettingsAsync.htm)|
Сохраняет глобальные (сейчас визуальные) настройки топика.  
[SubscribeAsync](M_Tessa_Forums_ForumProviderStrategy_SubscribeAsync.htm)|
Подписывает или отписывает текущего сотрудника как участника топика.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetMessageInfoAsync](M_Tessa_Forums_ForumProviderStrategy_TryGetMessageInfoAsync.htm)|
Возвращает актуальную информацию по сообщению с указанным идентификатором. Не
загружает содержимое сообщения
[Body](P_Tessa_Forums_Models_MessageModelBase_Body.htm) и приложенные файлы
[Attachments](P_Tessa_Forums_Models_MessageModel_Attachments.htm). Возвращает
null, если указанное сообщение не найдено.  
[UpdateMessageAsync](M_Tessa_Forums_ForumProviderStrategy_UpdateMessageAsync.htm)|
Редактирует ранее отправленное сообщение.  
[UpdateParticipantsAsync](M_Tessa_Forums_ForumProviderStrategy_UpdateParticipantsAsync.htm)|
Изменяет свойства участников в топике.  
[UpdateRolesAsync](M_Tessa_Forums_ForumProviderStrategy_UpdateRolesAsync.htm)|
Изменяет роли участников в топике.  
## __Методы расширения
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
