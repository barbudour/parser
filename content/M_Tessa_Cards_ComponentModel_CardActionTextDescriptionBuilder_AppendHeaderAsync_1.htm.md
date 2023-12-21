# CardActionTextDescriptionBuilder.AppendHeaderAsync(StringBuilder,
CardGetFileContentRequest, CancellationToken) - метод
Добавляет описание заголовка для запроса на загрузку контента файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<StringBuilder> AppendHeaderAsync(
    	StringBuilder builder,
    	CardGetFileContentRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AppendHeaderAsync ( 
    	builder As StringBuilder,
    	request As CardGetFileContentRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringBuilder)
C++ __Копировать
     public:
    virtual ValueTask<StringBuilder^> AppendHeaderAsync(
    	StringBuilder^ builder, 
    	CardGetFileContentRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract AppendHeaderAsync : 
            builder : StringBuilder * 
            request : CardGetFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
    override AppendHeaderAsync : 
            builder : StringBuilder * 
            request : CardGetFileContentRequest * 
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
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
     Запрос на загрузку контента файла, который соответствует действию [Tessa.Cards.CardActionType.GetFile]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)>  
Объект builder для цепочки вызовов.
#### Реализации
[ICardActionDescriptionBuilder.AppendHeaderAsync(StringBuilder,
CardGetFileContentRequest,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder_AppendHeaderAsync_1.htm)  
##  __См. также
#### Ссылки
[CardActionTextDescriptionBuilder -
](T_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder.htm)
[AppendHeaderAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder_AppendHeaderAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
