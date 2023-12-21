# IWorkspaceModel - интерфейс
Модель представления для рабочей области, которую можно закрыть.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkspaceModel : INotifyPropertyChanged
VB __Копировать
     Public Interface IWorkspaceModel
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IWorkspaceModel : INotifyPropertyChanged
F# __Копировать
     type IWorkspaceModel = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[CloseCommand](P_Tessa_UI_IWorkspaceModel_CloseCommand.htm)| Команда закрытия
рабочей области.  
---|---  
[IsClosed](P_Tessa_UI_IWorkspaceModel_IsClosed.htm)| Признак того, что рабочая
область была закрыта.  
##  __Методы
[CloseAsync](M_Tessa_UI_IWorkspaceModel_CloseAsync.htm)|  Асинхронно закрывает
рабочую область. Возвращает false, если закрытие области было отменено, причём
значение будет возвращено синхронно. Используйте код следующего вида в
обработчике события window.Closing: async (s, e) => { var task =
model.CloseAsync(); e.Cancel = task.IsCompleted && !task.Result; await task; }  
---|---  
[SetIsClosedAsync](M_Tessa_UI_IWorkspaceModel_SetIsClosedAsync.htm)|
Устанавливает признак того, что рабочая область была закрыта.  
##  __События
[Closed](E_Tessa_UI_IWorkspaceModel_Closed.htm)| Происходит при закрытии
рабочей области.  
---|---  
[Closing](E_Tessa_UI_IWorkspaceModel_Closing.htm)| Происходит перед закрытием
рабочей области.  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
