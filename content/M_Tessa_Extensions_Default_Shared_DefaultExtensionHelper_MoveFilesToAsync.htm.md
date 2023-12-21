# DefaultExtensionHelper.MoveFilesToAsync - метод
Переносит все файлы или заданный файл fileID для карточки cardID на
местоположение контента файлов sourceType. Перенос файла включает перенос всех
его версий. Если версия уже располагалась в заданном местоположении, то
действий не производится. Метод корректно выполняется только в том случае,
если пользователь является администратором. Возвращает результат выполнения
метода, в котором, как правило, содержатся ошибки в случае неудачного
выполнения. Возвращаемый объект никогда не равен null.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> MoveFilesToAsync(
    	CardFileSourceType sourceType,
    	ICardRepository extendedRepository,
    	Guid cardID,
    	Guid? fileID = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function MoveFilesToAsync ( 
    	sourceType As CardFileSourceType,
    	extendedRepository As ICardRepository,
    	cardID As Guid,
    	Optional fileID As Guid? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    static Task<ValidationResult^>^ MoveFilesToAsync(
    	CardFileSourceType sourceType, 
    	ICardRepository^ extendedRepository, 
    	Guid cardID, 
    	Nullable<Guid> fileID = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member MoveFilesToAsync : 
            sourceType : CardFileSourceType * 
            extendedRepository : ICardRepository * 
            cardID : Guid * 
            ?fileID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _fileID = defaultArg fileID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
sourceType [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Местоположение контента файлов, на которое требуется перенести файлы.
extendedRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточки с расширениями.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, файл или файлы которой должны быть перенесены.
fileID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
    Идентификатор файла, который переносится, или null, если переносятся все файлы карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат выполнения метода. Не равен null.
##  __См. также
#### Ссылки
[DefaultExtensionHelper -
](T_Tessa_Extensions_Default_Shared_DefaultExtensionHelper.htm)
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
