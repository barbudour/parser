# FileSourceForCard.CanUploadFileCoreAsync - метод
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<ValidationResult> CanUploadFileCoreAsync(
    	string filePath,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function CanUploadFileCoreAsync ( 
    	filePath As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     protected:
    virtual ValueTask<ValidationResult^> CanUploadFileCoreAsync(
    	String^ filePath, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CanUploadFileCoreAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
    override CanUploadFileCoreAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
     Полный путь к проверяемому файлу. Не должен быть равен null или пустой строке. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Объект, содержащий сообщения при проверке файла на возможность загрузки в
систему. Если возвращённый объект содержит ошибки, то загрузка запрещена.
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
