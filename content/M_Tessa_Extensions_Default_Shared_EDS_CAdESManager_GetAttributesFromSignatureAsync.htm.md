# CAdESManager.GetAttributesFromSignatureAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<SignatureAttributes> GetAttributesFromSignatureAsync(
    	byte[] signature,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAttributesFromSignatureAsync ( 
    	signature As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of SignatureAttributes)
C++ __Копировать
     public:
    virtual Task<SignatureAttributes^>^ GetAttributesFromSignatureAsync(
    	array<unsigned char>^ signature, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAttributesFromSignatureAsync : 
            signature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignatureAttributes> 
    override GetAttributesFromSignatureAsync : 
            signature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignatureAttributes> 
#### Параметры
signature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[SignatureAttributes](T_Tessa_Platform_EDS_SignatureAttributes.htm)>
#### Реализации
[ICAdESManager.GetAttributesFromSignatureAsync(Byte[],
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_GetAttributesFromSignatureAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
