# CardExtensions.TrySetFieldIgnoreCaseAsync - метод
Устанавливает значение поля строковой секции или строки коллекционной секции
карточки без учёта регистра. Возвращает признак того, что значение было
установлено, т.к. было определено имя поля с учётом регистра.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> TrySetFieldIgnoreCaseAsync(
    	this ICardFieldContainer fieldContainer,
    	string fieldName,
    	Object fieldValue,
    	string sectionName = null,
    	ICardMetadata cardMetadata = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TrySetFieldIgnoreCaseAsync ( 
    	fieldContainer As ICardFieldContainer,
    	fieldName As String,
    	fieldValue As Object,
    	Optional sectionName As String = Nothing,
    	Optional cardMetadata As ICardMetadata = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<bool> TrySetFieldIgnoreCaseAsync(
    	ICardFieldContainer^ fieldContainer, 
    	String^ fieldName, 
    	Object^ fieldValue, 
    	String^ sectionName = nullptr, 
    	ICardMetadata^ cardMetadata = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TrySetFieldIgnoreCaseAsync : 
            fieldContainer : ICardFieldContainer * 
            fieldName : string * 
            fieldValue : Object * 
            ?sectionName : string * 
            ?cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _sectionName = defaultArg sectionName null
            let _cardMetadata = defaultArg cardMetadata null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
fieldContainer [ICardFieldContainer](T_Tessa_Cards_ICardFieldContainer.htm)
    Строковая секция или строка коллекционной секции карточки.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя возвращаемого поля без учёта регистра.
fieldValue [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Значение устанавливаемого поля. Может быть равно null.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя секции карточки без учёта регистра или null, если метаинформация cardMetadata не будет использоваться. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm) (Optional)
     Метаинформация по типу карточки или общая метаинформация, которые используются для корректировки регистра в именах поля и секции. Также можно указать null, если корректировка регистра будет возможна только по данным, содержащимся в объекте карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если значение было установлено, т.к. было определено имя поля с учётом
регистра; false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardFieldContainer](T_Tessa_Cards_ICardFieldContainer.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
