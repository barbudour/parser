# ApplicationUpdateChecker.CheckAsync(String, Boolean, Assembly,
CancellationToken) - метод
Осуществляет проверку обновления приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> CheckAsync(
    	string applicationAlias,
    	bool client64Bit,
    	Assembly assembly,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CheckAsync ( 
    	applicationAlias As String,
    	client64Bit As Boolean,
    	assembly As Assembly,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ CheckAsync(
    	String^ applicationAlias, 
    	bool client64Bit, 
    	Assembly^ assembly, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CheckAsync : 
            applicationAlias : string * 
            client64Bit : bool * 
            assembly : Assembly * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override CheckAsync : 
            applicationAlias : string * 
            client64Bit : bool * 
            assembly : Assembly * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Псевдоним приложения 
client64Bit [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что приложение является 64-битным.
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
     Папка в которой содержится локальная копия приложения 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат проверки наличия обновления. Если
[IsSuccessful](P_Tessa_Platform_Validation_ValidationResult_IsSuccessful.htm),
то локальная версия приложения соответствует удаленной. Если
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
проверочный ключ
[RemoteApplicationIsNotAvailable](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationIsNotAvailable.htm),
то приложение на сервере не обнаружено. Если
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
проверочный ключ
[RemoteApplicationIsUpdated](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationIsUpdated.htm),
то приложение на сервере имеет более старую версию, чем локальная версия. Если
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
проверочный ключ
[RemoteApplicationRequiresUpdate](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationRequiresUpdate.htm),
то приложение на сервере имеет более новую версию, чем локальная версия.
#### Реализации
[IApplicationUpdateChecker.CheckAsync(String, Boolean, Assembly,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationUpdateChecker_CheckAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationUpdateChecker -
](T_Tessa_Applications_Synchronization_ApplicationUpdateChecker.htm)
[CheckAsync -
перегрузка](Overload_Tessa_Applications_Synchronization_ApplicationUpdateChecker_CheckAsync.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
