# ICardActionDescriptionBuilder.AppendHeaderAsync(StringBuilder,
WorkplaceStoreRequest, CancellationToken) - метод
Добавляет описание заголовка для запроса на сохранение рабочих мест.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<StringBuilder> AppendHeaderAsync(
    	StringBuilder builder,
    	WorkplaceStoreRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function AppendHeaderAsync ( 
    	builder As StringBuilder,
    	request As WorkplaceStoreRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringBuilder)
C++ __Копировать
     ValueTask<StringBuilder^> AppendHeaderAsync(
    	StringBuilder^ builder, 
    	WorkplaceStoreRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract AppendHeaderAsync : 
            builder : StringBuilder * 
            request : WorkplaceStoreRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
#### Параметры
builder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Объект, содержащий текстовое описание информации о действии.
request
[WorkplaceStoreRequest](T_Tessa_Platform_Configuration_WorkplaceStoreRequest.htm)
    Запрос на сохранение рабочих мест.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)>  
Объект builder для цепочки вызовов.
## __См. также
#### Ссылки
[ICardActionDescriptionBuilder -
](T_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder.htm)
[AppendHeaderAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder_AppendHeaderAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
