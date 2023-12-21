# CardTableViewControlViewModel.DeleteRowsAsync - метод
Удаляет заданные строки с учётом визуальных изменений в контроле. При этом
выполняются обработчики события
[RowInvoked](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInvoked.htm),
которые могут запретить удаление некоторых строк или вывести на экран окна с
ошибками. Укажите
[SelectedRows](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedRows.htm),
чтобы удалить выбранные строки (аналогично соответствующей кнопке в контроле).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteRowsAsync(
    	IList<TableRowViewModel> selectedRows,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteRowsAsync ( 
    	selectedRows As IList(Of TableRowViewModel),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ DeleteRowsAsync(
    	IList<TableRowViewModel^>^ selectedRows, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member DeleteRowsAsync : 
            selectedRows : IList<TableRowViewModel> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
selectedRows
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[TableRowViewModel](T_Tessa_UI_Views_Content_TableRowViewModel.htm)>
     Удаляемые строки, не должны быть равны null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
