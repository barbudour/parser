# ISelectableViewModel - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISelectableViewModel : IViewModel, 
    	INotifyPropertyChanged
VB __Копировать
     Public Interface ISelectableViewModel
    	Inherits IViewModel, INotifyPropertyChanged
C++ __Копировать
     public interface class ISelectableViewModel : IViewModel, 
    	INotifyPropertyChanged
F# __Копировать
     type ISelectableViewModel = 
        interface
            interface IViewModel
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IViewModel](T_Tessa_UI_IViewModel.htm)
##  __Свойства
[IsSelectable](P_Tessa_UI_ISelectableViewModel_IsSelectable.htm)|  
---|---  
[IsSelected](P_Tessa_UI_ISelectableViewModel_IsSelected.htm)|  
[Model](P_Tessa_UI_IViewModel_Model.htm)|  
(Унаследован от [IViewModel](T_Tessa_UI_IViewModel.htm))  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
