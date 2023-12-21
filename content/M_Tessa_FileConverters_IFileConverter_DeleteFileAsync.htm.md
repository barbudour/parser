# IFileConverter.DeleteFileAsync - метод
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<(ValidationResult result, bool fileExisted)> DeleteFileAsync(
    	IFileConverterRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function DeleteFileAsync ( 
    	request As IFileConverterRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As ValidationResult, fileExisted As Boolean))
C++ __Копировать
    Task<ValueTuple<ValidationResult^, bool>>^ DeleteFileAsync(
    	IFileConverterRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract DeleteFileAsync : 
            request : IFileConverterRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, bool>> 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос, на основании которого выполнялась конвертация файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
Результат удаления с сообщениями об ошибках и предупреждениями, а также
признак того, был ли файл в кэше на момент вызова метода.
## __См. также
#### Ссылки
[IFileConverter - ](T_Tessa_FileConverters_IFileConverter.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
