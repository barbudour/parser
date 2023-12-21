# ITessaShellTab - интерфейс
Вкладка приложения [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm).
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaShellTab : INotifyPropertyChanged
VB __Копировать
     Public Interface ITessaShellTab
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class ITessaShellTab : INotifyPropertyChanged
F# __Копировать
     type ITessaShellTab = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[TryGetUIContext](M_Tessa_UI_Windows_WindowExtensions_TryGetUIContext.htm)|
Возвращает объект [IUIContext](T_Tessa_UI_IUIContext.htm), соответствующий
вкладке приложения, или null, если объект не связана со вкладкой.  
(Определяется [WindowExtensions](T_Tessa_UI_Windows_WindowExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
