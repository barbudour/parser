# IForumControlSettings - интерфейс
Интерфейс для обработки пользовательских настроек для контрола обсуждения.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumControlSettings : INotifyPropertyChanged
VB __Копировать
     Public Interface IForumControlSettings
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IForumControlSettings : INotifyPropertyChanged
F# __Копировать
     type IForumControlSettings = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[ContentRatio](P_Tessa_Forums_IForumControlSettings_ContentRatio.htm)|
Соотношение контрола обсуждение к пустым слева и справа полям от контрола.  
---|---  
[ForumMaxAttachedFiles](P_Tessa_Forums_IForumControlSettings_ForumMaxAttachedFiles.htm)|
Максимальное количество файлов, приложенных к сообщению.  
[ForumMaxAttachedFileSizeKb](P_Tessa_Forums_IForumControlSettings_ForumMaxAttachedFileSizeKb.htm)|
Максимальный размер файла, приложенного к сообщению, Кб.  
[ForumMaxMessageInlines](P_Tessa_Forums_IForumControlSettings_ForumMaxMessageInlines.htm)|
Максимальное количество вложений
[InnerItem](T_Tessa_Forums_Models_AttachmentType.htm) в сообщении (например,
вставленных изображений).  
[ForumMaxMessageSize](P_Tessa_Forums_IForumControlSettings_ForumMaxMessageSize.htm)|
Максимальное количество символов в сообщении.  
[HideTopicListNavigation](P_Tessa_Forums_IForumControlSettings_HideTopicListNavigation.htm)|
Скрывать кнопку перейти к обсуждениям. Необходимо для singleton обсуждений.  
[InputBlockHeight](P_Tessa_Forums_IForumControlSettings_InputBlockHeight.htm)|
Высота блока с вводом сообщения.  
[IsFullSize](P_Tessa_Forums_IForumControlSettings_IsFullSize.htm)|  Растянуть
по ширине  
## __Методы
[SetupFromAsync](M_Tessa_Forums_IForumControlSettings_SetupFromAsync.htm)|
Установить настройки из модели
[ForumServerSettings](T_Tessa_Forums_ForumServerSettings.htm)  
---|---  
[Store](M_Tessa_Forums_IForumControlSettings_Store.htm)|  Сохранить
пользовательский настройки контрола обсуждение.  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
