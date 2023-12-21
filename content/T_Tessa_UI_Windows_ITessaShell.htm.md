# ITessaShell - интерфейс
Основное окно приложения.
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaShell : INotifyPropertyChanged
VB __Копировать
     Public Interface ITessaShell
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class ITessaShell : INotifyPropertyChanged
F# __Копировать
     type ITessaShell = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[SelectedTab](P_Tessa_UI_Windows_ITessaShell_SelectedTab.htm)|  Вкладка из
списка [Tessa.UI.Windows.ITessaShell.SelectedTab], активная в настоящий
момент, или null, если активная вкладка отсутствует (обычно в случае, когда
вкладок нет).  
---|---  
[Settings](P_Tessa_UI_Windows_ITessaShell_Settings.htm)|  Последние настройки
приложения, которые были применены, или null, если настройки ещё не были
применены.  
[Tabs](P_Tessa_UI_Windows_ITessaShell_Tabs.htm)| Вкладки приложения, открытые
в настоящий момент.  
[TargetProxyFuncAsync](P_Tessa_UI_Windows_ITessaShell_TargetProxyFuncAsync.htm)|
Асинхронная функция, возвращающая объект, для которого применяются настройки
боковых панелей помимо текущего объекта, или null, если такой объект не задан
(при этом возвращаемая асинхронная задача не равна null). Параметром принимает
объект, посредством которого можно отменить асинхронную задачу.  
## __Методы
[ApplySettingsAsync](M_Tessa_UI_Windows_ITessaShell_ApplySettingsAsync.htm)|
Применяет заданные настройки приложения.  
---|---  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
[SettingsApplied](E_Tessa_UI_Windows_ITessaShell_SettingsApplied.htm)|
Событие, возникающее после применения настроек.  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
