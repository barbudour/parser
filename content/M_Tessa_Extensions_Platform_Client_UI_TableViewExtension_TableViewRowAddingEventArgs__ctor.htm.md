# TableViewRowAddingEventArgs - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public TableViewRowAddingEventArgs(
    	CardRow row,
    	IList<CardRow> rows,
    	int rowIndex,
    	CardTableViewControlViewModel control,
    	ICardModel cardModel,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	row As CardRow,
    	rows As IList(Of CardRow),
    	rowIndex As Integer,
    	control As CardTableViewControlViewModel,
    	cardModel As ICardModel,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    TableViewRowAddingEventArgs(
    	CardRow^ row, 
    	IList<CardRow^>^ rows, 
    	int rowIndex, 
    	CardTableViewControlViewModel^ control, 
    	ICardModel^ cardModel, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            row : CardRow * 
            rows : IList<CardRow> * 
            rowIndex : int * 
            control : CardTableViewControlViewModel * 
            cardModel : ICardModel * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> TableViewRowAddingEventArgs
#### Параметры
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка карточки, с которой производится действие.
rows
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Список всех строк в таблице.
rowIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс вставляемого элемента, по умолчанию Rows.Count.
control
[CardTableViewControlViewModel](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
    Контрол, в рамках которого выполняется событие.
cardModel [ICardModel](T_Tessa_UI_Cards_ICardModel.htm)
    Модель карточки, в которой расположена строка row.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[TableViewRowAddingEventArgs -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowAddingEventArgs.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
