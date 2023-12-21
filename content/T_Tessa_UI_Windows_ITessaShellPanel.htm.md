# ITessaShellPanel - интерфейс
Информация по боковым панелям.
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaShellPanel : INotifyPropertyChanged
VB __Копировать
     Public Interface ITessaShellPanel
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class ITessaShellPanel : INotifyPropertyChanged
F# __Копировать
     type ITessaShellPanel = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[IsOpened](P_Tessa_UI_Windows_ITessaShellPanel_IsOpened.htm)| Признак того,
что боковая панель открыта.  
---|---  
##  __Методы
[Close](M_Tessa_UI_Windows_ITessaShellPanel_Close.htm)| Закрывает боковую
панель, если она открыта.  
---|---  
[Open](M_Tessa_UI_Windows_ITessaShellPanel_Open.htm)|  Открывает боковую
панель, которая автоматически закрывается по прошествии заданной задержки.
Если боковая панель уже открыта, то не выполняет действий.  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
