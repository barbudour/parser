# CardDatabaseContentStrategy.StoreAsync - метод
Сохраняет контент версии файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreAsync(
    	CardContentContext context,
    	Stream contentStream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	context As CardContentContext,
    	contentStream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreAsync(
    	CardContentContext^ context, 
    	Stream^ contentStream, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            context : CardContentContext * 
            contentStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override StoreAsync : 
            context : CardContentContext * 
            contentStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Контекст, описывающий сохраняемый контент версии файла.
contentStream
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток, содержащий данные сохраняемого контента версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardContentStrategy.StoreAsync(CardContentContext, Stream,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardDatabaseContentStrategy -
](T_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
