# TableViewRowEventArgs - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public TableViewRowEventArgs(
    	GridRowAction action,
    	CardTableViewControlViewModel control,
    	CardRow row,
    	ICardModel rowModel,
    	ViewControlRowViewModel rowViewModel,
    	ICardModel cardModel,
    	TableCellViewModel cell = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	action As GridRowAction,
    	control As CardTableViewControlViewModel,
    	row As CardRow,
    	rowModel As ICardModel,
    	rowViewModel As ViewControlRowViewModel,
    	cardModel As ICardModel,
    	Optional cell As TableCellViewModel = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    TableViewRowEventArgs(
    	GridRowAction action, 
    	CardTableViewControlViewModel^ control, 
    	CardRow^ row, 
    	ICardModel^ rowModel, 
    	ViewControlRowViewModel^ rowViewModel, 
    	ICardModel^ cardModel, 
    	TableCellViewModel^ cell = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            action : GridRowAction * 
            control : CardTableViewControlViewModel * 
            row : CardRow * 
            rowModel : ICardModel * 
            rowViewModel : ViewControlRowViewModel * 
            cardModel : ICardModel * 
            ?cell : TableCellViewModel * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cell = defaultArg cell null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> TableViewRowEventArgs
#### Параметры
action [GridRowAction](T_Tessa_UI_Cards_Controls_GridRowAction.htm)
    Действие со строкой row.
control
[CardTableViewControlViewModel](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
    Контрол, в рамках которого выполняется событие.
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка карточки, с которой производится действие.
rowModel [ICardModel](T_Tessa_UI_Cards_ICardModel.htm)
     Модель строки row вместе с формой, которая только что была инициализирована, или null, если выполняется удаление строки, при этом модель не требуется. 
rowViewModel
[ViewControlRowViewModel](T_Tessa_UI_Views_Content_ViewControlRowViewModel.htm)
    Модель представления для строки таблицы.
cardModel [ICardModel](T_Tessa_UI_Cards_ICardModel.htm)
    Модель карточки, в которой расположена строка row.
cell [TableCellViewModel](T_Tessa_UI_Views_Content_TableCellViewModel.htm)
(Optional)
     Объект, описывающий ячейку, по которой был выполнен клик, или null, если клик был по строке снаружи ячеек или производится добавление/удаление строки без привязки к ячейке. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
Объект, посредством которого можно отменить асинхронную задачу.
## __См. также
#### Ссылки
[TableViewRowEventArgs -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
