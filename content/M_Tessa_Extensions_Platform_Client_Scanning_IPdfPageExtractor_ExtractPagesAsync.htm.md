# IPdfPageExtractor.ExtractPagesAsync - метод
Выполняет извлечение страниц PDF с изображениями PNG.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     Task ExtractPagesAsync(
    	IPdfPageExtractorContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ExtractPagesAsync ( 
    	context As IPdfPageExtractorContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ ExtractPagesAsync(
    	IPdfPageExtractorContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ExtractPagesAsync : 
            context : IPdfPageExtractorContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IPdfPageExtractorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext.htm)
    Контекст операции по разбору файла PDF на страницы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IPdfPageExtractor -
](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractor.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
