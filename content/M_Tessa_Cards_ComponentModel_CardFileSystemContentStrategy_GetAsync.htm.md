# CardFileSystemContentStrategy.GetAsync - метод
Загружает контент версии файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<Stream> GetAsync(
    	CardContentContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync ( 
    	context As CardContentContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     public:
    virtual ValueTask<Stream^> GetAsync(
    	CardContentContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
    override GetAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
#### Параметры
context
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Контекст, описывающий загружаемый контент версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток, содержащий контент версии файла.
#### Реализации
[ICardContentStrategy.GetAsync(CardContentContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_GetAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSystemContentStrategy -
](T_Tessa_Cards_ComponentModel_CardFileSystemContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
