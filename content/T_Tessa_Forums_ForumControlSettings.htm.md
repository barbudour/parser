# ForumControlSettings - класс
Предоставляет пользовательские настройки для контрола обсуждения.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumControlSettings : NotificationObject, 
    	IForumControlSettings, INotifyPropertyChanged
VB __Копировать
     Public NotInheritable Class ForumControlSettings
    	Inherits NotificationObject
    	Implements IForumControlSettings, INotifyPropertyChanged
C++ __Копировать
     public ref class ForumControlSettings sealed : public NotificationObject, 
    	IForumControlSettings, INotifyPropertyChanged
F# __Копировать
     [<SealedAttribute>]
    type ForumControlSettings = 
        class
            inherit NotificationObject
            interface IForumControlSettings
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ ForumControlSettings
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IForumControlSettings](T_Tessa_Forums_IForumControlSettings.htm)
##  __Конструкторы
[ForumControlSettings](M_Tessa_Forums_ForumControlSettings__ctor.htm)|
Инициализирует новый экземпляр класса ForumControlSettings  
---|---  
##  __Свойства
[ContentRatio](P_Tessa_Forums_ForumControlSettings_ContentRatio.htm)|
Соотношение контрола обсуждение к пустым слева и справа полям от контрола.  
---|---  
[ForumMaxAttachedFiles](P_Tessa_Forums_ForumControlSettings_ForumMaxAttachedFiles.htm)|
Максимальное количество файлов, приложенных к сообщению.  
[ForumMaxAttachedFileSizeKb](P_Tessa_Forums_ForumControlSettings_ForumMaxAttachedFileSizeKb.htm)|
Максимальный размер файла, приложенного к сообщению, Кб.  
[ForumMaxMessageInlines](P_Tessa_Forums_ForumControlSettings_ForumMaxMessageInlines.htm)|
Максимальное количество вложений
[InnerItem](T_Tessa_Forums_Models_AttachmentType.htm) в сообщении (например,
вставленных изображений).  
[ForumMaxMessageSize](P_Tessa_Forums_ForumControlSettings_ForumMaxMessageSize.htm)|
Максимальное количество символов в сообщении.  
[HideTopicListNavigation](P_Tessa_Forums_ForumControlSettings_HideTopicListNavigation.htm)|
Скрывать кнопку перейти к обсуждениям. Необходимо для singleton обсуждений.  
[InputBlockHeight](P_Tessa_Forums_ForumControlSettings_InputBlockHeight.htm)|
Высота блока с вводом сообщения.  
[IsFullSize](P_Tessa_Forums_ForumControlSettings_IsFullSize.htm)|  Растянуть
по ширине  
## __Методы
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
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[SetupFromAsync](M_Tessa_Forums_ForumControlSettings_SetupFromAsync.htm)|
Установить настройки из модели
[ForumServerSettings](T_Tessa_Forums_ForumServerSettings.htm)  
[Store](M_Tessa_Forums_ForumControlSettings_Store.htm)|  Сохранить
пользовательский настройки контрола обсуждение.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Поля
[DefaultContantRatio](F_Tessa_Forums_ForumControlSettings_DefaultContantRatio.htm)|  
---|---  
[DefaultInputBlockHeight](F_Tessa_Forums_ForumControlSettings_DefaultInputBlockHeight.htm)|  
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
