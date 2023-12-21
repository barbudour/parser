# IPdfGenerator.TryGenerateAsync - метод
Формирует документ PDF в виде
[ScanDocument](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocument.htm).
Возвращает null, если формирование документа не удалось.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ScanDocument> TryGenerateAsync(
    	IPdfGeneratorContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGenerateAsync ( 
    	context As IPdfGeneratorContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ScanDocument)
C++ __Копировать
    Task<ScanDocument^>^ TryGenerateAsync(
    	IPdfGeneratorContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGenerateAsync : 
            context : IPdfGeneratorContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ScanDocument> 
#### Параметры
context
[IPdfGeneratorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext.htm)
    Контекст операции по разбору файла PDF на страницы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ScanDocument](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocument.htm)>  
Объект, содержащий сформированный документ PDF, или null, если формирование
документа не удалось.
## __См. также
#### Ссылки
[IPdfGenerator -
](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
