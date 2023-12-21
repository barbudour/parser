# CardExtensions.GetDigestAsync - метод
Асинхронно возвращает Digest для заданной карточки, полученный выполнением
запроса [GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm), или null,
если Digest неизвестен или не требуется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<string> GetDigestAsync(
    	this ICardRepository cardRepository,
    	Card card,
    	string eventName = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetDigestAsync ( 
    	cardRepository As ICardRepository,
    	card As Card,
    	Optional eventName As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<String^>^ GetDigestAsync(
    	ICardRepository^ cardRepository, 
    	Card^ card, 
    	String^ eventName = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetDigestAsync : 
            cardRepository : ICardRepository * 
            card : Card * 
            ?eventName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _eventName = defaultArg eventName null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить Digest.
eventName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя события по расчёту Digest для сохранения в историю действий с карточкой. Обычно указывается из констант [CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm) для стандартных событий, или любая уникальная строка для других событий. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Задача, возвращающая Digest для заданной карточки или null, если Digest
неизвестен или не требуется.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardRepository](T_Tessa_Cards_ICardRepository.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
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
