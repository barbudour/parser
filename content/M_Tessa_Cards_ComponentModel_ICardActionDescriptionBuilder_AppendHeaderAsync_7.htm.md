# ICardActionDescriptionBuilder.AppendHeaderAsync(StringBuilder,
ViewStoreRequest, CancellationToken) - метод
Добавляет описание заголовка для запроса на сохранение представлений.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<StringBuilder> AppendHeaderAsync(
    	StringBuilder builder,
    	ViewStoreRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function AppendHeaderAsync ( 
    	builder As StringBuilder,
    	request As ViewStoreRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringBuilder)
C++ __Копировать
     ValueTask<StringBuilder^> AppendHeaderAsync(
    	StringBuilder^ builder, 
    	ViewStoreRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract AppendHeaderAsync : 
            builder : StringBuilder * 
            request : ViewStoreRequest * 
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
[ViewStoreRequest](T_Tessa_Platform_Configuration_ViewStoreRequest.htm)
    Запрос на сохранение представлений.
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
