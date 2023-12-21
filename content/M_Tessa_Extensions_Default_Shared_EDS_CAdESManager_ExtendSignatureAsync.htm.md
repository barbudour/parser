# CAdESManager.ExtendSignatureAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task<SignedData> ExtendSignatureAsync(
    	byte[] certificate,
    	SignatureData signature,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function ExtendSignatureAsync ( 
    	certificate As Byte(),
    	signature As SignatureData,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of SignedData)
C++ __Копировать
     public:
    virtual Task<SignedData^>^ ExtendSignatureAsync(
    	array<unsigned char>^ certificate, 
    	SignatureData^ signature, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ExtendSignatureAsync : 
            certificate : byte[] * 
            signature : SignatureData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignedData> 
    override ExtendSignatureAsync : 
            certificate : byte[] * 
            signature : SignatureData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignedData> 
#### Параметры
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
signature [SignatureData](T_Tessa_Platform_EDS_SignatureData.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[SignedData](T_Tessa_Platform_EDS_SignedData.htm)>
#### Реализации
[ICAdESManager.ExtendSignatureAsync(Byte[], SignatureData,
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_ExtendSignatureAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
