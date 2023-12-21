# ApplicationUpdateChecker.CheckAsync(String, Nullable<Boolean>,
ApplicationPackage, CancellationToken) - метод
Осуществляет проверку обновления приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> CheckAsync(
    	string applicationAlias,
    	bool? client64Bit,
    	ApplicationPackage package,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CheckAsync ( 
    	applicationAlias As String,
    	client64Bit As Boolean?,
    	package As ApplicationPackage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ CheckAsync(
    	String^ applicationAlias, 
    	Nullable<bool> client64Bit, 
    	ApplicationPackage^ package, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CheckAsync : 
            applicationAlias : string * 
            client64Bit : Nullable<bool> * 
            package : ApplicationPackage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override CheckAsync : 
            applicationAlias : string * 
            client64Bit : Nullable<bool> * 
            package : ApplicationPackage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Идентификатор приложения 
client64Bit
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Признак того, что приложение является 64-битным. Укажите null, чтобы не фильтровать приложения по разрядности, и скачивать те из них, разрядность которых соответствует разрядности ОС или настройкам в карточке сотрудника. 
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
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
[IApplicationUpdateChecker.CheckAsync(String, Nullable<Boolean>,
ApplicationPackage,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationUpdateChecker_CheckAsync_2.htm)  
##  __См. также
#### Ссылки
[ApplicationUpdateChecker -
](T_Tessa_Applications_Synchronization_ApplicationUpdateChecker.htm)
[CheckAsync -
перегрузка](Overload_Tessa_Applications_Synchronization_ApplicationUpdateChecker_CheckAsync.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
