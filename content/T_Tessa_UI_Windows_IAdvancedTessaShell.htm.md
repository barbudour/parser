# IAdvancedTessaShell - интерфейс
Описание интерфейса основного окна приложения с доп. параметрами.
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAdvancedTessaShell : ITessaShell, 
    	INotifyPropertyChanged
VB __Копировать
     Public Interface IAdvancedTessaShell
    	Inherits ITessaShell, INotifyPropertyChanged
C++ __Копировать
     public interface class IAdvancedTessaShell : ITessaShell, 
    	INotifyPropertyChanged
F# __Копировать
     type IAdvancedTessaShell = 
        interface
            interface ITessaShell
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm)
##  __Свойства
[LeftControls](P_Tessa_UI_Windows_IAdvancedTessaShell_LeftControls.htm)|
Коллекция дополнительных элементов управления слева от списка вкладок.  
---|---  
[LeftPanel](P_Tessa_UI_Windows_IAdvancedTessaShell_LeftPanel.htm)|  Левая
боковая панель.  
[RightControls](P_Tessa_UI_Windows_IAdvancedTessaShell_RightControls.htm)|
Коллекция дополнительных элементов управления справа от списка вкладок.  
[RightPanel](P_Tessa_UI_Windows_IAdvancedTessaShell_RightPanel.htm)|  Правая
боковая панель.  
[SelectedTab](P_Tessa_UI_Windows_ITessaShell_SelectedTab.htm)|  Вкладка из
списка [Tessa.UI.Windows.ITessaShell.SelectedTab], активная в настоящий
момент, или null, если активная вкладка отсутствует (обычно в случае, когда
вкладок нет).  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
[Settings](P_Tessa_UI_Windows_ITessaShell_Settings.htm)|  Последние настройки
приложения, которые были применены, или null, если настройки ещё не были
применены.  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
[Tabs](P_Tessa_UI_Windows_ITessaShell_Tabs.htm)| Вкладки приложения, открытые
в настоящий момент.  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
[TargetProxyFuncAsync](P_Tessa_UI_Windows_ITessaShell_TargetProxyFuncAsync.htm)|
Асинхронная функция, возвращающая объект, для которого применяются настройки
боковых панелей помимо текущего объекта, или null, если такой объект не задан
(при этом возвращаемая асинхронная задача не равна null). Параметром принимает
объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
##  __Методы
[ApplySettingsAsync](M_Tessa_UI_Windows_ITessaShell_ApplySettingsAsync.htm)|
Применяет заданные настройки приложения.  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
---|---  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
[SettingsApplied](E_Tessa_UI_Windows_ITessaShell_SettingsApplied.htm)|
Событие, возникающее после применения настроек.  
(Унаследован от [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
