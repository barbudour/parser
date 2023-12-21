# CardExtensions.GetTypeIDAsync - метод
Асинхронно возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификатора типа карточки по заданному идентификатору карточки. Значение
null возвращается в случае, если идентификатор типа не был определён.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> GetTypeIDAsync(
    	this ICardRepository cardRepository,
    	Guid instanceID,
    	CardInstanceType instanceType = CardInstanceType.Card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTypeIDAsync ( 
    	cardRepository As ICardRepository,
    	instanceID As Guid,
    	Optional instanceType As CardInstanceType = CardInstanceType.Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<Nullable<Guid>>^ GetTypeIDAsync(
    	ICardRepository^ cardRepository, 
    	Guid instanceID, 
    	CardInstanceType instanceType = CardInstanceType::Card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTypeIDAsync : 
            cardRepository : ICardRepository * 
            instanceID : Guid * 
            ?instanceType : CardInstanceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
instanceID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки, для которого требуется получить идентификатор типа. 
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm) (Optional)
    Тип экземпляра карточки, заданного в параметре instanceID.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Задача, возвращающая результат выполнения запроса на получение идентификатора
типа карточки по заданному идентификатору карточки.
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
