# CardTableViewControlViewModel.RowValidating - событие
Событие, происходящее при валидации строки перед сохранением или закрытием её
окна редактирования. Если хотя бы один обработчик выбросит исключение, то оно
будет считаться ошибкой валидации.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<GridRowValidationEventArgs> RowValidating
VB __Копировать
     Public Event RowValidating As EventHandler(Of GridRowValidationEventArgs)
C++ __Копировать
     public:
     event EventHandler<GridRowValidationEventArgs^>^ RowValidating {
    	void add (EventHandler<GridRowValidationEventArgs^>^ value);
    	void remove (EventHandler<GridRowValidationEventArgs^>^ value);
    }
F# __Копировать
     member RowValidating : IEvent<EventHandler<GridRowValidationEventArgs>,
        GridRowValidationEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[GridRowValidationEventArgs](T_Tessa_UI_Cards_Controls_GridRowValidationEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
