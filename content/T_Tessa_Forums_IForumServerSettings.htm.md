# IForumServerSettings - интерфейс
Интерфейс для получения настроек обсуждений из карточки "настройки сервера".
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumServerSettings
VB __Копировать
     Public Interface IForumServerSettings
C++ __Копировать
     public interface class IForumServerSettings
F# __Копировать
     type IForumServerSettings = interface end
##  __Методы
[GetForumMaxAttachedFilesAsync](M_Tessa_Forums_IForumServerSettings_GetForumMaxAttachedFilesAsync.htm)|
Возвращает максимальное количество файлов, приложенных к сообщению.  
---|---  
[GetForumMaxAttachedFileSizeKbAsync](M_Tessa_Forums_IForumServerSettings_GetForumMaxAttachedFileSizeKbAsync.htm)|
Возвращает максимальный размер файла, приложенного к сообщению.  
[GetForumMaxMessageInlinesAsync](M_Tessa_Forums_IForumServerSettings_GetForumMaxMessageInlinesAsync.htm)|
Возвращает максимальное количество вложений
[InnerItem](T_Tessa_Forums_Models_AttachmentType.htm) в сообщении (например,
вставленных изображений).  
[GetForumMaxMessageSizeAsync](M_Tessa_Forums_IForumServerSettings_GetForumMaxMessageSizeAsync.htm)|
Возвращает максимальное количество символов в сообщении.  
[GetForumRefreshIntervalAsync](M_Tessa_Forums_IForumServerSettings_GetForumRefreshIntervalAsync.htm)|
Возвращает интервал обновления индикатора уведомлений.  
[GetFullTextMessageSearchAsync](M_Tessa_Forums_IForumServerSettings_GetFullTextMessageSearchAsync.htm)|
Возвращает значение включен ли Полнотекстовый поиск по сообщениям.  
[GetModifyMessageAtNoOlderThanAsync](M_Tessa_Forums_IForumServerSettings_GetModifyMessageAtNoOlderThanAsync.htm)|
Возврашает значение "Редактировать сообщения не старше, чем" в минутах.  
[GetModifyOwnMessageAtNoOlderThanAsync](M_Tessa_Forums_IForumServerSettings_GetModifyOwnMessageAtNoOlderThanAsync.htm)|
Возврашает значение "Редактировать собственные сообщения не старше, чем" в
минутах.  
## __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
