# CardHelper.GetFileCardTypesAsync - метод
Получение типов файлов, доступных из API карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<IEnumerable<CardType>> GetFileCardTypesAsync(
    	ICardMetadata cardMetadata,
    	bool isAdministrator,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetFileCardTypesAsync ( 
    	cardMetadata As ICardMetadata,
    	isAdministrator As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of CardType))
C++ __Копировать
     public:
    static ValueTask<IEnumerable<CardType^>^> GetFileCardTypesAsync(
    	ICardMetadata^ cardMetadata, 
    	bool isAdministrator, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetFileCardTypesAsync : 
            cardMetadata : ICardMetadata * 
            isAdministrator : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<CardType>> 
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация о типах карточек.
isAdministrator
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак работы из-под администратора.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardType](T_Tessa_Cards_CardType.htm)>>  
Типы файлов, доступные из API карточек.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
