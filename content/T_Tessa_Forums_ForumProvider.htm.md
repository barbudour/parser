# ForumProvider - класс
##  __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumProvider : IForumProvider, 
    	IAttachmentManager
VB __Копировать
     Public NotInheritable Class ForumProvider
    	Implements IForumProvider, IAttachmentManager
C++ __Копировать
     public ref class ForumProvider sealed : IForumProvider, 
    	IAttachmentManager
F# __Копировать
     [<SealedAttribute>]
    type ForumProvider = 
        class
            interface IForumProvider
            interface IAttachmentManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ForumProvider
Implements
    [IAttachmentManager](T_Tessa_Forums_IAttachmentManager.htm), [IForumProvider](T_Tessa_Forums_IForumProvider.htm)
##  __Конструкторы
[ForumProvider](M_Tessa_Forums_ForumProvider__ctor.htm)| Инициализирует новый
экземпляр класса ForumProvider  
---|---  
##  __Методы
[AddParticipantsAsync](M_Tessa_Forums_ForumProvider_AddParticipantsAsync.htm)|
Добавляет участников в топик.  
---|---  
[AddRolesAsync](M_Tessa_Forums_ForumProvider_AddRolesAsync.htm)|  Добавляет
роли участников в топик.  
[AddTopicAsync](M_Tessa_Forums_ForumProvider_AddTopicAsync.htm)|  Создаёт
топик.  
[ArchiveTopicAsync](M_Tessa_Forums_ForumProvider_ArchiveTopicAsync.htm)|
Выполняет архивирование или разархивирование топика.  
[CheckPermissionByFileAsync](M_Tessa_Forums_ForumProvider_CheckPermissionByFileAsync.htm)|
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
[GetMessagesAsync](M_Tessa_Forums_ForumProvider_GetMessagesAsync.htm)|
Загружает сообщения топика.  
[GetSatelliteIDAsync](M_Tessa_Forums_ForumProvider_GetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для обсуждений.  
[GetTopicAsync](M_Tessa_Forums_ForumProvider_GetTopicAsync.htm)|  Возвращает
информацию по указанному топику.  
[GetTopicsWithMessagesAsync](M_Tessa_Forums_ForumProvider_GetTopicsWithMessagesAsync.htm)|
Возвращает список топиков с последними сообщениями в каждом из них.  
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
[RemoveParticipantsAsync](M_Tessa_Forums_ForumProvider_RemoveParticipantsAsync.htm)|
Удаляет участников топика.  
[RemoveRolesAsync](M_Tessa_Forums_ForumProvider_RemoveRolesAsync.htm)|
Удаляет роли участников из топика.  
[SendMessageAsync](M_Tessa_Forums_ForumProvider_SendMessageAsync.htm)|
Отправляет сообщение в топике.  
[SetForumSettingsAsync](M_Tessa_Forums_ForumProvider_SetForumSettingsAsync.htm)|
Сохраняет глобальные (сейчас визуальные) настройки топика.  
[SubscribeAsync](M_Tessa_Forums_ForumProvider_SubscribeAsync.htm)|
Подписывает или отписывает текущего сотрудника как участника топика.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateMessageAsync](M_Tessa_Forums_ForumProvider_UpdateMessageAsync.htm)|
Редактирует ранее отправленное сообщение.  
[UpdateParticipantsAsync](M_Tessa_Forums_ForumProvider_UpdateParticipantsAsync.htm)|
Изменяет свойства участников в топике.  
[UpdateRolesAsync](M_Tessa_Forums_ForumProvider_UpdateRolesAsync.htm)|
Изменяет роли участников в топике.  
## __Поля
[ForumPrefixKey](F_Tessa_Forums_ForumProvider_ForumPrefixKey.htm)|  
---|---  
[KrTokenKey](F_Tessa_Forums_ForumProvider_KrTokenKey.htm)|  
[ModifyMessageAtNoOlderThanKey](F_Tessa_Forums_ForumProvider_ModifyMessageAtNoOlderThanKey.htm)|  
[ModifyOwnMessageAtNoOlderThanKey](F_Tessa_Forums_ForumProvider_ModifyOwnMessageAtNoOlderThanKey.htm)|  
[SatelliteIDKey](F_Tessa_Forums_ForumProvider_SatelliteIDKey.htm)|  
[TopicIDsKey](F_Tessa_Forums_ForumProvider_TopicIDsKey.htm)|  
[TopicModelKey](F_Tessa_Forums_ForumProvider_TopicModelKey.htm)|  
## __Методы расширения
[AddFilesAsync](M_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions_AddFilesAsync.htm)|  
(Определяется
[AttachmentUIManagerExtensions](T_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions.htm))  
---|---  
[CreateGetFileContentFromCardAsyncFunc](M_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions_CreateGetFileContentFromCardAsyncFunc.htm)|  
(Определяется
[AttachmentUIManagerExtensions](T_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetFileContentAsync](M_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions_GetFileContentAsync.htm)|  
(Определяется
[AttachmentUIManagerExtensions](T_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions.htm))  
[GetFileContentFromCardAsync](M_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions_GetFileContentFromCardAsync.htm)|  
(Определяется
[AttachmentUIManagerExtensions](T_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[RemoveFileAsync](M_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions_RemoveFileAsync.htm)|  
(Определяется
[AttachmentUIManagerExtensions](T_Tessa_UI_Cards_Forums_AttachmentUIManagerExtensions.htm))  
[SaveAttachmentsToСardAsync](M_Tessa_Forums_ExtensionClasses_AttachmentManagerExtensions_SaveAttachmentsToСardAsync.htm)|
Cохраняет файлы приложенные RichTextBox (в том числе в сообщениях форума) к
карточке  
(Определяется
[AttachmentManagerExtensions](T_Tessa_Forums_ExtensionClasses_AttachmentManagerExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
