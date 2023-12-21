# CardTableViewControlViewModel.RowChanged - событие
Событие, возникающее при изменении строки секции, от которой зависят строки
таблицы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<TableViewRowChangedEventArgs> RowChanged
VB __Копировать
     Public Event RowChanged As EventHandler(Of TableViewRowChangedEventArgs)
C++ __Копировать
     public:
     event EventHandler<TableViewRowChangedEventArgs^>^ RowChanged {
    	void add (EventHandler<TableViewRowChangedEventArgs^>^ value);
    	void remove (EventHandler<TableViewRowChangedEventArgs^>^ value);
    }
F# __Копировать
     member RowChanged : IEvent<EventHandler<TableViewRowChangedEventArgs>,
        TableViewRowChangedEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[TableViewRowChangedEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
