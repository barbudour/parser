# ITessaShellControl - интерфейс
Описание интерфейса элемента управления отображаемого перед вкладками
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaShellControl : IAutomationBase, 
    	INotifyPropertyChanged
VB __Копировать
     Public Interface ITessaShellControl
    	Inherits IAutomationBase, INotifyPropertyChanged
C++ __Копировать
     public interface class ITessaShellControl : IAutomationBase, 
    	INotifyPropertyChanged
F# __Копировать
     type ITessaShellControl = 
        interface
            interface IAutomationBase
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAutomationBase](T_Tessa_UI_Automation_IAutomationBase.htm)
##  __Свойства
[AutomationId](P_Tessa_UI_Automation_IAutomationBase_AutomationId.htm)|
Уникальный идентификатор для автоматизации.  
(Унаследован от [IAutomationBase](T_Tessa_UI_Automation_IAutomationBase.htm))  
---|---  
[AutomationName](P_Tessa_UI_Automation_IAutomationBase_AutomationName.htm)|
Имя для автоматизации.  
(Унаследован от [IAutomationBase](T_Tessa_UI_Automation_IAutomationBase.htm))  
[IconGeometry](P_Tessa_UI_Windows_ITessaShellControl_IconGeometry.htm)|  
[IconHeight](P_Tessa_UI_Windows_ITessaShellControl_IconHeight.htm)|  
[IconWidth](P_Tessa_UI_Windows_ITessaShellControl_IconWidth.htm)|  
[Padding](P_Tessa_UI_Windows_ITessaShellControl_Padding.htm)|  
[StrokeThickness](P_Tessa_UI_Windows_ITessaShellControl_StrokeThickness.htm)|  
[ToolTip](P_Tessa_UI_Windows_ITessaShellControl_ToolTip.htm)|  
[Visibility](P_Tessa_UI_Windows_ITessaShellControl_Visibility.htm)|  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
