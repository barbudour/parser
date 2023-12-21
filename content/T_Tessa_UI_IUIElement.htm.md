# IUIElement - интерфейс
Описание интерфейса для моделей-представления пользовательского интерфейса
поддерживающих режим установки доступности и признака отображения элемента в
пользовательском интерфейсе
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIElement : INotifyPropertyChanged
VB __Копировать
     Public Interface IUIElement
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IUIElement : INotifyPropertyChanged
F# __Копировать
     type IUIElement = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[IsEnabled](P_Tessa_UI_IUIElement_IsEnabled.htm)|  Признак доступности
элемента для взаимодействия  
---|---  
[IsVisible](P_Tessa_UI_IUIElement_IsVisible.htm)|  Признак отображения
элемента в пользовательском интерфейса  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
