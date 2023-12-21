# CAdESManager.CheckExtendedSignatureAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task<IReadOnlyCollection<SignatureValidationInfo>> CheckExtendedSignatureAsync(
    	SignedData signedData,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function CheckExtendedSignatureAsync ( 
    	signedData As SignedData,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IReadOnlyCollection(Of SignatureValidationInfo))
C++ __Копировать
     public:
    virtual Task<IReadOnlyCollection<SignatureValidationInfo^>^>^ CheckExtendedSignatureAsync(
    	SignedData^ signedData, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CheckExtendedSignatureAsync : 
            signedData : SignedData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyCollection<SignatureValidationInfo>> 
    override CheckExtendedSignatureAsync : 
            signedData : SignedData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyCollection<SignatureValidationInfo>> 
#### Параметры
signedData [SignedData](T_Tessa_Platform_EDS_SignedData.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[SignatureValidationInfo](T_Tessa_Platform_EDS_SignatureValidationInfo.htm)>>
#### Реализации
[ICAdESManager.CheckExtendedSignatureAsync(SignedData,
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_CheckExtendedSignatureAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
