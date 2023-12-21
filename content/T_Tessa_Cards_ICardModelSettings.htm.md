# ICardModelSettings - интерфейс
Настройки модели представления карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardModelSettings : INotifyPropertyChanged, 
    	IEquatable<ICardModelSettings>, ICloneable
VB __Копировать
     Public Interface ICardModelSettings
    	Inherits INotifyPropertyChanged, IEquatable(Of ICardModelSettings), ICloneable
C++ __Копировать
     public interface class ICardModelSettings : INotifyPropertyChanged, 
    	IEquatable<ICardModelSettings^>, ICloneable
F# __Копировать
     type ICardModelSettings = 
        interface
            interface INotifyPropertyChanged
            interface IEquatable<ICardModelSettings>
            interface ICloneable
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ICardModelSettings>
##  __Свойства
[ContentWidthRatio](P_Tessa_Cards_ICardModelSettings_ContentWidthRatio.htm)|
Отношение ширины области карточки (вместе с заданиями) к суммарной ширине
области редактора карточки. Значение должно располагаться на отрезке [0;1].
Значение 1 означает, что карточка занимает всё доступное пространство без
пустой области справа. Значение 0.5 означает, что карточка занимает половину
доступной ширины, а значение 0.25 определяет, что ширина области карточки в
три раза меньше, чем пустая область справа.  
---|---  
[FilePreviewIsHidden](P_Tessa_Cards_ICardModelSettings_FilePreviewIsHidden.htm)|
Признак того, что область предпросмотра файлов скрыта.  
[FilePreviewPosition](P_Tessa_Cards_ICardModelSettings_FilePreviewPosition.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[FilePreviewWidthRatio](P_Tessa_Cards_ICardModelSettings_FilePreviewWidthRatio.htm)|
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра. Значение должно располагаться на отрезке [0;1].
Значение 0.5 означает, что области распределены в равных долях, а значение
0.25 определяет, что ширина области предпросмотра в три раза меньше, чем
область карточки.  
[TaskAreaWidth](P_Tessa_Cards_ICardModelSettings_TaskAreaWidth.htm)| Ширина
области с заданиями (в пикселях). Значение не должно быть меньше нуля.  
##  __Методы
[Clone](M_Tessa_Cards_ICardModelSettings_Clone.htm)| Создаёт полную копию
объекта с настройками.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ICardModelSettings>)  
[SetContentWidthRatioAsync](M_Tessa_Cards_ICardModelSettings_SetContentWidthRatioAsync.htm)|
Отношение ширины области карточки (вместе с заданиями) к суммарной ширине
области редактора карточки.  
[SetFilePreviewIsHiddenAsync](M_Tessa_Cards_ICardModelSettings_SetFilePreviewIsHiddenAsync.htm)|
Признак того, что область предпросмотра файлов скрыта.  
[SetFilePreviewPositionAsync](M_Tessa_Cards_ICardModelSettings_SetFilePreviewPositionAsync.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[SetFilePreviewWidthRatioAsync](M_Tessa_Cards_ICardModelSettings_SetFilePreviewWidthRatioAsync.htm)|
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра.  
[SetTaskAreaWidthAsync](M_Tessa_Cards_ICardModelSettings_SetTaskAreaWidthAsync.htm)|
Ширина области с заданиями (в пикселях).  
[SetupFromAsync](M_Tessa_Cards_ICardModelSettings_SetupFromAsync.htm)|
Устанавливает настройки из данных в заданной хеш-таблице.  
[Store](M_Tessa_Cards_ICardModelSettings_Store.htm)| Сохраняет настройки в
заданной хеш-таблице.  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
