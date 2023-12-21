# ForumServerSettings - класс
Интерфейс для получения настроек обсуждений из карточки "настройки сервера".
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumServerSettings : IForumServerSettings
VB __Копировать
     Public NotInheritable Class ForumServerSettings
    	Implements IForumServerSettings
C++ __Копировать
     public ref class ForumServerSettings sealed : IForumServerSettings
F# __Копировать
     [<SealedAttribute>]
    type ForumServerSettings = 
        class
            interface IForumServerSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ForumServerSettings
Implements
    [IForumServerSettings](T_Tessa_Forums_IForumServerSettings.htm)
##  __Конструкторы
[ForumServerSettings](M_Tessa_Forums_ForumServerSettings__ctor.htm)|
Инициализирует новый экземпляр класса ForumServerSettings  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetForumMaxAttachedFilesAsync](M_Tessa_Forums_ForumServerSettings_GetForumMaxAttachedFilesAsync.htm)|
Возвращает максимальное количество файлов, приложенных к сообщению.  
[GetForumMaxAttachedFileSizeKbAsync](M_Tessa_Forums_ForumServerSettings_GetForumMaxAttachedFileSizeKbAsync.htm)|
Возвращает максимальный размер файла, приложенного к сообщению.  
[GetForumMaxMessageInlinesAsync](M_Tessa_Forums_ForumServerSettings_GetForumMaxMessageInlinesAsync.htm)|
Возвращает максимальное количество вложений
[InnerItem](T_Tessa_Forums_Models_AttachmentType.htm) в сообщении (например,
вставленных изображений).  
[GetForumMaxMessageSizeAsync](M_Tessa_Forums_ForumServerSettings_GetForumMaxMessageSizeAsync.htm)|
Возвращает максимальное количество символов в сообщении.  
[GetForumRefreshIntervalAsync](M_Tessa_Forums_ForumServerSettings_GetForumRefreshIntervalAsync.htm)|
Возвращает интервал обновления индикатора уведомлений.  
[GetFullTextMessageSearchAsync](M_Tessa_Forums_ForumServerSettings_GetFullTextMessageSearchAsync.htm)|
Возвращает значение включен ли Полнотекстовый поиск по сообщениям.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetModifyMessageAtNoOlderThanAsync](M_Tessa_Forums_ForumServerSettings_GetModifyMessageAtNoOlderThanAsync.htm)|
Возврашает значение "Редактировать сообщения не старше, чем" в минутах.  
[GetModifyOwnMessageAtNoOlderThanAsync](M_Tessa_Forums_ForumServerSettings_GetModifyOwnMessageAtNoOlderThanAsync.htm)|
Возврашает значение "Редактировать собственные сообщения не старше, чем" в
минутах.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DefaultForumMaxAttachedFiles](F_Tessa_Forums_ForumServerSettings_DefaultForumMaxAttachedFiles.htm)|  
---|---  
[DefaultForumMaxAttachedFileSizeKb](F_Tessa_Forums_ForumServerSettings_DefaultForumMaxAttachedFileSizeKb.htm)|  
[DefaultForumMaxMessageInlines](F_Tessa_Forums_ForumServerSettings_DefaultForumMaxMessageInlines.htm)|  
[DefaultForumMaxMessageSize](F_Tessa_Forums_ForumServerSettings_DefaultForumMaxMessageSize.htm)|  
[DefaultForumRefreshInterval](F_Tessa_Forums_ForumServerSettings_DefaultForumRefreshInterval.htm)|  
[DefaultModifyMessageAtNoOlderThan](F_Tessa_Forums_ForumServerSettings_DefaultModifyMessageAtNoOlderThan.htm)|  
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
