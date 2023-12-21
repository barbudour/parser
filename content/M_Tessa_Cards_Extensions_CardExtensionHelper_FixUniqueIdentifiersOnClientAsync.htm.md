# CardExtensionHelper.FixUniqueIdentifiersOnClientAsync - метод
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях identifierFieldName в коллекционной секции с именем sectionName. Под
уникальностью ссылки подразумевается, что в одну и ту же карточку не может
быть добавлено более одной ссылки с одним и тем же идентификатором. Метод
следует вызывать в расширении на сохранение карточки, файла или задания,
передаваемого в поле card.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask FixUniqueIdentifiersOnClientAsync(
    	Card card,
    	string sectionName,
    	string identifierFieldName,
    	string parentRowIDFieldName = null,
    	string orderFieldName = null,
    	Func<IList<CardRow>, CardRow, CancellationToken, ValueTask> removeRowFuncAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function FixUniqueIdentifiersOnClientAsync ( 
    	card As Card,
    	sectionName As String,
    	identifierFieldName As String,
    	Optional parentRowIDFieldName As String = Nothing,
    	Optional orderFieldName As String = Nothing,
    	Optional removeRowFuncAsync As Func(Of IList(Of CardRow), CardRow, CancellationToken, ValueTask) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    static ValueTask FixUniqueIdentifiersOnClientAsync(
    	Card^ card, 
    	String^ sectionName, 
    	String^ identifierFieldName, 
    	String^ parentRowIDFieldName = nullptr, 
    	String^ orderFieldName = nullptr, 
    	Func<IList<CardRow^>^, CardRow^, CancellationToken, ValueTask>^ removeRowFuncAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member FixUniqueIdentifiersOnClientAsync : 
            card : Card * 
            sectionName : string * 
            identifierFieldName : string * 
            ?parentRowIDFieldName : string * 
            ?orderFieldName : string * 
            ?removeRowFuncAsync : Func<IList<CardRow>, CardRow, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parentRowIDFieldName = defaultArg parentRowIDFieldName null
            let _orderFieldName = defaultArg orderFieldName null
            let _removeRowFuncAsync = defaultArg removeRowFuncAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Сохраняемая карточка. Может быть обычной карточкой, файлов или заданием.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя коллекционной секции, которая содержит список идентификаторов.
identifierFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля в секции sectionName, которое содержит идентификатор любого типа, уникальность которого требуется обеспечить в пределах карточки. 
parentRowIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Имя поля в секции sectionName, которое содержит идентификатор родительской строки, уникальность которого требуется обеспечить в пределах карточки, или null, если секция sectionName не является дочерней. 
orderFieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя поля для сортировки в строках карточки или null, если поле не задано. 
removeRowFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardRow](T_Tessa_Cards_CardRow.htm)>,
[CardRow](T_Tessa_Cards_CardRow.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Функция, выполняющая удаление указанной строки из коллекции строк, или null, если строка удаляется обычным образом. Переопределять удаление имеет смысл на клиенте, где также требуется удалить дочерние строки из структуры карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Заметки
Метод гарантирует, что если пользователь удалит и тут же добавит строку с
таким же идентификатором в поле identifierFieldName, то удалённая не будет
удалена, а новая строка не будет добавлена.
Рекомендуется использовать метод в случае, если в секции sectionName есть
уникальный индекс на идентификатор карточки и идентификатор в поле
identifierFieldName.
##  __См. также
#### Ссылки
[CardExtensionHelper - ](T_Tessa_Cards_Extensions_CardExtensionHelper.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
