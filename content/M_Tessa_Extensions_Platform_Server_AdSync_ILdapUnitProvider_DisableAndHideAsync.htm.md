# ILdapUnitProvider.DisableAndHideAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task DisableAndHideAsync(
    	DateTime syncDate,
    	RoleType roleType,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function DisableAndHideAsync ( 
    	syncDate As DateTime,
    	roleType As RoleType,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ DisableAndHideAsync(
    	DateTime syncDate, 
    	RoleType roleType, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract DisableAndHideAsync : 
            syncDate : DateTime * 
            roleType : RoleType * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
syncDate [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
roleType [RoleType](T_Tessa_Roles_RoleType.htm)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
