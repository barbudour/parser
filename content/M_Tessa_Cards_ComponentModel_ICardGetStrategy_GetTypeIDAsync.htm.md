# ICardGetStrategy.GetTypeIDAsync - метод
Возвращает идентификатор типа карточки, файла или задания по идентификатору
экземпляра или null, если карточка, файл или задание не найдены.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<Guid?> GetTypeIDAsync(
    	Guid instanceID,
    	CardInstanceType instanceType = CardInstanceType.Card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetTypeIDAsync ( 
    	instanceID As Guid,
    	Optional instanceType As CardInstanceType = CardInstanceType.Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
    Task<Nullable<Guid>>^ GetTypeIDAsync(
    	Guid instanceID, 
    	CardInstanceType instanceType = CardInstanceType::Card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetTypeIDAsync : 
            instanceID : Guid * 
            ?instanceType : CardInstanceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
instanceID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор экземпляра карточки, файла или задания.
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm) (Optional)
    Тип экземпляра: карточка, файл или задание.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор типа карточка, файла или задания или null, если карточка, файл
или задание не найдены.
## __См. также
#### Ссылки
[ICardGetStrategy - ](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
