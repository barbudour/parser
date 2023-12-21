# CardExtensionHelper.FixUniqueIdentifiersAsync - метод
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях из списка identifierFieldNames в списке полей rows. Под уникальностью
ссылки подразумевается, что в одну и ту же карточку не может быть добавлено
более одной ссылки с одним и тем же идентификатором. Возвращает признак того,
что была найдена хотя бы одна строка-дубликат. Если задано removeDuplicates
как false, то дубликаты не удаляются.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> FixUniqueIdentifiersAsync(
    	ListStorage<CardRow> rows,
    	string[] identifierFieldNames,
    	string parentIdentifierFieldName = null,
    	string orderFieldName = null,
    	bool removeDuplicates = true,
    	Func<IList<CardRow>, CardRow, CancellationToken, ValueTask> removeRowFuncAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function FixUniqueIdentifiersAsync ( 
    	rows As ListStorage(Of CardRow),
    	identifierFieldNames As String(),
    	Optional parentIdentifierFieldName As String = Nothing,
    	Optional orderFieldName As String = Nothing,
    	Optional removeDuplicates As Boolean = true,
    	Optional removeRowFuncAsync As Func(Of IList(Of CardRow), CardRow, CancellationToken, ValueTask) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> FixUniqueIdentifiersAsync(
    	ListStorage<CardRow^>^ rows, 
    	array<String^>^ identifierFieldNames, 
    	String^ parentIdentifierFieldName = nullptr, 
    	String^ orderFieldName = nullptr, 
    	bool removeDuplicates = true, 
    	Func<IList<CardRow^>^, CardRow^, CancellationToken, ValueTask>^ removeRowFuncAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member FixUniqueIdentifiersAsync : 
            rows : ListStorage<CardRow> * 
            identifierFieldNames : string[] * 
            ?parentIdentifierFieldName : string * 
            ?orderFieldName : string * 
            ?removeDuplicates : bool * 
            ?removeRowFuncAsync : Func<IList<CardRow>, CardRow, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parentIdentifierFieldName = defaultArg parentIdentifierFieldName null
            let _orderFieldName = defaultArg orderFieldName null
            let _removeDuplicates = defaultArg removeDuplicates true
            let _removeRowFuncAsync = defaultArg removeRowFuncAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
rows
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Список строк. Может быть обычной карточкой, файлов или заданием.
identifierFieldNames
[String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список имён полей в строках rows, которые содержат идентификаторы любого типа, уникальность которых требуется обеспечить в пределах списка строк, в т.ч. родительские идентификаторы. 
parentIdentifierFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Имя поля в строках rows, которое содержит идентификатор для связи с родительской строкой (ParentRowID), у которых обычно указан флажок "Is reference to owner". Эти идентификаторы позволяют найти строки в пределах одной родительской строки при удалении дубликатов. Может быть указан null или пустая строка, если строки rows не принадлежат дочерней секции. 
orderFieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя поля для сортировки в строках rows или null, если поле не задано. 
removeDuplicates
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что строки-дубликаты должны быть удалены. Используйте false, чтобы найти строки, но не удалять их. 
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
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если была найдена хотя бы одна строка-дубликат; false в противном
случае.
## __Заметки
Метод гарантирует, что если пользователь удалит и тут же добавит строку с
таким же идентификатором, то удалённая не будет удалена, а новая строка не
будет добавлена.
Рекомендуется использовать метод в случае, если в секции есть необходимые
уникальные индексы.
##  __См. также
#### Ссылки
[CardExtensionHelper - ](T_Tessa_Cards_Extensions_CardExtensionHelper.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
