# CardExtensions.GetTypeIDListAsync - метод
Асинхронно возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификаторов типов карточек по заданным идентификаторам карточек. Элементы
результирующего массива со значениями null возвращаются в случае, если
идентификатор типа не был определён.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?[]> GetTypeIDListAsync(
    	this ICardRepository cardRepository,
    	ICollection<Guid> instanceIDs,
    	CardInstanceType instanceType = CardInstanceType.Card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTypeIDListAsync ( 
    	cardRepository As ICardRepository,
    	instanceIDs As ICollection(Of Guid),
    	Optional instanceType As CardInstanceType = CardInstanceType.Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?())
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<array<Nullable<Guid>>^>^ GetTypeIDListAsync(
    	ICardRepository^ cardRepository, 
    	ICollection<Guid>^ instanceIDs, 
    	CardInstanceType instanceType = CardInstanceType::Card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTypeIDListAsync : 
            cardRepository : ICardRepository * 
            instanceIDs : ICollection<Guid> * 
            ?instanceType : CardInstanceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>[]> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
instanceIDs
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификаторы карточек, для которых требуется получить идентификаторы типов. Значение null трактуется как пустой массив. 
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm) (Optional)
    Тип экземпляров карточек, заданных в параметре instanceIDs.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>[]>  
Задача, возвращающая результат выполнения запроса на получение идентификаторов
типов карточек по заданным идентификаторам карточек. Результат гарантированно
не равен null. Порядок идентификаторов типов совпадает с порядком
идентификаторов карточек, заданном в параметре instanceIDs.
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
