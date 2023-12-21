# CardFileContentResult - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentResult(
    	CardGetFileContentResponse response,
    	Func<CancellationToken, ValueTask<Stream>> getContentFuncAsync = null
    )
VB __Копировать
     Public Sub New ( 
    	response As CardGetFileContentResponse,
    	Optional getContentFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream)) = Nothing
    )
C++ __Копировать
     public:
    CardFileContentResult(
    	CardGetFileContentResponse^ response, 
    	Func<CancellationToken, ValueTask<Stream^>>^ getContentFuncAsync = nullptr
    )
F# __Копировать
     new : 
            response : CardGetFileContentResponse * 
            ?getContentFuncAsync : Func<CancellationToken, ValueTask<Stream>> 
    (* Defaults:
            let _getContentFuncAsync = defaultArg getContentFuncAsync null
    *)
    -> CardFileContentResult
#### Параметры
response
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)
    Ответ на запрос на получение контента. Не может быть равен null.
getContentFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
(Optional)
     Функция, возвращающая поток с данными контента. Может быть равна null, если контент недоступен. 
## __См. также
#### Ссылки
[CardFileContentResult - ](T_Tessa_Cards_CardFileContentResult.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
