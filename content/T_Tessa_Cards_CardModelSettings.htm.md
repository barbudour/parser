# CardModelSettings - класс
Настройки модели представления карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardModelSettings : NotificationObject, 
    	ICardModelSettings, INotifyPropertyChanged, IEquatable<ICardModelSettings>, ICloneable
VB __Копировать
     Public NotInheritable Class CardModelSettings
    	Inherits NotificationObject
    	Implements ICardModelSettings, INotifyPropertyChanged, IEquatable(Of ICardModelSettings), 
    	ICloneable
C++ __Копировать
     public ref class CardModelSettings sealed : public NotificationObject, 
    	ICardModelSettings, INotifyPropertyChanged, IEquatable<ICardModelSettings^>, ICloneable
F# __Копировать
     [<SealedAttribute>]
    type CardModelSettings = 
        class
            inherit NotificationObject
            interface ICardModelSettings
            interface INotifyPropertyChanged
            interface IEquatable<ICardModelSettings>
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ CardModelSettings
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm)>, [ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm)
##  __Конструкторы
[CardModelSettings()](M_Tessa_Cards_CardModelSettings__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
[CardModelSettings(Dictionary<String,
Object>)](M_Tessa_Cards_CardModelSettings__ctor_1.htm)|  Создаёт экземпляр
класса по свойствам, заданным в хеш-таблице.  
[CardModelSettings(ICardModelSettings)](M_Tessa_Cards_CardModelSettings__ctor_2.htm)|
Создаёт экземпляр класса, свойства которого копируются из заданного объекта.  
## __Свойства
[ContentWidthRatio](P_Tessa_Cards_CardModelSettings_ContentWidthRatio.htm)|
Отношение ширины области карточки (вместе с заданиями) к суммарной ширине
области редактора карточки. Значение должно располагаться на отрезке [0;1].
Значение 1 означает, что карточка занимает всё доступное пространство без
пустой области справа. Значение 0.5 означает, что карточка занимает половину
доступной ширины, а значение 0.25 определяет, что ширина области карточки в
три раза меньше, чем пустая область справа.  
---|---  
[FilePreviewIsHidden](P_Tessa_Cards_CardModelSettings_FilePreviewIsHidden.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[FilePreviewPosition](P_Tessa_Cards_CardModelSettings_FilePreviewPosition.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[FilePreviewWidthRatio](P_Tessa_Cards_CardModelSettings_FilePreviewWidthRatio.htm)|
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра. Значение должно располагаться на отрезке [0;1].
Значение 0.5 означает, что области распределены в равных долях, а значение
0.25 определяет, что ширина области предпросмотра в три раза меньше, чем
область карточки.  
[TaskAreaWidth](P_Tessa_Cards_CardModelSettings_TaskAreaWidth.htm)| Ширина
области с заданиями (в пикселях). Значение не должно быть меньше нуля.  
##  __Методы
[Clone](M_Tessa_Cards_CardModelSettings_Clone.htm)| Создаёт полную копию
объекта с настройками.  
---|---  
[Equals(ICardModelSettings)](M_Tessa_Cards_CardModelSettings_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_CardModelSettings_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_CardModelSettings_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[SetContentWidthRatioAsync](M_Tessa_Cards_CardModelSettings_SetContentWidthRatioAsync.htm)|
Отношение ширины области карточки (вместе с заданиями) к суммарной ширине
области редактора карточки.  
[SetFilePreviewIsHiddenAsync](M_Tessa_Cards_CardModelSettings_SetFilePreviewIsHiddenAsync.htm)|
Признак того, что область предпросмотра файлов скрыта.  
[SetFilePreviewPositionAsync](M_Tessa_Cards_CardModelSettings_SetFilePreviewPositionAsync.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[SetFilePreviewWidthRatioAsync](M_Tessa_Cards_CardModelSettings_SetFilePreviewWidthRatioAsync.htm)|
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра.  
[SetTaskAreaWidthAsync](M_Tessa_Cards_CardModelSettings_SetTaskAreaWidthAsync.htm)|
Ширина области с заданиями (в пикселях).  
[SetupFromAsync](M_Tessa_Cards_CardModelSettings_SetupFromAsync.htm)|
Устанавливает настройки из данных в заданной хеш-таблице.  
[Store](M_Tessa_Cards_CardModelSettings_Store.htm)| Сохраняет настройки в
заданной хеш-таблице.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetStorageFromSatellite](M_Tessa_Cards_CardModelSettings_TryGetStorageFromSatellite.htm)|
Возвращает хранилище с сериализованным объектом, который можно использовать в
методе [SetupFromAsync(Dictionary<String, Object>, Func<Action,
CancellationToken, Task>,
CancellationToken)](M_Tessa_Cards_CardModelSettings_SetupFromAsync.htm).  
## __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Поля
[DefaultContentWidthRatio](F_Tessa_Cards_CardModelSettings_DefaultContentWidthRatio.htm)|
Значение по умолчанию для свойства
[ContentWidthRatio](P_Tessa_Cards_CardModelSettings_ContentWidthRatio.htm).  
---|---  
[DefaultFilePreviewWidthRatio](F_Tessa_Cards_CardModelSettings_DefaultFilePreviewWidthRatio.htm)|
Значение по умолчанию для свойства
[FilePreviewWidthRatio](P_Tessa_Cards_CardModelSettings_FilePreviewWidthRatio.htm).  
[DefaultTaskAreaWidth](F_Tessa_Cards_CardModelSettings_DefaultTaskAreaWidth.htm)|
Значение по умолчанию для свойства
[TaskAreaWidth](P_Tessa_Cards_CardModelSettings_TaskAreaWidth.htm).  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
