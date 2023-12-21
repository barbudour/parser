# CardTableViewControlViewModel.RowEditorClosing - событие
Событие, происходящее при закрытии редактора для строки таблицы, который может
быть открыт при создании строки или при открытии существующей строки. При
создании строки событие вызывается только при сохранении строки (но не при
отмене), причём проверка строки валидаторами вызываются после срабатывания
события. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) установлено равным true, то закрытие не
будет выполнено.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<TableViewRowEventArgs> RowEditorClosing
VB __Копировать
     Public Event RowEditorClosing As EventHandler(Of TableViewRowEventArgs)
C++ __Копировать
     public:
     event EventHandler<TableViewRowEventArgs^>^ RowEditorClosing {
    	void add (EventHandler<TableViewRowEventArgs^>^ value);
    	void remove (EventHandler<TableViewRowEventArgs^>^ value);
    }
F# __Копировать
     member RowEditorClosing : IEvent<EventHandler<TableViewRowEventArgs>,
        TableViewRowEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[TableViewRowEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
