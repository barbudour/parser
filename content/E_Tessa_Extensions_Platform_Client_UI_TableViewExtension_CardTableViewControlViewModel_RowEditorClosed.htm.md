# CardTableViewControlViewModel.RowEditorClosed - событие
Событие, происходящее при закрытии редактора для строки таблицы, который может
быть открыт при создании строки или при открытии существующей строки. Событие
вызывается как при закрытии с сохранением строки, так и при отмене. Обработчик
события обычно удаляет подписки, добавленные в
[RowInitializing](E_Tessa_UI_Cards_Controls_GridViewModel_RowInitializing.htm).
Через аргументы этого события нельзя отменить закрытие строки, для этого
используйте событие
[RowEditorClosing](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowEditorClosing.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<TableViewRowEventArgs> RowEditorClosed
VB __Копировать
     Public Event RowEditorClosed As EventHandler(Of TableViewRowEventArgs)
C++ __Копировать
     public:
     event EventHandler<TableViewRowEventArgs^>^ RowEditorClosed {
    	void add (EventHandler<TableViewRowEventArgs^>^ value);
    	void remove (EventHandler<TableViewRowEventArgs^>^ value);
    }
F# __Копировать
     member RowEditorClosed : IEvent<EventHandler<TableViewRowEventArgs>,
        TableViewRowEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[TableViewRowEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
