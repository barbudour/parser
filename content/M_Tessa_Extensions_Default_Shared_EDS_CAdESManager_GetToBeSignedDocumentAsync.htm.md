# CAdESManager.GetToBeSignedDocumentAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<byte[]> GetToBeSignedDocumentAsync(
    	byte[] certificate,
    	ISignatureFile file,
    	DateTime signingTime,
    	string digestAlgorithmOid = null,
    	string encryptionAlgorithmOid = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetToBeSignedDocumentAsync ( 
    	certificate As Byte(),
    	file As ISignatureFile,
    	signingTime As DateTime,
    	Optional digestAlgorithmOid As String = Nothing,
    	Optional encryptionAlgorithmOid As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public:
    virtual Task<array<unsigned char>^>^ GetToBeSignedDocumentAsync(
    	array<unsigned char>^ certificate, 
    	ISignatureFile^ file, 
    	DateTime signingTime, 
    	String^ digestAlgorithmOid = nullptr, 
    	String^ encryptionAlgorithmOid = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetToBeSignedDocumentAsync : 
            certificate : byte[] * 
            file : ISignatureFile * 
            signingTime : DateTime * 
            ?digestAlgorithmOid : string * 
            ?encryptionAlgorithmOid : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithmOid = defaultArg digestAlgorithmOid null
            let _encryptionAlgorithmOid = defaultArg encryptionAlgorithmOid null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
    override GetToBeSignedDocumentAsync : 
            certificate : byte[] * 
            file : ISignatureFile * 
            signingTime : DateTime * 
            ?digestAlgorithmOid : string * 
            ?encryptionAlgorithmOid : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithmOid = defaultArg digestAlgorithmOid null
            let _encryptionAlgorithmOid = defaultArg encryptionAlgorithmOid null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
#### Параметры
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
signingTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
digestAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
encryptionAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[ICAdESManager.GetToBeSignedDocumentAsync(Byte[], ISignatureFile, DateTime,
String, String,
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_GetToBeSignedDocumentAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
