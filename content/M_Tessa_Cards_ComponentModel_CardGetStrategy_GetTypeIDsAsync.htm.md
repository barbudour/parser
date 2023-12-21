# CardGetStrategy.GetTypeIDsAsync - метод
Возвращает идентификаторы типов карточек, файлов или заданий по
идентификаторам экземпляров. Порядок возвращённых идентификаторов типов
соответствует порядку переданных экземпляров instanceIDs. Возвращённый
идентификатор типа равен null, если карточка, файл или задание с
соответствующим идентификатором экземпляра не найдены.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IList<Guid?>> GetTypeIDsAsync(
    	Guid[] instanceIDs,
    	CardInstanceType instanceType = CardInstanceType.Card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTypeIDsAsync ( 
    	instanceIDs As Guid(),
    	Optional instanceType As CardInstanceType = CardInstanceType.Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IList(Of Guid?))
C++ __Копировать
     public:
    virtual Task<IList<Nullable<Guid>>^>^ GetTypeIDsAsync(
    	array<Guid>^ instanceIDs, 
    	CardInstanceType instanceType = CardInstanceType::Card, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTypeIDsAsync : 
            instanceIDs : Guid[] * 
            ?instanceType : CardInstanceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<Nullable<Guid>>> 
    override GetTypeIDsAsync : 
            instanceIDs : Guid[] * 
            ?instanceType : CardInstanceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _instanceType = defaultArg instanceType CardInstanceType.Card
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<Nullable<Guid>>> 
#### Параметры
instanceIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
    Идентификаторы экземпляров карточки, файла или задания.
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm) (Optional)
    Тип экземпляров: карточки, файлы или задания.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>>  
Идентификаторы типов карточек, файлов или заданий.
#### Реализации
[ICardGetStrategy.GetTypeIDsAsync(Guid[], CardInstanceType,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_GetTypeIDsAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
