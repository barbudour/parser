# CardTableViewControlViewModel.RowAdding - событие
Событие, возникающее перед вставкой новой строки в таблицу.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<TableViewRowAddingEventArgs> RowAdding
VB __Копировать
     Public Event RowAdding As EventHandler(Of TableViewRowAddingEventArgs)
C++ __Копировать
     public:
     event EventHandler<TableViewRowAddingEventArgs^>^ RowAdding {
    	void add (EventHandler<TableViewRowAddingEventArgs^>^ value);
    	void remove (EventHandler<TableViewRowAddingEventArgs^>^ value);
    }
F# __Копировать
     member RowAdding : IEvent<EventHandler<TableViewRowAddingEventArgs>,
        TableViewRowAddingEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[TableViewRowAddingEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowAddingEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
