# CardTableViewControlViewModel.RowInitializing - событие
Событие, происходящее при инициализации окна для строки таблицы, а именно при
создании строки или при открытии существующей строки. Событие вызывается
непосредственно перед тем, как окно будет открыто. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) установлено равным true, то открытие
окна будет отменено.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<TableViewRowEventArgs> RowInitializing
VB __Копировать
     Public Event RowInitializing As EventHandler(Of TableViewRowEventArgs)
C++ __Копировать
     public:
     event EventHandler<TableViewRowEventArgs^>^ RowInitializing {
    	void add (EventHandler<TableViewRowEventArgs^>^ value);
    	void remove (EventHandler<TableViewRowEventArgs^>^ value);
    }
F# __Копировать
     member RowInitializing : IEvent<EventHandler<TableViewRowEventArgs>,
        TableViewRowEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[TableViewRowEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
