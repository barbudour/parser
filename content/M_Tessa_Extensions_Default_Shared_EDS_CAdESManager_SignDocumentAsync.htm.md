# CAdESManager.SignDocumentAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task<SignatureData> SignDocumentAsync(
    	byte[] certificate,
    	ISignatureFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function SignDocumentAsync ( 
    	certificate As Byte(),
    	file As ISignatureFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of SignatureData)
C++ __Копировать
     public:
    virtual Task<SignatureData^>^ SignDocumentAsync(
    	array<unsigned char>^ certificate, 
    	ISignatureFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SignDocumentAsync : 
            certificate : byte[] * 
            file : ISignatureFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignatureData> 
    override SignDocumentAsync : 
            certificate : byte[] * 
            file : ISignatureFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<SignatureData> 
#### Параметры
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[SignatureData](T_Tessa_Platform_EDS_SignatureData.htm)>
#### Реализации
[ICAdESManager.SignDocumentAsync(Byte[], ISignatureFile,
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_SignDocumentAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
