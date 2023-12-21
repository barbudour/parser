# CardDatabaseContentStrategy.GetSizeAsync - метод
Возвращает длину контента версии файла в байтах.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<long> GetSizeAsync(
    	CardContentContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetSizeAsync ( 
    	context As CardContentContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Long)
C++ __Копировать
     public:
    virtual ValueTask<long long> GetSizeAsync(
    	CardContentContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetSizeAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<int64> 
    override GetSizeAsync : 
            context : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<int64> 
#### Параметры
context
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Контекст, описывающий контент версии файла, размер которого требуется получить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>  
Размер контента версии файла в байтах.
#### Реализации
[ICardContentStrategy.GetSizeAsync(CardContentContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_GetSizeAsync.htm)  
##  __См. также
#### Ссылки
[CardDatabaseContentStrategy -
](T_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
